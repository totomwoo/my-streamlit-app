"""CSV 업로드 → 에이블 AI 핵심 분석(결론 + 꼭 필요한 그래프) + 직접 탐색 + HTML 보고서/메일 발송"""
from __future__ import annotations

import json
import os
import re
import smtplib
from datetime import datetime, timezone, timedelta
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html import escape
from io import BytesIO

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

MAX_CSV_BYTES = 15 * 1024 * 1024
MAX_RATIO_COLS = 6          # 비율표를 만들 수치형 컬럼 수 상한 (쌍의 수가 급증하지 않도록)
REPORT_FILENAME = "csv_visual_report.html"

# 그래프 색: 단일 시리즈는 앱 보라색, 여러 시리즈는 색맹 검증 팔레트를 정해진 순서로 사용
AI_ACCENT = "#6250d6"
AI_PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
FONT_FAMILY = "Pretendard, 'Noto Sans KR', 'Malgun Gothic', sans-serif"
PLOTLY_CONFIG = {"displayModeBar": False, "responsive": True}

AI_ROLE = """
당신은 마케팅팀 김 대리의 AI 개인비서 '에이블'의 데이터 분석 담당입니다.
업로드된 CSV의 컬럼 정보와 집계표만 보고, 김 대리가 바로 의사결정할 수 있는 분석 결과를 만듭니다.

[원칙]
1. 숫자는 아래 제공된 표([전체 합계], [전체 비율표], [...별 합계], [...별 비율표], [날짜별 합계])에 있는 값을 그대로 옮겨 적습니다.
   - 스스로 더하기·나누기·평균 내기 등 어떤 계산도 하지 않습니다. 표에 없는 숫자는 쓰지 않습니다.
   - 전환율, 건당 비용, 평균 단가처럼 나눗셈이 필요한 지표는 반드시 [비율표]에 적힌 값을 씁니다.
     비율표의 컬럼 'a/b'는 a ÷ b 입니다. 예) '유효신청수/방문수'는 전환율, '비용/유효신청수'는 신청당 비용(원).
   - 비율을 %로 말할 때만 표의 값에 100을 곱해 소수 첫째 자리까지 적습니다. 예) 0.1133 → 11.3%
     그 외 숫자(합계, 건당 비용 등)는 표의 값을 그대로 적습니다.
   - 순위나 비교(가장 높다/낮다)도 표에 적힌 값끼리만 비교합니다.
2. headline은 가장 중요한 결론 한 문장이며, 핵심 숫자를 포함합니다.
3. key_findings는 3개이며, 각각 표에서 가져온 숫자 근거를 포함합니다.
4. 비율 지표 쓰는 법
   - 전환율 = 성과 ÷ 방문수 → denominator "방문수", scale 100, unit "%"
   - 건당 비용 = 비용 ÷ 성과 → denominator 성과 컬럼, scale 1, unit "원"
   - 비율이 아니면 denominator는 null, scale은 1입니다.
5. 컬럼 이름은 주어진 이름을 글자 그대로 씁니다.

[그래프 고르는 법]
- 마케팅 성과 데이터(매체·채널, 소재, 비용, 신청·구매 등 성과 컬럼)라면 반드시 이 순서로 3개를 고릅니다.
  1) 매체별 건당 비용: bar, x=매체 컬럼, y=비용 컬럼, denominator=성과 컬럼, color_by=null
  2) 매체×소재 전환율: bar, x=매체 컬럼, y=성과 컬럼, denominator=방문수, scale 100, color_by=소재 컬럼
  3) 날짜별 성과 추이: line, x=날짜 컬럼, y=성과 컬럼, agg "sum", color_by=null
- 그 외 데이터는 결론을 보여주는 데 꼭 필요한 그래프만 2~4개 고릅니다.
- bar의 x는 범주형, line의 x는 날짜형, scatter의 x·y는 수치형 컬럼입니다.
- title은 20자 이내, metric_name은 지표 이름(예: 신청당 비용, 전환율, 유효신청수)입니다.
- insight는 그래프에서 읽어야 할 점을 표의 숫자와 함께 한 문장으로 씁니다.

[KPI]
- 마케팅 성과 데이터라면 총 성과 건수, 총 비용, 전체 전환율, 건당 비용 4개를 이 순서로 씁니다.

[제안·한계]
- recommendations는 바로 실행할 수 있는 제안 2~3개, caveats는 데이터 한계 1~2개입니다.
- 모든 문장은 정중한 한국어로 짧게 씁니다.
"""

AI_SCHEMA = {
    "type": "json_schema",
    "name": "csv_insight",
    "strict": True,
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["headline", "key_findings", "kpis", "charts", "recommendations", "caveats"],
        "properties": {
            "headline": {"type": "string"},
            "key_findings": {"type": "array", "items": {"type": "string"}},
            "kpis": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["label", "column", "denominator", "scale", "unit"],
                    "properties": {
                        "label": {"type": "string"},
                        "column": {"type": "string"},
                        "denominator": {"type": ["string", "null"]},
                        "scale": {"type": "number"},
                        "unit": {"type": "string"},
                    },
                },
            },
            "charts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["chart_type", "title", "metric_name", "x", "y", "denominator",
                                 "scale", "agg", "color_by", "unit", "insight"],
                    "properties": {
                        "chart_type": {"type": "string", "enum": ["bar", "line", "scatter"]},
                        "title": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "x": {"type": "string"},
                        "y": {"type": "string"},
                        "denominator": {"type": ["string", "null"]},
                        "scale": {"type": "number"},
                        "agg": {"type": "string", "enum": ["sum", "mean", "count"]},
                        "color_by": {"type": ["string", "null"]},
                        "unit": {"type": "string"},
                        "insight": {"type": "string"},
                    },
                },
            },
            "recommendations": {"type": "array", "items": {"type": "string"}},
            "caveats": {"type": "array", "items": {"type": "string"}},
        },
    },
}

# 앱 화면과 HTML 보고서가 같은 카드 스타일을 쓴다
AI_CSS = """<style>
.able-hero{border-radius:18px;padding:20px 24px;margin:4px 0 16px;
  background:linear-gradient(135deg,#6250d6 0%,#8a7cf0 100%);color:#fff;
  box-shadow:0 8px 24px rgba(98,80,214,.18);}
.able-hero .tag{font-size:12px;letter-spacing:.04em;opacity:.85;}
.able-hero .head{font-size:20px;font-weight:700;line-height:1.5;margin-top:6px;}
.able-kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 16px;}
.able-kpi{border:1px solid #ebe9f7;border-radius:14px;padding:14px 16px;background:#faf9ff;}
.able-kpi .l{font-size:12px;color:#6b6880;}
.able-kpi .v{font-size:22px;font-weight:700;color:#1f2430;margin-top:4px;white-space:nowrap;}
.able-card{border:1px solid #ebe9f7;border-radius:14px;padding:16px 20px;background:#fff;margin:0 0 16px;}
.able-card .t{font-size:15px;font-weight:700;color:#1f2430;margin-bottom:6px;}
.able-card ol,.able-card ul{margin:0;padding-left:1.2em;line-height:1.85;color:#2b2a35;font-size:14px;}
</style>"""

# HTML 보고서 전용 스타일 (앱 화면의 배경·여백·2열 그리드를 재현)
REPORT_CSS = """<style>
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{font-family:Pretendard,'Noto Sans KR','Malgun Gothic',sans-serif;color:#1e1b4b;
  background:linear-gradient(160deg,#EFEBFF 0%,#E7EEFF 55%,#E3F3FF 100%);min-height:100vh;}
.wrap{max-width:1100px;margin:0 auto;padding:36px 24px 48px;}
.top{display:flex;flex-direction:column;gap:10px;margin-bottom:18px;}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:16px;}
.brand i{width:34px;height:34px;border-radius:10px;background:#5B4BE0;color:#fff;font-style:normal;
  display:inline-flex;align-items:center;justify-content:center;}
.top h1{font-size:26px;font-weight:700;margin:0;letter-spacing:-.01em;}
.chips{display:flex;flex-wrap:wrap;gap:8px;}
.chip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;background:#fff;
  border:1px solid #ebe9f7;font-size:13px;color:#3f3f5f;}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:0 0 16px;}
.grid .able-card{margin:0;min-width:0;}
.chart .js-plotly-plot,.chart .plotly-graph-div{width:100%!important;}
.insight{margin:8px 0 0;font-size:13px;color:#6b6880;line-height:1.6;}
.empty{font-size:14px;color:#6b6880;}
details.able-card{padding:0;overflow:hidden;}
details.able-card summary{cursor:pointer;list-style:none;padding:14px 20px;font-size:15px;font-weight:700;color:#1f2430;
  display:flex;align-items:center;gap:8px;}
details.able-card summary::-webkit-details-marker{display:none;}
details.able-card summary::after{content:'펼치기';margin-left:auto;font-size:12px;font-weight:400;color:#6b6880;}
details.able-card[open] summary::after{content:'접기';}
details.able-card .body{padding:0 20px 18px;overflow-x:auto;}
details.able-card .lead{margin:0 0 12px;font-size:13px;color:#3f3f5f;line-height:1.7;}
table.dataframe{border-collapse:collapse;width:100%;font-size:13px;}
table.dataframe th,table.dataframe td{border:1px solid #ebe9f7;padding:7px 10px;text-align:left;white-space:nowrap;}
table.dataframe th{background:#f4f3ff;color:#3f3f5f;font-weight:600;}
table.dataframe tr:nth-child(even) td{background:#faf9ff;}
.foot{font-size:12px;color:#6b6880;line-height:1.7;margin-top:8px;}
@media (max-width:900px){
  .wrap{padding:24px 16px 36px;}
  .grid{grid-template-columns:1fr;}
  .top h1{font-size:22px;}
}
@media print{
  body{background:#fff;}
  .wrap{max-width:none;padding:0;}
  .able-hero{box-shadow:none;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
  .able-card,.able-kpi,.chart{break-inside:avoid;}
  details.able-card summary::after{content:'';}
}
</style>"""


# ---------------- 공통 ----------------
def _secret(name, default=""):
    """환경 변수 → st.secrets 순서로 읽는다 (app.py의 get_secret과 동일)"""
    value = os.getenv(name)
    if value:
        return value
    try:
        return st.secrets[name]
    except Exception:
        return default


def _send_report_email(to, subject, body, html_bytes, filename):
    """HTML 보고서를 첨부해 Gmail SMTP로 발송"""
    sender = _secret("GMAIL_ADDRESS")
    password = _secret("GMAIL_APP_PASSWORD")
    if not (sender and password):
        return {"status": "failed", "error": "GMAIL_ADDRESS / GMAIL_APP_PASSWORD 가 설정되지 않았습니다."}
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to
    msg.attach(MIMEText(body, "plain", "utf-8"))
    part = MIMEApplication(html_bytes, _subtype="html")
    part.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(part)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as s:
            s.starttls()
            s.login(sender, password)
            s.sendmail(sender, [to], msg.as_string())
        return {"status": "success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}


def _read_csv(upload):
    if upload.size > MAX_CSV_BYTES:
        raise ValueError("CSV 파일은 15MB 이하만 업로드할 수 있습니다.")
    raw = upload.getvalue()
    for encoding in ("utf-8-sig", "cp949", "euc-kr"):
        try:
            return pd.read_csv(BytesIO(raw), encoding=encoding, low_memory=False)
        except UnicodeDecodeError:
            pass
        except pd.errors.EmptyDataError:
            raise ValueError("비어 있는 CSV 파일입니다.") from None
        except (pd.errors.ParserError, ValueError) as exc:
            raise ValueError(f"CSV 형식을 확인해주세요: {exc}") from None
    raise ValueError("인코딩을 인식하지 못했습니다. UTF-8 또는 CP949 CSV를 사용해주세요.")


def _recognize_dates(frame):
    dates = {}
    for col in frame.columns:
        if pd.api.types.is_datetime64_any_dtype(frame[col]):
            dates[col] = pd.to_datetime(frame[col], errors="coerce")
            continue
        colname = str(col).lower()
        if not any(k in colname for k in ("date", "날짜", "일자", "일시", "시간", "timestamp")):
            continue
        parsed = pd.to_datetime(frame[col], errors="coerce")
        if len(parsed) and parsed.notna().mean() >= 0.7:
            dates[col] = parsed
    return dates


def _quality_table(frame):
    rows = []
    for col in frame:
        ser = frame[col]
        isnum = pd.api.types.is_numeric_dtype(ser) and not pd.api.types.is_bool_dtype(ser)
        rows.append({
            "컬럼": str(col), "자료형": str(ser.dtype), "결측치": int(ser.isna().sum()),
            "결측률(%)": round(ser.isna().mean() * 100, 2), "고유값 수": int(ser.nunique(dropna=True)),
            "평균(수치형)": round(float(pd.to_numeric(ser, errors="coerce").mean()), 3) if isnum and ser.notna().any() else None,
        })
    return pd.DataFrame(rows)


# ---------------- 숫자 표기 (앱 화면·그래프 라벨·HTML 보고서 공통) ----------------
def _fmt_num(v, unit=""):
    """정수가 아니면서 작은 값(100 미만)만 소수 첫째 자리, 그 외에는 천 단위 구분 정수"""
    if v is None or pd.isna(v):
        return "-"
    is_int = abs(v - round(v)) < 1e-9
    text = f"{v:,.1f}" if (not is_int and abs(v) < 100) else f"{v:,.0f}"
    return f"{text}{unit}"


def _value_fmt(values):
    """막대 값 라벨용 d3 포맷: _fmt_num과 같은 규칙 (소수가 있고 최대값이 100 미만일 때만 .1f)"""
    vals = pd.Series(values, dtype="float").dropna()
    if vals.empty:
        return ",.0f"
    has_frac = (vals % 1).abs().gt(1e-9).any()
    return ",.1f" if (has_frac and vals.abs().max() < 100) else ",.0f"


def _kpi_values(ai, frame, numbers):
    """KPI 값은 LLM이 아니라 코드가 직접 계산한다. 앱 화면과 HTML 보고서가 이 결과를 함께 쓴다 → [(라벨, 값)]"""
    cards = []
    for k in ai["kpis"][:4]:
        if k["column"] not in numbers or (k["denominator"] and k["denominator"] not in numbers):
            continue
        total = frame[k["column"]].sum()
        if k["denominator"]:
            d = frame[k["denominator"]].sum()
            total = total / d if d else float("nan")
        cards.append((k["label"], _fmt_num(total * (k["scale"] or 1), k["unit"])))
    return cards


def _basic_kpis(frame, numbers, total_missing):
    """AI 분석 전에도 보여 주는 기본 지표 4개 (화면 상단 metric과 같은 값)"""
    count = max(len(frame) * len(frame.columns), 1)
    return [
        ("데이터 행", f"{len(frame):,}"),
        ("컬럼 수", f"{len(frame.columns):,}"),
        ("수치형 컬럼", f"{len(numbers):,}"),
        ("결측 비율", f"{total_missing / count * 100:.1f}%"),
    ]


# ---------------- 공통 HTML 조각 (앱 화면 + 보고서) ----------------
def _html_list(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{escape(str(i))}</li>" for i in items) + f"</{tag}>"


def _hero_html(tag, headline):
    return (f"<div class='able-hero'><div class='tag'>{escape(tag)}</div>"
            f"<div class='head'>{escape(headline)}</div></div>")


def _kpis_html(cards):
    if not cards:
        return ""
    inner = "".join(f"<div class='able-kpi'><div class='l'>{escape(str(l))}</div>"
                    f"<div class='v'>{escape(str(v))}</div></div>" for l, v in cards)
    return "<div class='able-kpis'>" + inner + "</div>"


def _card_html(title, items, ordered=False):
    return f"<div class='able-card'><div class='t'>{escape(title)}</div>" + _html_list(items, ordered) + "</div>"


# ---------------- 에이블 AI 분석 ----------------
def _round_ratio(v):
    """작은 비율(전환율 등)은 소수 4자리, 큰 값(건당 비용 등)은 2자리로 반올림"""
    if pd.isna(v):
        return v
    return round(float(v), 4) if abs(v) < 10 else round(float(v), 2)


def _ratio_table(sums, nums):
    """합계표(행=범주, 열=수치형 컬럼)에서 수치형 컬럼 쌍의 비율 a÷b 를 모두 계산한다. 열 이름 'a/b' = a ÷ b"""
    out = pd.DataFrame(index=sums.index)
    for a in nums:
        for b in nums:
            if a != b:
                out[f"{a}/{b}"] = sums[a] / sums[b].where(sums[b] != 0)
    return out.map(_round_ratio)


def _ai_profile(frame, dates, numbers, cats):
    """LLM에 보낼 요약: 컬럼 정보 + 집계표 + 미리 계산한 비율표 + 샘플 5행 (원본 전체는 보내지 않음)
    LLM은 숫자를 직접 계산하지 않고 이 표의 값만 인용하도록 AI_ROLE에서 지시한다."""
    parts = [
        f"행 수: {len(frame)}, 컬럼 수: {len(frame.columns)}",
        "수치형 컬럼: " + ", ".join(map(str, numbers)),
        "날짜형 컬럼: " + ", ".join(map(str, dates)),
        "범주형 컬럼: " + ", ".join(f"{c}({frame[c].nunique()}개)" for c in cats),
    ]
    if numbers:
        nums = numbers[:MAX_RATIO_COLS]
        ratio_note = "(열 'a/b' = a ÷ b, %는 ×100)"
        parts.append("[수치형 요약]\n" + frame[numbers].describe().T.round(2).to_csv())
        overall = frame[numbers].sum().to_frame("전체").T
        parts.append("[전체 합계]\n" + overall.round(2).to_csv())
        if len(nums) >= 2:
            parts.append(f"[전체 비율표] {ratio_note}\n" + _ratio_table(overall, nums).to_csv())
        small = [c for c in cats if 1 < frame[c].nunique() <= 15]
        for c in small[:3]:
            sums = frame.groupby(c)[numbers].sum()
            parts.append(f"[{c}별 합계]\n" + sums.round(2).to_csv())
            if len(nums) >= 2:
                parts.append(f"[{c}별 비율표] {ratio_note}\n" + _ratio_table(sums, nums).to_csv())
        if len(small) >= 2:
            a, b = small[0], small[1]
            sums = frame.groupby([a, b])[numbers].sum()
            parts.append(f"[{a}×{b}별 합계]\n" + sums.round(2).to_csv())
            if len(nums) >= 2:
                parts.append(f"[{a}×{b}별 비율표] {ratio_note}\n" + _ratio_table(sums, nums).to_csv())
        for d, ser in list(dates.items())[:1]:
            daily = frame[numbers].groupby(ser.dt.date).sum()
            if len(daily) > 60:
                daily = frame[numbers].groupby(ser.dt.to_period("W").astype(str)).sum()
            parts.append(f"[{d}별 합계]\n" + daily.round(2).to_csv())
    parts.append("[샘플 5행]\n" + frame.head(5).to_csv(index=False))
    return "\n\n".join(parts)[:30000]


def _ai_analyze(filename, profile):
    from openai import OpenAI
    client = OpenAI(api_key=_secret("OPENAI_API_KEY") or None)
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": AI_ROLE},
            {"role": "user", "content": f"에이블, 이 데이터를 분석해 주세요.\n파일명: {filename}\n\n{profile}"},
        ],
        text={"format": AI_SCHEMA},
        temperature=0,
    )
    return json.loads(response.output_text)


def _style_fig(fig, title, ylabel):
    fig.update_layout(
        title=dict(text=f"<b>{escape(title)}</b>", x=0, xanchor="left", font=dict(size=15, color="#1f2430")),
        font=dict(family=FONT_FAMILY, size=12, color="#52514e"),
        height=340, margin=dict(l=64, r=12, t=64, b=8),       # 왼쪽 여백: y축 제목이 잘리지 않게
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title_text=""),
        hoverlabel=dict(bgcolor="#ffffff", bordercolor="#e5e3de", font=dict(size=12, color="#1f2430")),
        bargap=0.35, bargroupgap=0.08,
    )
    fig.update_xaxes(title_text="", showgrid=False, linecolor="#d9d6cf", ticks="", automargin=True)
    fig.update_yaxes(title_text=ylabel, gridcolor="rgba(82,81,78,0.12)", zeroline=False, tickformat=",",
                     automargin=True, title_standoff=12)
    return fig


def _build_ai_chart(spec, frame, dates, numbers, cats):
    """LLM이 고른 '그래프 설계도'를 실제 데이터로 계산해 그린다. 규칙에 안 맞으면 None"""
    kind, x, y = spec["chart_type"], spec["x"], spec["y"]
    den, color = spec["denominator"], spec["color_by"]
    scale = spec["scale"] or 1
    if y not in numbers or (den and den not in numbers):
        return None
    if color not in cats or color == x or frame[color].nunique() > 8:
        color = None
    ylabel = spec["metric_name"] or str(y)
    if spec["unit"]:
        ylabel += f" ({spec['unit']})"

    if kind == "scatter":
        if x not in numbers or x == y:
            return None
        if color and frame[color].nunique() > 3:
            color = None
        df = frame[[x, y] + ([color] if color else [])].dropna()
        fig = px.scatter(df, x=x, y=y, color=color, color_discrete_sequence=AI_PALETTE)
        fig.update_traces(marker=dict(size=10, opacity=0.85, line=dict(width=2, color="#ffffff")))
        if not color:
            fig.update_traces(marker_color=AI_ACCENT)
        return _style_fig(fig, spec["title"], ylabel)

    if kind == "line":
        if x not in dates:
            return None
        base = frame.assign(_x=dates[x].dt.date)
    elif kind == "bar":
        if x not in cats:
            return None
        base = frame.assign(_x=frame[x].astype(str))
    else:
        return None

    keys = ["_x"] + ([color] if color else [])
    grouped = base.groupby(keys, dropna=True)
    if den:
        s = grouped[[y, den]].sum()
        val = s[y] / s[den].where(s[den] != 0) * scale
    elif spec["agg"] == "mean":
        val = grouped[y].mean() * scale
    elif spec["agg"] == "count":
        val = grouped[y].count()
    else:
        val = grouped[y].sum() * scale
    df = val.rename("value").reset_index().dropna(subset=["value"]).rename(columns={"_x": x})
    if df.empty:
        return None
    df["value"] = df["value"].astype(float)
    fmt = _value_fmt(df["value"])    # 예: 8,231원은 "8,231", 전환율 11.3%는 "11.3"
    labels = {"value": ylabel, x: str(x)}
    if color:
        labels[color] = str(color)

    if kind == "bar":
        order = df.groupby(x)["value"].sum().sort_values(ascending=False).index.tolist()
        orders = {x: order}
        if color:
            orders[color] = sorted(df[color].astype(str).unique())
        fig = px.bar(df, x=x, y="value", color=color, barmode="group", labels=labels,
                     category_orders=orders, color_discrete_sequence=AI_PALETTE)
        fig.update_traces(marker_cornerradius=4, marker_line_width=0)
        if not color:
            fig.update_traces(marker_color=AI_ACCENT)
        if len(df) <= 12:   # 막대 수가 적을 때만 값 라벨 (글자색은 회색 텍스트 색)
            fig.update_traces(texttemplate="%{y:" + fmt + "}", textposition="outside",
                              textfont=dict(size=11, color="#52514e"), cliponaxis=False)
        fig.update_yaxes(range=[0, df["value"].max() * 1.18])   # 위쪽 라벨이 잘리지 않게 여백
    else:
        df = df.sort_values(x)
        fig = px.line(df, x=x, y="value", color=color, markers=True, labels=labels,
                      color_discrete_sequence=AI_PALETTE)
        fig.update_traces(line=dict(width=2), marker=dict(size=8, line=dict(width=2, color="#ffffff")))
        if not color:
            fig.update_traces(line_color=AI_ACCENT, marker_color=AI_ACCENT)
        fig.update_layout(hovermode="x unified")
        fig.update_xaxes(tickformat="%m/%d")
    return _style_fig(fig, spec["title"], ylabel)


def _render_ai(ai, frame, dates, numbers, cats):
    """에이블 AI 분석 화면. 보고서에 실을 (설계도, 그래프) 목록을 돌려준다"""
    st.markdown(AI_CSS, unsafe_allow_html=True)
    st.markdown(_hero_html("🤖 에이블 핵심 결론", ai["headline"]), unsafe_allow_html=True)

    # KPI 카드 (값은 코드가 직접 계산, 긴 숫자도 잘리지 않게 HTML 카드)
    kpis = _kpi_values(ai, frame, numbers)
    if kpis:
        st.markdown(_kpis_html(kpis), unsafe_allow_html=True)

    st.markdown(_card_html("📌 핵심 발견", ai["key_findings"], ordered=True), unsafe_allow_html=True)

    # 꼭 필요한 그래프만 (2열 카드)
    built = []
    for spec in ai["charts"][:4]:
        try:
            fig = _build_ai_chart(spec, frame, dates, numbers, cats)
        except Exception:
            fig = None
        if fig is not None:
            built.append((spec, fig))
    for i in range(0, len(built), 2):
        pair = built[i:i + 2]
        cols = st.columns(2) if len(pair) == 2 else [st.container()]
        for j, (col, (spec, fig)) in enumerate(zip(cols, pair)):
            with col.container(border=True):
                st.plotly_chart(fig, use_container_width=True, key=f"csv_ai_chart_{i + j}",
                                config={"displayModeBar": False})
                st.caption("💡 " + spec["insight"])
    if not built:
        st.info("AI가 고른 그래프를 그릴 수 없었습니다. 아래 '직접 탐색'에서 확인해 주세요.")

    left, right = st.columns(2)
    left.markdown(_card_html("✅ 제안", ai["recommendations"]), unsafe_allow_html=True)
    right.markdown(_card_html("⚠️ 데이터 한계", ai["caveats"]), unsafe_allow_html=True)
    return built


# ---------------- HTML 보고서 ----------------
def _report_fig(fig):
    """보고서용 복사본에 앱 그래프와 같은 글꼴·배경·여백을 입힌다 (화면에 그린 그래프 객체는 바꾸지 않음)"""
    rep = go.Figure(fig.to_dict())
    title = rep.layout.title.text or ""
    if title and not title.startswith("<b>"):
        title = f"<b>{title}</b>"
    rep.update_layout(
        title=dict(text=title, x=0, xanchor="left", font=dict(size=15, color="#1f2430")),
        font=dict(family=FONT_FAMILY, size=12, color="#52514e"),
        height=340, margin=dict(l=64, r=12, t=64, b=8), autosize=True,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    )
    rep.update_xaxes(automargin=True)
    rep.update_yaxes(automargin=True, gridcolor="rgba(82,81,78,0.12)", zeroline=False)
    if len(rep.data) == 1:          # 직접 탐색 그래프(단일 시리즈)는 앱 보라색으로 통일
        trace = rep.data[0]
        if trace.type == "scatter":
            trace.update(marker_color=AI_ACCENT, line_color=AI_ACCENT)
        else:
            trace.update(marker_color=AI_ACCENT)
    return rep


def _report_html(filename, frame, quality, ai, ai_built, manual_figures, basic_notes, kpis):
    """앱의 AI 분석 화면과 같은 구성·팔레트로 HTML 보고서를 만든다.
    ai=None 이면 기본 요약과 직접 탐색 그래프만 같은 카드 스타일로 담는다."""
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST")
    h = ["<!doctype html><html lang='ko'><head><meta charset='utf-8'>",
         "<meta name='viewport' content='width=device-width, initial-scale=1'>",
         "<title>에이블 CSV 시각화 보고서</title>",
         "<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css'>",
         AI_CSS, REPORT_CSS, "</head><body><div class='wrap'>",
         "<header class='top'><div class='brand'><i>A</i><span>에이블</span></div>",
         "<h1>에이블 CSV 시각화 보고서</h1><div class='chips'>",
         f"<span class='chip'>📄 원본 파일 · {escape(filename)}</span>",
         f"<span class='chip'>🕒 생성 {escape(now)}</span>",
         f"<span class='chip'>📊 {len(frame):,}행 × {len(frame.columns):,}열</span>",
         "</div></header>"]

    if ai:
        h.append(_hero_html("🤖 에이블 핵심 결론", ai["headline"]))
        h.append(_kpis_html(kpis))
        h.append(_card_html("📌 핵심 발견", ai["key_findings"], ordered=True))
    else:
        h.append(_hero_html("📋 기본 요약", "AI 분석을 실행하지 않아 데이터 기본 요약과 직접 선택한 그래프만 담았습니다."))
        h.append(_kpis_html(kpis))
        h.append(_card_html("📌 주요 결과 및 유의점", basic_notes))

    # 그래프 카드 (제목은 그래프 안에 한 번만, AI 그래프에는 💡 insight)
    charts = [(fig, spec["insight"]) for spec, fig in ai_built] + [(fig, None) for _, fig in manual_figures]
    if charts:
        h.append("<div class='grid'>")
        for i, (fig, insight) in enumerate(charts):
            h.append("<div class='able-card chart'>")
            h.append(pio.to_html(_report_fig(fig), full_html=False, include_plotlyjs=(i == 0),
                                 config=PLOTLY_CONFIG))
            if insight:
                h.append(f"<p class='insight'>💡 {escape(insight)}</p>")
            h.append("</div>")
        h.append("</div>")
    else:
        h.append("<div class='able-card'><div class='t'>📈 시각화</div>"
                 "<p class='empty'>현재 CSV에는 생성 가능한 시각화 조합이 없습니다.</p></div>")

    if ai:
        h.append("<div class='grid'>" + _card_html("✅ 제안", ai["recommendations"])
                 + _card_html("⚠️ 데이터 한계", ai["caveats"]) + "</div>")

    h.append("<details class='able-card'><summary>🧪 컬럼 품질 요약</summary><div class='body'>")
    h.append("<p class='lead'>" + " ".join(escape(n) for n in basic_notes) + "</p>")
    h.append(quality.to_html(index=False, escape=True, na_rep="-", border=0))
    h.append("</div></details>")
    h.append("<details class='able-card'><summary>🔍 데이터 미리보기 (최대 20행)</summary><div class='body'>")
    h.append(frame.head(20).to_html(index=False, escape=True, na_rep="-", border=0))
    h.append("</div></details>")
    h.append("<p class='foot'>분석은 파일 내 값으로만 수행했으며 결측치는 임의로 0으로 대체하지 않았습니다. "
             "상관관계는 인과관계를 의미하지 않습니다.</p>")
    h.append("<script>window.addEventListener('beforeprint',function(){"
             "document.querySelectorAll('details').forEach(function(d){d.open=true;});});</script>")
    h.append("</div></body></html>")
    return "\n".join(h).encode("utf-8")


# ---------------- 메일 보내기 팝업 ----------------
@st.dialog("📧 보고서 메일로 보내기", width="large")
def _mail_dialog():
    """보고서 메일 발송 팝업. 필요한 데이터는 rerun 후에도 남도록 session_state에서 읽는다"""
    data = st.session_state.get("csv_mail_payload")
    if not data:
        st.warning("보낼 보고서가 없습니다. 창을 닫고 다시 시도해 주세요.")
        return
    st.caption(f"첨부 파일: `{REPORT_FILENAME}` · 원본 `{data['source']}`")
    to = st.text_input("받는 사람", value=_secret("MY_EMAIL"), placeholder="본인이메일@gmail.com", key="csv_mail_to")
    subject = st.text_input("제목", value=data["subject"], key=f"csv_mail_subject_{data['source']}")
    memo = st.text_area("전달 메모 (선택)", placeholder="예: 금요일 예산 배분 회의 자료입니다.", key="csv_mail_memo")
    if st.button("보고서 메일 보내기", type="primary", key="csv_mail_send", use_container_width=True):
        to = to.strip()
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", to):
            st.warning("받는 사람 이메일 주소를 확인해주세요.")
            return
        body = (memo.strip() + "\n\n" if memo.strip() else "")
        body += "[주요 결과]\n" + "\n".join("- " + n for n in data["notes"])
        body += "\n\n첨부한 HTML 파일을 브라우저로 열면 그래프를 확인할 수 있습니다."
        with st.spinner("메일을 보내는 중입니다..."):
            result = _send_report_email(to, subject.strip() or data["subject"], body, data["html"], REPORT_FILENAME)
        if result["status"] == "success":
            st.success(f"{to} 로 보고서를 보냈습니다. 창을 닫아도 됩니다.")
        else:
            st.error("메일 발송에 실패했습니다: " + result["error"])


# ---------------- 화면 ----------------
def render_csv_report():
    st.title("CSV 업로드 · 데이터 시각화 보고서")
    st.caption("원본 파일은 수정하지 않습니다. AI 분석 시 원본 전체가 아닌 컬럼 정보·집계표·샘플 5행만 OpenAI로 보냅니다.")
    upload = st.file_uploader("분석할 CSV 파일 업로드", type=["csv"], key="csv_report_file")
    if upload is None:
        st.info("CSV를 업로드하면 에이블이 핵심 결론과 꼭 필요한 그래프를 골라 보여드립니다.")
        return
    try:
        raw = _read_csv(upload)
    except (ValueError, OSError, UnicodeError) as exc:
        st.error(str(exc))
        return
    if raw.empty or len(raw.columns) == 0:
        st.warning("분석할 행이나 컬럼이 없습니다.")
        return

    frame = raw.copy()
    quality = _quality_table(frame)
    numbers = [c for c in frame.columns if pd.api.types.is_numeric_dtype(frame[c]) and not pd.api.types.is_bool_dtype(frame[c])]
    dates = _recognize_dates(frame)
    cats = [c for c in frame.columns if c not in numbers and c not in dates]
    total_missing = int(frame.isna().sum().sum())
    count = max(len(frame) * len(frame.columns), 1)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("데이터 행", f"{len(frame):,}")
    m2.metric("컬럼 수", len(frame.columns))
    m3.metric("수치형 컬럼", len(numbers))
    m4.metric("결측 비율", f"{total_missing / count * 100:.1f}%")

    # 1) 에이블 AI 분석
    sig = f"{upload.name}:{upload.size}"
    store = st.session_state.setdefault("csv_ai_results", {})
    head_col, btn_col = st.columns([3, 1], vertical_alignment="center")
    head_col.subheader("🤖 에이블 AI 분석")
    run = btn_col.button("다시 분석" if sig in store else "AI 핵심 분석", type="primary",
                         use_container_width=True, key="csv_ai_run")
    if run:
        with st.spinner("에이블이 데이터를 분석하고 있습니다..."):
            try:
                store[sig] = _ai_analyze(upload.name, _ai_profile(frame, dates, numbers, cats))
            except Exception as exc:
                st.error(f"AI 분석에 실패했습니다: {exc}")
    ai = store.get(sig)
    ai_built = _render_ai(ai, frame, dates, numbers, cats) if ai else []
    if not ai:
        st.info("버튼을 누르면 에이블이 데이터를 분석해 핵심 결론과 꼭 필요한 그래프만 골라 보여드립니다.")

    basic_notes = [
        f"전체 {len(frame):,}행 / {len(frame.columns)}개 컬럼, 수치형 {len(numbers)}개, 날짜형 후보 {len(dates)}개.",
        f"전체 셀 기준 결측치 {total_missing:,}개 ({total_missing / count * 100:.2f}%).",
    ]
    notes = list(basic_notes)
    if ai:
        notes = ([f"핵심 결론: {ai['headline']}"]
                 + [f"발견: {f}" for f in ai["key_findings"]]
                 + [f"제안: {r}" for r in ai["recommendations"]]
                 + [f"데이터 한계: {c}" for c in ai["caveats"]]
                 + notes)

    # 2) 원본 데이터 · 직접 탐색 (기존 기능)
    manual_figures = []
    with st.expander("📂 원본 데이터 · 직접 탐색", expanded=not ai):
        tab_prev, tab_quality, tab_viz = st.tabs(["데이터 미리보기", "데이터 품질", "직접 시각화"])
        with tab_prev:
            st.dataframe(frame.head(100), use_container_width=True, hide_index=True)
            st.caption("원본 데이터는 유지됩니다. 미리보기는 최대 100행입니다.")
        with tab_quality:
            st.dataframe(quality, use_container_width=True, hide_index=True)
            st.download_button("컬럼 품질표 CSV 다운로드", quality.to_csv(index=False).encode("utf-8-sig"),
                               file_name="csv_quality_summary.csv", mime="text/csv", key="csv_quality_export")
        with tab_viz:
            if numbers:
                num = st.selectbox("분포를 확인할 수치형 컬럼", numbers, key="csv_report_hist_num")
                plot_frame = frame[[num]].dropna()
                if not plot_frame.empty:
                    fig = px.histogram(plot_frame, x=num, nbins=30, title=f"{num} 분포")
                    manual_figures.append((f"{num} 분포", fig))
                    st.plotly_chart(fig, use_container_width=True, key="csv_r_hist")
            if cats and numbers:
                left, right = st.columns(2)
                category = left.selectbox("비교할 범주형 컬럼", cats, key="csv_r_group_col")
                target = right.selectbox("비교할 수치형 컬럼", numbers, key="csv_r_group_metric")
                agg_type = st.radio("범주별 집계", ["합계", "평균", "건수"], horizontal=True, key="csv_r_agg")
                src = frame[[category, target]].dropna(subset=[category])
                if agg_type == "합계":
                    grouped = src.groupby(category, dropna=False)[target].sum(min_count=1)
                elif agg_type == "평균":
                    grouped = src.groupby(category, dropna=False)[target].mean()
                else:
                    grouped = src.groupby(category, dropna=False)[target].count()
                grouped = grouped.dropna().sort_values(ascending=False).head(15).reset_index(name="value")
                if not grouped.empty:
                    fig = px.bar(grouped, x=category, y="value", title=f"{category}별 {target} {agg_type} (상위 15개)")
                    manual_figures.append((f"{category}별 {target} {agg_type}", fig))
                    st.plotly_chart(fig, use_container_width=True, key="csv_r_bar")
            if dates and numbers:
                left, right = st.columns(2)
                date_col = left.selectbox("시계열 날짜 컬럼", list(dates), key="csv_r_date_col")
                time_metric = right.selectbox("시계열 수치 컬럼", numbers, key="csv_r_time_metric")
                tmp = pd.DataFrame({"date": dates[date_col], "value": frame[time_metric]}).dropna()
                if not tmp.empty:
                    daily = tmp.assign(date=tmp["date"].dt.date).groupby("date", as_index=False)["value"].sum()
                    fig = px.line(daily, x="date", y="value", markers=True, title=f"일자별 {time_metric} 합계")
                    manual_figures.append((f"일자별 {time_metric} 합계", fig))
                    st.plotly_chart(fig, use_container_width=True, key="csv_r_line")
            if len(numbers) > 1:
                x, y = st.columns(2)
                xcol = x.selectbox("산점도 X축", numbers, index=0, key="csv_r_x")
                ycol = y.selectbox("산점도 Y축", numbers, index=1, key="csv_r_y")
                clean = frame[[xcol, ycol]].dropna()
                if not clean.empty:
                    if len(clean) > 3000:
                        clean = clean.sample(3000, random_state=42)
                    fig = px.scatter(clean, x=xcol, y=ycol, opacity=0.6, title=f"{xcol} · {ycol} 관계")
                    manual_figures.append((f"{xcol} · {ycol} 산점도", fig))
                    st.plotly_chart(fig, use_container_width=True, key="csv_r_scatter")

    # 3) 보고서 다운로드 · 이메일 (팝업)
    st.subheader("📄 시각화 보고서")
    kpis = _kpi_values(ai, frame, numbers) if ai else _basic_kpis(frame, numbers, total_missing)
    html_bytes = _report_html(upload.name, frame, quality, ai, ai_built, manual_figures, basic_notes, kpis)
    dl_col, mail_col = st.columns(2)
    dl_col.download_button("HTML 시각화 보고서 다운로드", data=html_bytes, file_name=REPORT_FILENAME,
                           mime="text/html", key="csv_html_export", type="primary", use_container_width=True)
    if mail_col.button("📧 보고서 메일로 보내기", key="csv_mail_open", use_container_width=True):
        st.session_state["csv_mail_payload"] = {
            "html": html_bytes, "notes": notes, "source": upload.name,
            "subject": f"[CSV 시각화 보고서] {upload.name}",
        }
        _mail_dialog()
    st.caption("AI 분석을 실행하면 보고서에 에이블의 결론과 그래프가 함께 들어갑니다.")
