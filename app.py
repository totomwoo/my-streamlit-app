# =========================================================
# 에이블(able.) — 김 대리의 음성 AI 개인비서
# KT AIVLE School 미니프로젝트 3차
#
# 구성
#   1) 설정   : 라이브러리, 상수, Secrets, 외부 서비스 클라이언트, CSS
#   2) 상태   : session_state 초기화
#   3) 도구 함수 : 날짜/이메일/캘린더/월간 그리드 등 순수 함수
#   4) LLM    : 회의록 분석(구조화 출력), 대화(함수 호출 루프), STT, TTS
#   5) 화면   : 헤더 / 왼쪽(브리핑·업무·캘린더) / 오른쪽(대화 패널)
# =========================================================

import os, json, html, hashlib, uuid, smtplib
import calendar as cal_lib
from datetime import date, datetime, timedelta, timezone
from email.mime.text import MIMEText

import streamlit as st
from openai import OpenAI

# 구글 캘린더 라이브러리 (없어도 앱은 동작해야 함)
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GCAL_LIB_OK = True
except Exception:
    GCAL_LIB_OK = False


# =========================================================
# 1) 설정
# =========================================================
st.set_page_config(page_title="able. — 김 대리의 AI 비서", page_icon="◼", layout="wide")

KST = timezone(timedelta(hours=9))          # 한국 시간 (서머타임 없음)
LLM_MODEL = "gpt-4o-mini"
STT_MODEL = "whisper-1"
TTS_MODEL = "gpt-4o-mini-tts"               # 실패하면 tts-1 로 재시도
TTS_VOICE = "alloy"
MAX_TURNS = 10                              # 대화 기록 유지 턴 수
WEEKDAY_KO = ["월", "화", "수", "목", "금", "토", "일"]
WEEKDAY_EN = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
CAL_SCOPES = ["https://www.googleapis.com/auth/calendar"]
USER_NAME = "김 대리"


def get_secret(name, default=None):
    """환경 변수 → st.secrets 순서로 읽는다. (Cloud의 최상위 Secrets는 환경 변수로도 제공됨)"""
    value = os.getenv(name)
    if value:
        return value
    try:
        return st.secrets[name]
    except Exception:
        return default


def get_service_account_info():
    """st.secrets 의 [gcp_service_account] 표를 dict 로. 없으면 None"""
    try:
        info = dict(st.secrets["gcp_service_account"])
        if info.get("private_key"):
            info["private_key"] = info["private_key"].replace("\\n", "\n")
        return info if info.get("client_email") else None
    except Exception:
        return None


OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
GMAIL_ADDRESS = get_secret("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = get_secret("GMAIL_APP_PASSWORD")
MY_EMAIL = get_secret("MY_EMAIL") or GMAIL_ADDRESS or ""   # 기본 수신자
GOOGLE_CALENDAR_ID = get_secret("GOOGLE_CALENDAR_ID")
SA_INFO = get_service_account_info()
GMAIL_OK = bool(GMAIL_ADDRESS and GMAIL_APP_PASSWORD)


# ---- OpenAI 클라이언트 ----
@st.cache_resource(show_spinner=False)
def get_openai_client(api_key):
    return OpenAI(api_key=api_key)


client = get_openai_client(OPENAI_API_KEY) if OPENAI_API_KEY else None


# ---- 구글 캘린더 서비스 (서비스 계정) ----
@st.cache_resource(show_spinner=False)
def get_calendar_service(sa_json):
    creds = service_account.Credentials.from_service_account_info(json.loads(sa_json), scopes=CAL_SCOPES)
    return build("calendar", "v3", credentials=creds, cache_discovery=False)


calendar_service, CAL_SETUP_ERROR = None, None
if not GCAL_LIB_OK:
    CAL_SETUP_ERROR = "google-api-python-client 가 설치되지 않았습니다."
elif not (SA_INFO and GOOGLE_CALENDAR_ID):
    CAL_SETUP_ERROR = "Secrets 에 gcp_service_account 또는 GOOGLE_CALENDAR_ID 가 없습니다."
else:
    try:
        calendar_service = get_calendar_service(json.dumps(SA_INFO, sort_keys=True))
    except Exception as e:
        CAL_SETUP_ERROR = f"캘린더 인증 실패: {e}"
CAL_OK = calendar_service is not None


# ---- 디자인 토큰 / CSS (에디토리얼 모노) ----
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=IBM+Plex+Sans+KR:wght@300;400;500;600&display=swap');
:root{--paper:#ECEBE7;--ink:#1C1C1C;--gray:#5F5E5A;--rule:#C9C7C1;--charcoal:#4B4B4D;--stripe:#3E3E40;--card:#5A5A5C;--on-dark:#F1F0EC;--on-dark-muted:#CFCDC7;}
.stApp{background:var(--paper);color:var(--ink);}
.stApp p,.stApp div,.stApp span,.stApp label,.stApp input,.stApp textarea,.stApp button{font-family:'IBM Plex Sans KR',sans-serif;}
.stApp .able-no,.stApp .able-due,.stApp .able-daynum,.stApp .able-month,.stApp .able-mark-sm,.stApp .able-wordmark{font-family:'Inter',sans-serif;}
header[data-testid="stHeader"]{background:transparent;}
.block-container{padding:40px 64px 64px;max-width:1440px;}
/* 버튼: 각진 모서리, 얇은 선 */
.stButton>button,.stFormSubmitButton>button{border-radius:0;border:1px solid var(--ink);background:transparent;color:var(--ink);font-size:12px;min-height:40px;padding:0 14px;box-shadow:none;}
.stButton>button:hover,.stFormSubmitButton>button:hover{background:var(--ink);color:var(--paper);border-color:var(--ink);}
.stButton>button[kind="primary"]{background:var(--ink);color:var(--paper);}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="base-input"],[data-testid="stFileUploaderDropzone"]{border-radius:0!important;}
/* 타이포 */
.able-wordmark{font-family:'Inter',sans-serif;font-weight:500;font-size:96px;line-height:.9;letter-spacing:-.05em;margin:0;}
.able-meta{font-size:12px;line-height:1.6;color:var(--gray);text-align:right;}
.able-tagline{margin-top:24px;padding-bottom:16px;border-bottom:1px solid var(--rule);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-size:14px;color:#3F3E3B;}
.able-section{font-size:12px;color:var(--gray);margin:28px 0 10px;letter-spacing:.02em;}
.able-lead{font-size:24px;line-height:1.5;font-weight:300;letter-spacing:-.01em;margin:0 0 10px;}
.able-sub{font-size:13px;line-height:1.7;color:var(--gray);margin:0 0 4px;}
.able-hint{font-size:13px;line-height:1.7;color:var(--gray);margin:4px 0 0;}
.able-no{font-family:'Inter',sans-serif;font-size:13px;color:var(--gray);}
.able-task-title{display:block;font-size:16px;font-weight:500;}
.able-task-detail{display:block;font-size:12px;color:var(--gray);margin-top:2px;}
.able-due{font-family:'Inter',sans-serif;font-size:13px;}
.able-muted{color:var(--gray);}
.able-rule{border-bottom:1px solid var(--rule);margin:4px 0 8px;}
.able-rule-dark{border-bottom:1px solid var(--ink);margin:0 0 4px;}
.able-registered{display:inline-flex;align-items:center;gap:8px;font-size:12px;}
.able-registered i{display:inline-block;width:8px;height:8px;background:var(--ink);}
/* 캘린더 */
.able-month{font-family:'Inter',sans-serif;font-size:20px;font-weight:500;letter-spacing:-.02em;line-height:40px;}
.able-legend{font-size:12px;color:#3F3E3B;display:flex;gap:16px;justify-content:flex-end;line-height:40px;}
.able-legend i{display:inline-block;width:10px;height:10px;margin-right:6px;vertical-align:-1px;}
.able-grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));border-top:1px solid var(--ink);border-left:1px solid var(--rule);}
.able-grid-head{padding:8px;font-size:11px;color:var(--gray);border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);}
.able-cell{min-height:76px;padding:8px;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);display:flex;flex-direction:column;gap:5px;min-width:0;}
.able-cell-today{background:#E2E1DC;}
.able-daynum{font-family:'Inter',sans-serif;font-size:13px;color:var(--gray);}
.able-cell-today .able-daynum{color:var(--ink);font-weight:500;}
.able-chip{font-size:11px;padding:2px 6px;line-height:1.4;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.able-chip-fill{background:var(--ink);color:var(--paper);}
.able-chip-line{border:1px solid var(--ink);color:var(--ink);}
.able-more{font-size:11px;color:var(--gray);}
/* 오른쪽 차콜 패널 */
.st-key-able_strip{background:repeating-linear-gradient(90deg,var(--stripe) 0 2px,var(--charcoal) 2px 5px);padding:18px 24px;box-shadow:0 18px 40px rgba(0,0,0,.18);}
.st-key-able_strip p,.st-key-able_strip span,.st-key-able_strip div{color:var(--on-dark);}
.st-key-able_chat{background:var(--charcoal);padding:24px;box-shadow:0 24px 48px rgba(0,0,0,.22);}
.st-key-able_chat p,.st-key-able_chat span,.st-key-able_chat label,.st-key-able_chat [data-testid="stMarkdownContainer"]{color:var(--on-dark);}
.st-key-able_chat .stButton>button,.st-key-able_chat .stFormSubmitButton>button{border-color:var(--on-dark);color:var(--on-dark);background:transparent;width:100%;}
.st-key-able_chat .stButton>button:hover,.st-key-able_chat .stFormSubmitButton>button:hover{background:var(--paper);color:var(--ink);}
.st-key-able_chat .stButton>button[kind="primary"]{background:var(--paper);color:var(--ink);border-color:var(--paper);font-weight:600;}
.st-key-able_chat [data-baseweb="input"],.st-key-able_chat [data-baseweb="textarea"],.st-key-able_chat [data-baseweb="base-input"]{background:transparent!important;border-color:var(--on-dark-muted)!important;}
.st-key-able_chat input,.st-key-able_chat textarea{color:var(--on-dark)!important;background:transparent!important;-webkit-text-fill-color:var(--on-dark);}
.st-key-able_card{background:var(--card);padding:16px;}
.able-label{font-size:11px;color:var(--on-dark-muted)!important;letter-spacing:.04em;display:block;margin-bottom:4px;}
.able-you{margin:0 0 14px;font-size:14px;line-height:1.7;}
.able-answer{margin:0 0 4px;font-size:16px;line-height:1.7;font-weight:300;}
.able-tool{display:block;font-size:12px;color:var(--on-dark-muted)!important;}
.able-gap{height:10px;}
.able-mark-sm{font-family:'Inter',sans-serif;font-size:40px;font-weight:500;letter-spacing:-.05em;line-height:1;}
.able-foot{font-size:11px;color:var(--on-dark-muted)!important;text-align:right;line-height:1.5;}
.able-footer{margin-top:48px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-size:11px;color:var(--gray);letter-spacing:.04em;}
.able-status{display:inline-flex;align-items:center;gap:8px;font-size:12px;background:#2F2F31;padding:6px 10px;float:right;margin-top:14px;}
.able-status i{width:7px;height:7px;border-radius:50%;background:var(--on-dark);display:inline-block;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# =========================================================
# 2) 상태
# =========================================================
today = datetime.now(KST).date()

DEFAULTS = {
    "messages": [],              # [{"id","role","content","via","tools"}] user/assistant 만
    "meeting_text": None,        # 회의록 원문
    "meeting_name": None,        # 파일 이름
    "meeting_date": today.isoformat(),
    "briefing": None,            # {"title","participants","summary","facts"}
    "tasks": [],                 # [{"id","title","detail","requester","due","suggested_due","suggest_reason","event_id"}]
    "briefing_key": None,        # 마지막으로 분석한 (파일명, 해시, 날짜)
    "pending_actions": [],       # 확인 대기 중인 도구 실행 (이메일/캘린더). 앞에서부터 하나씩 카드로 표시
    "last_audio_hash": None,     # 같은 녹음을 두 번 처리하지 않기 위한 해시
    "tts_audio": None,           # 최신 답변 음성(bytes)
    "tts_autoplay": False,       # 최신 답변만 자동 재생
    "brief_audio": None,         # 브리핑 듣기 음성
    "brief_autoplay": False,
    "local_events": [],          # 캘린더 미연결 시 앱 안에 기록한 일정
    "cal_year": today.year,
    "cal_month": today.month,
    "picking_task": None,        # 날짜 선택 UI 가 열린 업무 id
    "notice": None,              # (종류, 문구) 다음 화면에 한 번 표시
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


def set_notice(kind, text):
    """사용자에게 보여줄 안내/오류 (다음 rerun 에서 한 번 표시)"""
    st.session_state.notice = (kind, text)


# =========================================================
# 3) 도구 함수 (순수 함수 중심)
# =========================================================
def esc(text):
    """HTML 이스케이프 + 줄바꿈 유지"""
    return html.escape(str(text or "")).replace("\n", "<br>")


def parse_iso(s):
    """'YYYY-MM-DD' → date, 실패하면 None"""
    try:
        return date.fromisoformat(str(s)[:10])
    except Exception:
        return None


def fmt_due(iso):
    """2026-11-13 → '11.13 FRI'"""
    d = parse_iso(iso)
    return f"{d.month:02d}.{d.day:02d} {WEEKDAY_EN[d.weekday()]}" if d else "— 미정"


def fmt_kor(iso):
    """2026-11-13 → '11/13 (금)'"""
    d = parse_iso(iso)
    return f"{d.month}/{d.day} ({WEEKDAY_KO[d.weekday()]})" if d else "미정"


def fmt_long_kor(iso):
    """2026-11-13 → '11월 13일 금요일'"""
    d = parse_iso(iso)
    return f"{d.month}월 {d.day}일 {WEEKDAY_KO[d.weekday()]}요일" if d else "미정"


def fmt_header_date(d):
    """2026.11.04 WED"""
    return f"{d.year}.{d.month:02d}.{d.day:02d} {WEEKDAY_EN[d.weekday()]}"


def trim_history(messages, max_turns=MAX_TURNS):
    """사용자 발화 기준으로 최근 max_turns 턴만 남긴다"""
    user_idx = [i for i, m in enumerate(messages) if m["role"] == "user"]
    if len(user_idx) <= max_turns:
        return messages
    return messages[user_idx[-max_turns]:]


def count_turns(messages):
    return sum(1 for m in messages if m["role"] == "user")


def decode_text(raw):
    """업로드 파일 디코딩 (utf-8 → cp949)"""
    for enc in ("utf-8-sig", "cp949"):
        try:
            return raw.decode(enc)
        except Exception:
            pass
    return raw.decode("utf-8", errors="ignore")


def strip_for_speech(text):
    """TTS 용으로 마크다운 기호 제거"""
    for ch in ["*", "#", "`", "_"]:
        text = text.replace(ch, "")
    for ch in [">", "- "]:
        text = text.replace(ch, " ")
    return " ".join(text.split())[:600]


# ---- 이메일 (교안 send_email 과 동일) ----
def send_email(to, subject, body):
    sender = GMAIL_ADDRESS
    password = GMAIL_APP_PASSWORD
    if not (sender and password):
        return {"status": "failed", "error": "GMAIL_ADDRESS / GMAIL_APP_PASSWORD 가 설정되지 않았습니다."}

    # 메일 구성 (본문, 제목, 발신자, 수신자)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to

    # 메일 보내기 (with 구문: 오류가 나도 연결이 닫힘)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
            s.starttls()
            s.login(sender, password)
            s.sendmail(sender, to, msg.as_string())
        return {"status": "success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}


# ---- 구글 캘린더 ----
def normalize_event(e):
    """구글 이벤트 → 앱에서 쓰는 단순 dict. 에이블이 만든 일정은 source=able"""
    start = e.get("start") or {}
    day = start.get("date") or (start.get("dateTime") or "")[:10]
    private = (e.get("extendedProperties") or {}).get("private") or {}
    return {
        "id": e.get("id"),
        "title": e.get("summary") or "(제목 없음)",
        "date": day,
        "is_able": private.get("source") == "able",
        "task_id": private.get("task_id"),
    }


@st.cache_data(ttl=60, show_spinner=False)
def fetch_events_cached(_service, calendar_id, start_iso, end_iso):
    """기간 내 일정 조회 (60초 캐시). _service 는 해시 대상에서 제외"""
    end_next = (parse_iso(end_iso) + timedelta(days=1)).isoformat()
    result = _service.events().list(
        calendarId=calendar_id,
        timeMin=f"{start_iso}T00:00:00+09:00",
        timeMax=f"{end_next}T00:00:00+09:00",
        singleEvents=True,
        orderBy="startTime",
        maxResults=250,
        timeZone="Asia/Seoul",
    ).execute()
    return [normalize_event(e) for e in result.get("items", [])]


def get_events(start_iso, end_iso):
    """(일정 목록, 오류 문구). 캘린더 미연결이면 앱 안 일정으로 대체"""
    if not CAL_OK:
        local = [e for e in st.session_state.local_events if start_iso <= e["date"] <= end_iso]
        return local, CAL_SETUP_ERROR
    try:
        return fetch_events_cached(calendar_service, GOOGLE_CALENDAR_ID, start_iso, end_iso), None
    except Exception as e:
        return [], f"구글 캘린더 조회 실패: {e}"


def insert_event(title, date_iso, description, task_id=None):
    """종일 일정 등록. 에이블 표식(extendedProperties.private.source=able) 포함"""
    d = parse_iso(date_iso)
    body = {
        "summary": title,
        "description": description or "",
        "start": {"date": d.isoformat()},
        "end": {"date": (d + timedelta(days=1)).isoformat()},   # 종일 일정의 end 는 다음 날(배타)
        "extendedProperties": {"private": {"source": "able", "task_id": task_id or ""}},
    }
    created = calendar_service.events().insert(calendarId=GOOGLE_CALENDAR_ID, body=body).execute()
    fetch_events_cached.clear()
    return created["id"]


def find_existing_event(title, date_iso, events):
    """같은 제목 + 같은 날짜 일정이 이미 있으면 반환 (중복 등록 방지)"""
    key = (title or "").strip()
    for ev in events:
        if ev["date"] == date_iso and (ev["title"] or "").strip() == key:
            return ev
    return None


def events_by_date(events):
    grouped = {}
    for ev in events:
        grouped.setdefault(ev["date"], []).append(ev)
    return grouped


def month_range(year, month):
    last_day = cal_lib.monthrange(year, month)[1]
    return date(year, month, 1).isoformat(), date(year, month, last_day).isoformat()


def shift_month(year, month, delta):
    m = month + delta
    y = year + (m - 1) // 12
    m = (m - 1) % 12 + 1
    return y, m


def month_grid_html(year, month, grouped, today_iso, max_chips=3):
    """월간 그리드 HTML (월요일 시작). 에이블 일정 = 채움, 그 외 = 테두리"""
    parts = ['<div class="able-grid">']
    for name in WEEKDAY_EN:
        parts.append(f'<span class="able-grid-head">{name}</span>')
    for week in cal_lib.Calendar(firstweekday=0).monthdayscalendar(year, month):
        for day in week:
            if day == 0:
                parts.append('<div class="able-cell"></div>')
                continue
            iso = f"{year:04d}-{month:02d}-{day:02d}"
            is_today = iso == today_iso
            cls = "able-cell able-cell-today" if is_today else "able-cell"
            num = f"{day} — today" if is_today else str(day)
            chips = []
            evs = grouped.get(iso, [])
            for ev in evs[:max_chips]:
                chip_cls = "able-chip able-chip-fill" if ev.get("is_able") else "able-chip able-chip-line"
                chips.append(f'<span class="{chip_cls}" title="{html.escape(str(ev["title"]))}">{html.escape(str(ev["title"]))}</span>')
            if len(evs) > max_chips:
                chips.append(f'<span class="able-more">+{len(evs) - max_chips}</span>')
            parts.append(f'<div class="{cls}"><span class="able-daynum">{num}</span>{"".join(chips)}</div>')
    parts.append("</div>")
    return "".join(parts)


# ---- 업무 / 확인 대기 작업 ----
def find_task(task_id):
    for t in st.session_state.tasks:
        if t["id"] == task_id:
            return t
    return None


def match_task_by_title(title):
    """모델이 만든 일정 제목과 업무 제목이 겹치면 그 업무로 연결"""
    key = (title or "").replace(" ", "")
    for t in st.session_state.tasks:
        tk = t["title"].replace(" ", "")
        if tk and (tk in key or key in tk):
            return t
    return None


def new_message(role, content, via="text", tools=None):
    return {"id": uuid.uuid4().hex[:8], "role": role, "content": content, "via": via, "tools": tools or []}


def find_message(msg_id):
    for m in st.session_state.messages:
        if m["id"] == msg_id:
            return m
    return None


def queue_pending(tool_name, args, task_id=None, msg_id=None):
    """send_email / add_calendar_event 는 바로 실행하지 않고 확인 대기열에 넣는다"""
    args = dict(args or {})
    if tool_name == "send_email":
        to = (args.get("to") or "").strip()
        if "@" not in to:                      # 수신자를 모르면 기본 수신자
            args["to"] = MY_EMAIL
        kind = "email"
    else:
        kind = "calendar"
        if not task_id:
            matched = match_task_by_title(args.get("title"))
            task_id = matched["id"] if matched else None
    action = {"id": uuid.uuid4().hex[:8], "type": kind, "tool": tool_name, "args": args,
              "task_id": task_id, "msg_id": msg_id}
    st.session_state.pending_actions.append(action)
    return action


def remove_pending(action_id):
    st.session_state.pending_actions = [a for a in st.session_state.pending_actions if a["id"] != action_id]


def update_tool_status(action, status):
    """'— send_email  waiting for you' 줄을 done / cancelled 로 바꾼다"""
    m = find_message(action.get("msg_id")) if action.get("msg_id") else None
    if not m:
        return
    m["tools"] = [f"{action['tool']}  {status}" if line.startswith(f"{action['tool']}  waiting") else line
                  for line in m["tools"]]


def append_assistant(content, tools=None, speak_it=True):
    st.session_state.messages.append(new_message("assistant", content, tools=tools))
    st.session_state.messages = trim_history(st.session_state.messages)
    if speak_it:
        speak(content)


# =========================================================
# 4) LLM
# =========================================================
# ---- (a) 회의록 분석: JSON 스키마 구조화 출력 ----
BRIEF_SCHEMA = {
    "type": "object",
    "properties": {
        "meeting_title": {"type": "string", "description": "회의 주제 (20자 이내)"},
        "participants": {"type": "array", "items": {"type": "string"}, "description": "발언한 참석자"},
        "summary": {"type": "string", "description": "김 대리가 알아야 할 결정 사항 중심 2~3문장 요약"},
        "key_facts": {"type": "array", "items": {"type": "string"}, "description": "핵심 사실 4~6개, 각 20자 이내"},
        "tasks": {
            "type": "array",
            "description": "김 대리에게 배정된 업무만",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "업무 이름 (15자 이내)"},
                    "detail": {"type": "string", "description": "세부 요구사항 한 줄 (40자 이내)"},
                    "requester": {"type": "string", "description": "업무를 지시한 사람 (예: 팀장)"},
                    "due": {"type": ["string", "null"], "description": "회의에서 언급된 마감을 회의 날짜 기준 YYYY-MM-DD 로 환산. 언급 없으면 null"},
                    "due_text": {"type": ["string", "null"], "description": "마감 원문 표현 (예: 다음 주까지). 없으면 null"},
                    "suggested_due": {"type": ["string", "null"], "description": "due 가 null 일 때만, 회의 맥락을 근거로 제안하는 YYYY-MM-DD. due 가 있으면 null"},
                    "suggest_reason": {"type": ["string", "null"], "description": "제안 이유 한 줄 (25자 이내). due 가 있으면 null"},
                },
                "required": ["title", "detail", "requester", "due", "due_text", "suggested_due", "suggest_reason"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["meeting_title", "participants", "summary", "key_facts", "tasks"],
    "additionalProperties": False,
}


def extract_briefing(meeting_text, meeting_date):
    """회의록 → (브리핑 dict, 업무 list). LLM 한 번 호출"""
    wd = WEEKDAY_KO[meeting_date.weekday()]
    system = f"""당신은 회의록을 분석하는 비서 '에이블'입니다. 회의록에서 {USER_NAME}에게 필요한 정보를 JSON 으로 추출합니다.
회의 날짜: {meeting_date.isoformat()} ({wd}요일)
규칙:
- tasks 에는 {USER_NAME}(김대리)에게 배정된 업무만 넣습니다. 다른 사람 업무는 제외합니다.
- 상대 날짜 환산: "다음 주까지" → 다음 주 금요일, "이번 주까지" → 이번 주 금요일, "다음 달 초" → 다음 달 5일, "N일 후" → 회의 날짜 + N일. 결과가 주말이면 직전 금요일로.
- 마감이 언급되지 않은 업무는 due 를 null 로 두고, 회의 맥락(출시 시점, 다른 업무와의 선후 관계, 다음 회의 등)을 근거로 suggested_due 와 한 줄 이유를 제안합니다. 제안 날짜는 회의 날짜 이후 평일이어야 합니다.
- summary 는 {USER_NAME} 관점에서 알아야 할 결정 사항 중심으로 씁니다."""
    response = client.responses.create(
        model=LLM_MODEL,
        input=[{"role": "system", "content": system},
               {"role": "user", "content": f"[회의록]\n{meeting_text}"}],
        text={"format": {"type": "json_schema", "name": "meeting_brief", "schema": BRIEF_SCHEMA, "strict": True}},
    )
    data = json.loads(response.output_text)

    # 날짜 검증 + 기본값 보정
    tasks = []
    for i, t in enumerate(data.get("tasks", [])):
        due = parse_iso(t.get("due"))
        suggested = parse_iso(t.get("suggested_due")) if due is None else None
        reason = (t.get("suggest_reason") or "").strip() if due is None else None
        if due is None and suggested is None:
            suggested = meeting_date + timedelta(days=7)
            reason = "회의 후 1주 (기본 제안)"
        tasks.append({
            "id": f"t{i + 1}",
            "title": (t.get("title") or "").strip() or f"업무 {i + 1}",
            "detail": (t.get("detail") or "").strip(),
            "requester": (t.get("requester") or "").strip() or "미상",
            "due": due.isoformat() if due else None,
            "due_text": t.get("due_text"),
            "suggested_due": suggested.isoformat() if suggested else None,
            "suggest_reason": reason or "",
            "event_id": None,
        })
    briefing = {
        "title": data.get("meeting_title") or "회의",
        "participants": data.get("participants") or [],
        "summary": data.get("summary") or "",
        "facts": data.get("key_facts") or [],
    }
    return briefing, tasks


# ---- (b) 대화용 도구 정의 (Responses API function tools, 교안과 같은 형식) ----
TOOLS = [
    {
        "type": "function",
        "name": "send_email",
        "description": f"이메일을 발송합니다. {USER_NAME}가 '메일로 보내줘'처럼 명시적으로 요청할 때만 사용합니다. 실제 발송은 사용자 확인 후 이루어집니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "이메일 수신자. 예: 'test@gmail.com'. 수신자를 모르면 기본 수신자 주소를 넣습니다."},
                "subject": {"type": "string", "description": "이메일 제목. 예: '[회의 요약] 신제품 출시 마케팅 전략'"},
                "body": {"type": "string", "description": "이메일 본문. 인사말, 핵심 요약, 업무 목록(마감 포함), 마무리로 구성한 완성된 한국어 메일"},
            },
            "required": ["to", "subject", "body"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "add_calendar_event",
        "description": "업무 마감 등 일정을 에이블 캘린더에 종일 일정으로 등록합니다. 업무 하나당 한 번 호출합니다. 실제 등록은 사용자 확인 후 이루어집니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "일정 제목. 예: '경쟁사 마케팅 분석 보고서 마감'"},
                "date": {"type": "string", "description": "날짜 YYYY-MM-DD"},
                "description": {"type": "string", "description": "일정 설명 (업무 세부 내용, 요청자)"},
            },
            "required": ["title", "date", "description"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "list_events",
        "description": "기간 내 캘린더 일정을 조회합니다. 일정 관련 질문에 답하기 전에 호출합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "조회 시작일 YYYY-MM-DD"},
                "end_date": {"type": "string", "description": "조회 종료일 YYYY-MM-DD (포함)"},
            },
            "required": ["start_date", "end_date"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def tool_list_events(start_date, end_date):
    """list_events 도구 실행: 결과를 모델에 다시 전달"""
    s, e = parse_iso(start_date), parse_iso(end_date)
    if not (s and e):
        return {"status": "failed", "error": "날짜 형식은 YYYY-MM-DD 여야 합니다."}
    if e < s:
        s, e = e, s
    events, err = get_events(s.isoformat(), e.isoformat())
    items = [{"date": ev["date"], "weekday": WEEKDAY_KO[parse_iso(ev["date"]).weekday()] if parse_iso(ev["date"]) else "",
              "title": ev["title"], "created_by_able": ev.get("is_able", False)} for ev in events]
    result = {"status": "success", "start_date": s.isoformat(), "end_date": e.isoformat(), "count": len(items), "events": items}
    if not CAL_OK:
        result["note"] = "구글 캘린더가 연결되지 않아 앱 안에 기록된 일정만 조회했습니다."
    elif err:
        result = {"status": "failed", "error": err}
    return result


def build_system_prompt():
    tasks_brief = [{k: t.get(k) for k in ("id", "title", "detail", "requester", "due", "suggested_due", "suggest_reason", "event_id")}
                   for t in st.session_state.tasks]
    meeting = st.session_state.meeting_text
    lines = [
        f"당신은 '에이블'입니다. 마케팅팀 {USER_NAME}의 개인 비서로, {USER_NAME}가 놓친 회의 내용을 정리하고 업무·일정·메일을 대신 처리합니다.",
        "말투: 간결한 한국어 존댓말. 답변은 2~4문장. 음성으로 읽히므로 마크다운, 이모지, 특수기호 없이 자연스러운 문장으로 말합니다. 여러 항목은 '첫째, 둘째'처럼 이어 말합니다.",
        f"오늘: {today.isoformat()} ({WEEKDAY_KO[today.weekday()]}요일). '이번 주'는 오늘이 속한 월요일부터 일요일, '다음 주'는 그 다음 주입니다.",
        "회의록이 있으면 반드시 회의록 내용에 근거해 답하고, 회의록에 없는 내용은 추측하지 말고 없다고 말합니다. 회의록이 없으면 먼저 회의록(.txt)을 올려 달라고 안내합니다.",
        "도구 사용 규칙:",
        f"- send_email: 사용자가 '메일로 보내줘', '이메일로 정리해줘'처럼 명시적으로 요청할 때만 호출합니다. 요약만 원하면 호출하지 않습니다. 수신자를 말하지 않으면 to 에 '{MY_EMAIL or 'me'}' 를 넣습니다.",
        "- add_calendar_event: 업무나 마감을 캘린더에 넣어 달라고 할 때 호출합니다. 업무마다 한 번씩 호출하고, due 가 없는 업무는 suggested_due 를 쓰며 그 사실을 답변에서 알립니다. event_id 가 이미 있는 업무는 다시 등록하지 않습니다.",
        "- list_events: 일정을 물으면 먼저 호출하고, 그 결과에 있는 일정만 말합니다.",
        "- 도구 결과가 pending_confirmation 이면 '초안(또는 등록 내용)을 준비했으니 화면의 확인 카드에서 보내기/등록 버튼을 눌러 주세요'라고 짧게 안내합니다. 실제로 보냈다거나 등록했다고 말하지 마세요.",
        "",
        f"[회의 정보] 회의 날짜: {st.session_state.meeting_date} / 파일: {st.session_state.meeting_name or '없음'}",
        f"[{USER_NAME}의 업무 목록 JSON]\n{json.dumps(tasks_brief, ensure_ascii=False)}",
        f"[회의록 원문]\n{meeting if meeting else '(아직 업로드되지 않았습니다)'}",
    ]
    return "\n".join(lines)


def run_able(assistant_msg_id):
    """대화 1턴 처리. list_events 는 바로 실행해 결과를 모델에 돌려주고,
    send_email / add_calendar_event 는 확인 대기열에 넣는다. (답변, 도구 상태 줄) 반환"""
    input_items = [{"role": "system", "content": build_system_prompt()}]
    input_items += [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    statuses = []
    tool_choice = "auto"
    response = None

    for _ in range(3):                                   # 도구 호출 → 결과 전달 → 최종 답변 (최대 3회 반복)
        response = client.responses.create(model=LLM_MODEL, input=input_items, tools=TOOLS, tool_choice=tool_choice)
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            break

        input_items += response.output                   # 모델의 도구 호출 항목을 그대로 되돌려 준다
        made_pending = False
        for call in calls:
            try:
                args = json.loads(call.arguments or "{}")
            except Exception:
                args = {}

            if call.name == "list_events":
                result = tool_list_events(args.get("start_date", ""), args.get("end_date", ""))
                statuses.append("list_events  done")
            elif call.name in ("send_email", "add_calendar_event"):
                task = match_task_by_title(args.get("title")) if call.name == "add_calendar_event" else None
                if task and task.get("event_id"):
                    result = {"status": "skipped", "reason": "이미 캘린더에 등록된 업무입니다."}
                    statuses.append("add_calendar_event  skipped (already registered)")
                else:
                    queue_pending(call.name, args, task_id=task["id"] if task else None, msg_id=assistant_msg_id)
                    result = {"status": "pending_confirmation",
                              "message": "사용자 확인 대기 중입니다. 화면의 확인 카드에서 버튼을 누르면 실행됩니다. 같은 도구를 다시 호출하지 마세요."}
                    statuses.append(f"{call.name}  waiting for you")
                    made_pending = True
            else:
                result = {"status": "failed", "error": f"알 수 없는 도구 {call.name}"}

            input_items.append({"type": "function_call_output", "call_id": call.call_id,
                                "output": json.dumps(result, ensure_ascii=False)})
        if made_pending:
            tool_choice = "none"                         # 확인 대기 중이면 더 호출하지 말고 답변만

    answer = (response.output_text or "").strip() if response else ""
    if not answer:
        answer = "요청을 처리했어요. 화면의 확인 카드를 확인해 주세요." if st.session_state.pending_actions else "죄송해요, 답변을 만들지 못했어요. 다시 말씀해 주세요."
    return answer, statuses


# ---- (c) STT / TTS ----
def transcribe(audio_bytes):
    """음성 → 텍스트 (whisper-1)"""
    transcript = client.audio.transcriptions.create(
        model=STT_MODEL, file=("audio.wav", audio_bytes, "audio/wav"), language="ko")
    return transcript.text.strip()


def speak(text):
    """텍스트 → 음성(bytes). 최신 답변만 자동 재생"""
    st.session_state.tts_audio = None
    st.session_state.tts_autoplay = False
    if not client or not text:
        return
    speech_text = strip_for_speech(text)
    for model in (TTS_MODEL, "tts-1"):
        try:
            speech = client.audio.speech.create(model=model, voice=TTS_VOICE, input=speech_text)
            st.session_state.tts_audio = speech.content
            st.session_state.tts_autoplay = True
            return
        except Exception as e:
            err = e
    set_notice("warning", f"음성 생성에 실패했어요: {err}")


# ---- (d) 사용자 메시지 1건 처리 ----
def handle_user_message(text, via, box):
    """사용자 발화 추가 → 에이블 답변 → 음성 → rerun"""
    text = (text or "").strip()
    if not text:
        return
    user_msg = new_message("user", text, via=via)
    st.session_state.messages.append(user_msg)
    assistant_id = uuid.uuid4().hex[:8]

    with box:
        render_message(user_msg)
        if client is None:
            answer, statuses = "OPENAI_API_KEY 가 설정되지 않아 답변할 수 없어요. Secrets 를 확인해 주세요.", []
        else:
            with st.spinner("에이블이 생각하고 있어요..."):
                try:
                    answer, statuses = run_able(assistant_id)
                except Exception as e:
                    answer, statuses = f"죄송해요, 답변 중 오류가 났어요. ({e})", []
    msg = new_message("assistant", answer, tools=statuses)
    msg["id"] = assistant_id
    st.session_state.messages.append(msg)
    st.session_state.messages = trim_history(st.session_state.messages)
    speak(answer)
    st.rerun()


# ---- (e) 확인 카드 실행 ----
def execute_email(action, to, subject, body):
    to = (to or "").strip()
    if "@" not in to:
        set_notice("error", "수신자 이메일 주소를 확인해 주세요.")
        return
    with st.spinner("메일을 보내고 있어요..."):
        result = send_email(to, subject.strip(), body)
    if result.get("status") == "success":
        remove_pending(action["id"])
        update_tool_status(action, "done")
        append_assistant(f"{to} 로 메일을 보냈어요. 제목은 '{subject.strip()}' 입니다.", tools=["send_email  done"])
        st.toast("메일을 보냈어요.")
    else:
        set_notice("error", f"메일 발송에 실패했어요: {result.get('error')}")


def execute_calendar(action, title, date_iso, description):
    title = (title or "").strip()
    if not title or not parse_iso(date_iso):
        set_notice("error", "일정 제목과 날짜를 확인해 주세요.")
        return
    task = find_task(action.get("task_id")) or match_task_by_title(title)

    # 중복 방지 1: 이미 등록된 업무
    if task and task.get("event_id"):
        remove_pending(action["id"])
        update_tool_status(action, "skipped")
        set_notice("info", f"'{task['title']}' 은(는) 이미 캘린더에 등록돼 있어요.")
        return

    # 중복 방지 2: 같은 제목 + 같은 날짜 일정이 캘린더에 있음
    events, _ = get_events(date_iso, date_iso)
    existing = find_existing_event(title, date_iso, events)
    if existing:
        event_id = existing["id"]
        answer = f"{fmt_long_kor(date_iso)}에 '{title}' 일정이 이미 있어서 그대로 두었어요."
    else:
        try:
            if CAL_OK:
                with st.spinner("캘린더에 등록하고 있어요..."):
                    event_id = insert_event(title, date_iso, description, task["id"] if task else None)
                answer = f"{fmt_long_kor(date_iso)}에 '{title}' 을(를) 캘린더에 등록했어요."
            else:
                event_id = "local-" + uuid.uuid4().hex[:8]
                st.session_state.local_events.append({"id": event_id, "title": title, "date": date_iso, "is_able": True,
                                                      "task_id": task["id"] if task else None})
                answer = f"{fmt_long_kor(date_iso)}에 '{title}' 을(를) 앱 안 캘린더에 기록했어요. 구글 캘린더는 연결되지 않았어요."
        except Exception as e:
            set_notice("error", f"캘린더 등록에 실패했어요: {e}")
            return

    if task:
        task["due"] = date_iso
        task["event_id"] = event_id
    remove_pending(action["id"])
    update_tool_status(action, "done")
    append_assistant(answer, tools=["add_calendar_event  done"])
    st.toast("캘린더에 등록했어요.")


def cancel_action(action):
    remove_pending(action["id"])
    update_tool_status(action, "cancelled")
    st.session_state.tts_autoplay = False


# =========================================================
# 5) 화면
# =========================================================
def render_message(m):
    """대화 말풍선 (HTML). YOU — 음성 인식 / ABLE"""
    if m["role"] == "user":
        label = "YOU — 음성 인식" if m.get("via") == "voice" else "YOU"
        st.markdown(f'<span class="able-label">{label}</span><p class="able-you">{esc(m["content"])}</p>', unsafe_allow_html=True)
    else:
        tools_html = "".join(f'<span class="able-tool">— {esc(line)}</span>' for line in m.get("tools", []))
        st.markdown(f'<span class="able-label">ABLE</span><p class="able-answer">{esc(m["content"])}</p>{tools_html}<div class="able-gap"></div>',
                    unsafe_allow_html=True)


incoming = None          # 이번 rerun 에 처리할 사용자 발화 (텍스트)
incoming_via = "text"

# 이번 달 일정 (헤더 상태 표시에도 쓰므로 먼저 조회)
cal_y, cal_m = st.session_state.cal_year, st.session_state.cal_month
m_start, m_end = month_range(cal_y, cal_m)
month_events, cal_fetch_error = get_events(m_start, m_end)
calendar_connected = CAL_OK and not cal_fetch_error

# ---- 헤더 ----
meta = [
    f"{USER_NAME} 전용 AI 비서",
    fmt_header_date(today),
    "openai — " + ("connected" if client else "not connected"),
    "google calendar — " + ("connected" if calendar_connected else "not connected"),
    "gmail — " + ("connected" if GMAIL_OK else "not connected"),
]
st.markdown(
    '<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px;">'
    '<h1 class="able-wordmark">able.</h1>'
    f'<div class="able-meta">{"<br>".join(meta)}</div></div>'
    '<div class="able-tagline"><span>회의록을 읽고, 내 업무를 찾고, 일정과 메일로 정리합니다.</span>'
    f'<span class="able-muted">source — {esc(st.session_state.meeting_name or "회의록 없음")}</span></div>',
    unsafe_allow_html=True,
)

left, right = st.columns([3, 2], gap="large")

# =========================
# 왼쪽: 01 브리핑 / 02 내 업무 / 03 캘린더
# =========================
with left:
    # ---- 01 브리핑 ----
    st.markdown('<div class="able-section">01 — 브리핑</div>', unsafe_allow_html=True)
    u1, u2 = st.columns([3, 1.3], vertical_alignment="bottom")
    uploaded = u1.file_uploader("회의록 (.txt)", type=["txt"], label_visibility="collapsed")
    meeting_date_input = u2.date_input("회의 날짜", value=parse_iso(st.session_state.meeting_date) or today, format="YYYY-MM-DD")

    # 새 파일 또는 새 날짜가 들어왔을 때만 다시 분석
    if uploaded is not None:
        raw = uploaded.getvalue()
        key = (uploaded.name, hashlib.md5(raw).hexdigest(), meeting_date_input.isoformat())
        if key != st.session_state.briefing_key:
            st.session_state.briefing_key = key
            st.session_state.meeting_text = decode_text(raw)
            st.session_state.meeting_name = uploaded.name
            st.session_state.meeting_date = meeting_date_input.isoformat()
            st.session_state.picking_task = None
            if client is None:
                set_notice("error", "OPENAI_API_KEY 가 없어 회의록을 분석할 수 없어요. 회의록 원문은 기억해 둘게요.")
            else:
                try:
                    with st.spinner("회의록을 읽고 김 대리님 업무를 찾고 있어요..."):
                        briefing, tasks = extract_briefing(st.session_state.meeting_text, meeting_date_input)
                    st.session_state.briefing, st.session_state.tasks = briefing, tasks
                    st.toast(f"회의록 분석 완료 — 업무 {len(tasks)}건")
                except Exception as e:
                    set_notice("error", f"회의록 분석에 실패했어요: {e}")

    b = st.session_state.briefing
    if b:
        n = len(st.session_state.tasks)
        lead = f"놓친 회의 「{b['title']}」에서 {USER_NAME}님께 업무 {n}건이 배정됐습니다."
        facts = " · ".join(esc(f) for f in b["facts"])
        st.markdown(f'<p class="able-lead">{esc(lead)}</p><p class="able-sub">{esc(b["summary"])}</p>'
                    f'<p class="able-sub">{facts}</p>', unsafe_allow_html=True)
        a1, a2, _ = st.columns([1.2, 1.2, 3])
        if a1.button("브리핑 듣기 →", key="btn_brief_tts"):
            if client is None:
                set_notice("error", "OPENAI_API_KEY 가 없어 음성을 만들 수 없어요.")
            else:
                try:
                    speech = client.audio.speech.create(model=TTS_MODEL, voice=TTS_VOICE, input=strip_for_speech(lead + " " + b["summary"]))
                    st.session_state.brief_audio, st.session_state.brief_autoplay = speech.content, True
                except Exception as e:
                    set_notice("error", f"브리핑 음성 생성 실패: {e}")
        if a2.button("메일로 받기 →", key="btn_brief_mail"):
            incoming = "회의 요약과 내 업무를 정리해서 내 메일로 보내줘"
        if st.session_state.brief_audio:
            st.audio(st.session_state.brief_audio, format="audio/mp3", autoplay=st.session_state.brief_autoplay)
            st.session_state.brief_autoplay = False
    elif st.session_state.meeting_text:
        st.markdown('<p class="able-hint">회의록은 기억하고 있지만 분석 결과가 없어요.</p>', unsafe_allow_html=True)
        if st.button("다시 분석", key="btn_reanalyze") and client is not None:
            try:
                with st.spinner("회의록을 다시 읽고 있어요..."):
                    briefing, tasks = extract_briefing(st.session_state.meeting_text, parse_iso(st.session_state.meeting_date) or today)
                st.session_state.briefing, st.session_state.tasks = briefing, tasks
                st.rerun()
            except Exception as e:
                set_notice("error", f"회의록 분석에 실패했어요: {e}")
    else:
        st.markdown('<p class="able-hint">회의록(.txt)을 올리고 회의 날짜를 고르면, 요약과 김 대리님의 업무를 바로 찾아 드려요.</p>',
                    unsafe_allow_html=True)

    # ---- 02 내 업무 ----
    st.markdown('<div class="able-section">02 — 내 업무</div>', unsafe_allow_html=True)
    tasks = st.session_state.tasks
    if not tasks:
        st.markdown('<p class="able-hint">회의록을 올리면 김 대리님께 배정된 업무가 여기에 정리됩니다.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="able-rule-dark"></div>', unsafe_allow_html=True)
        for i, t in enumerate(tasks):
            c1, c2, c3, c4 = st.columns([0.5, 4.3, 1.4, 2.2], vertical_alignment="center")
            c1.markdown(f'<span class="able-no">{i + 1:02d}</span>', unsafe_allow_html=True)
            detail = esc(t["detail"]) + (f' · 요청 {esc(t["requester"])}' if t.get("requester") else "")
            c2.markdown(f'<span class="able-task-title">{esc(t["title"])}</span><span class="able-task-detail">{detail}</span>',
                        unsafe_allow_html=True)
            if t["due"]:
                c3.markdown(f'<span class="able-due">{fmt_due(t["due"])}</span>', unsafe_allow_html=True)
            else:
                c3.markdown('<span class="able-due able-muted">— 미정</span>', unsafe_allow_html=True)

            with c4:
                if t.get("event_id"):
                    st.markdown('<span class="able-registered"><i></i>캘린더 등록됨</span>', unsafe_allow_html=True)
                elif t["due"]:
                    if st.button("캘린더에 추가", key=f"btn_add_{t['id']}"):
                        queue_pending("add_calendar_event",
                                      {"title": t["title"], "date": t["due"],
                                       "description": f"{t['detail']}\n요청: {t['requester']}\n출처: {st.session_state.meeting_name or '회의록'}"},
                                      task_id=t["id"])
                        st.rerun()
                else:
                    label = "닫기" if st.session_state.picking_task == t["id"] else "날짜 정하기 +"
                    if st.button(label, key=f"btn_pick_{t['id']}"):
                        st.session_state.picking_task = None if st.session_state.picking_task == t["id"] else t["id"]
                        st.rerun()

            # 마감 미정 업무: 에이블 제안 / 직접 지정
            if st.session_state.picking_task == t["id"] and not t["due"]:
                sd = t.get("suggested_due") or (today + timedelta(days=7)).isoformat()
                options = [f"에이블 제안: {fmt_kor(sd)} — {t.get('suggest_reason') or '회의 후 1주'}", "직접 지정"]
                choice = st.radio("마감일", options, key=f"radio_{t['id']}", label_visibility="collapsed")
                chosen = sd
                if choice == "직접 지정":
                    picked = st.date_input("날짜", value=parse_iso(sd) or today, key=f"date_{t['id']}", format="YYYY-MM-DD")
                    chosen = picked.isoformat()
                if st.button(f"{fmt_kor(chosen)} 로 캘린더에 추가", key=f"btn_pickok_{t['id']}"):
                    queue_pending("add_calendar_event",
                                  {"title": t["title"], "date": chosen,
                                   "description": f"{t['detail']}\n요청: {t['requester']}\n출처: {st.session_state.meeting_name or '회의록'}"},
                                  task_id=t["id"])
                    st.session_state.picking_task = None
                    st.rerun()
            st.markdown('<div class="able-rule"></div>', unsafe_allow_html=True)

    # ---- 03 캘린더 ----
    st.markdown('<div class="able-section">03 — 캘린더</div>', unsafe_allow_html=True)
    n1, n2, n3, n4, n5 = st.columns([0.5, 0.5, 2.6, 1.1, 2.3], vertical_alignment="center")
    if n1.button("‹", key="btn_prev"):
        st.session_state.cal_year, st.session_state.cal_month = shift_month(cal_y, cal_m, -1)
        st.rerun()
    if n2.button("›", key="btn_next"):
        st.session_state.cal_year, st.session_state.cal_month = shift_month(cal_y, cal_m, 1)
        st.rerun()
    n3.markdown(f'<span class="able-month">{cal_lib.month_name[cal_m]} {cal_y}</span>', unsafe_allow_html=True)
    if n4.button("새로고침", key="btn_refresh"):
        fetch_events_cached.clear()
        st.rerun()
    n5.markdown('<div class="able-legend"><span><i style="border:1px solid #1C1C1C;"></i>구글 캘린더</span>'
                '<span><i style="background:#1C1C1C;"></i>에이블 등록</span></div>', unsafe_allow_html=True)

    st.markdown(month_grid_html(cal_y, cal_m, events_by_date(month_events), today.isoformat()), unsafe_allow_html=True)
    if not CAL_OK:
        st.markdown(f'<p class="able-hint">구글 캘린더가 연결되지 않아 앱 안에 기록한 일정만 보여요. ({esc(CAL_SETUP_ERROR)})</p>',
                    unsafe_allow_html=True)
    elif cal_fetch_error:
        st.markdown(f'<p class="able-hint">{esc(cal_fetch_error)}</p>', unsafe_allow_html=True)

# =========================
# 오른쪽: 대화 패널
# =========================
with right:
    with st.container(key="able_strip"):
        status = "speaking" if st.session_state.tts_autoplay else "ready"
        st.markdown(f'<span class="able-mark-sm">able.</span><span class="able-status"><i></i>{status}</span>',
                    unsafe_allow_html=True)

    with st.container(key="able_chat"):
        # 안내/오류 (한 번만)
        if st.session_state.notice:
            kind, text = st.session_state.notice
            st.session_state.notice = None
            {"error": st.error, "warning": st.warning, "info": st.info}.get(kind, st.info)(text)

        # 대화 기록
        messages_box = st.container()
        with messages_box:
            if not st.session_state.messages:
                st.markdown('<span class="able-label">ABLE</span><p class="able-answer">안녕하세요, 에이블이에요. 회의록을 올려 주시면 요약하고 업무를 정리해 드릴게요. '
                            '마이크나 메시지로 말을 걸어 주세요.</p>', unsafe_allow_html=True)
            for idx, m in enumerate(st.session_state.messages):
                render_message(m)
                # 최신 답변에만 음성 플레이어 (처음 한 번만 자동 재생)
                if m["role"] == "assistant" and idx == len(st.session_state.messages) - 1 and st.session_state.tts_audio:
                    st.audio(st.session_state.tts_audio, format="audio/mp3", autoplay=st.session_state.tts_autoplay)
                    st.session_state.tts_autoplay = False

        # 확인 대기 카드 (맨 앞 1건)
        if st.session_state.pending_actions:
            action = st.session_state.pending_actions[0]
            args = action["args"]
            aid = action["id"]
            total = len(st.session_state.pending_actions)
            counter = f" · 대기 1 / {total}" if total > 1 else ""
            with st.container(key="able_card"):
                if action["type"] == "email":
                    st.markdown(f'<span class="able-label">MAIL — 보내기 전에 확인{counter}</span>', unsafe_allow_html=True)
                    to = st.text_input("TO", value=args.get("to") or MY_EMAIL, key=f"w_to_{aid}")
                    subject = st.text_input("RE", value=args.get("subject", ""), key=f"w_re_{aid}")
                    body = st.text_area("BODY", value=args.get("body", ""), height=180, key=f"w_body_{aid}")
                    k1, k2 = st.columns([1, 2])
                    if k1.button("취소", key=f"w_cancel_{aid}"):
                        cancel_action(action)
                        st.rerun()
                    if k2.button("보내기", key=f"w_send_{aid}", type="primary"):
                        execute_email(action, to, subject, body)
                        st.rerun()
                else:
                    st.markdown(f'<span class="able-label">CALENDAR — 등록 전에 확인{counter}</span>', unsafe_allow_html=True)
                    title = st.text_input("TITLE", value=args.get("title", ""), key=f"w_title_{aid}")
                    d = st.date_input("DATE", value=parse_iso(args.get("date")) or today, key=f"w_date_{aid}", format="YYYY-MM-DD")
                    desc = st.text_area("NOTE", value=args.get("description", ""), height=100, key=f"w_desc_{aid}")
                    k1, k2 = st.columns([1, 2])
                    if k1.button("취소", key=f"w_cancel_{aid}"):
                        cancel_action(action)
                        st.rerun()
                    if k2.button("등록", key=f"w_reg_{aid}", type="primary"):
                        execute_calendar(action, title, d.isoformat(), desc)
                        st.rerun()

        # 빠른 실행
        q1, q2, q3 = st.columns(3)
        if q1.button("요약해줘", key="q_summary"):
            incoming = "오늘 회의 내용을 요약해줘"
        if q2.button("이번 주 일정", key="q_week"):
            incoming = "이번 주 일정 알려줘"
        if q3.button("업무를 캘린더에", key="q_calendar"):
            incoming = "내 업무를 캘린더에 등록해줘"

        # 텍스트 입력
        with st.form("msg_form", clear_on_submit=True, border=False):
            f1, f2 = st.columns([4, 1], vertical_alignment="bottom")
            typed = f1.text_input("MESSAGE", placeholder="에이블에게 말하기", label_visibility="collapsed")
            sent = f2.form_submit_button("보내기")
        if sent and typed.strip():
            incoming, incoming_via = typed, "text"

        # 음성 입력 (같은 녹음은 한 번만 처리)
        st.markdown('<span class="able-label">VOICE</span>', unsafe_allow_html=True)
        audio_value = st.audio_input("음성으로 말하기", key="mic", label_visibility="collapsed")
        if audio_value is not None:
            audio_bytes = audio_value.getvalue()
            audio_hash = hashlib.md5(audio_bytes).hexdigest()
            if audio_hash != st.session_state.last_audio_hash:
                st.session_state.last_audio_hash = audio_hash
                if client is None:
                    set_notice("error", "OPENAI_API_KEY 가 없어 음성을 인식할 수 없어요.")
                else:
                    try:
                        with messages_box, st.spinner("듣고 있어요..."):
                            heard = transcribe(audio_bytes)
                        if heard:
                            incoming, incoming_via = heard, "voice"
                        else:
                            set_notice("warning", "음성을 알아듣지 못했어요. 다시 말씀해 주세요.")
                    except Exception as e:
                        set_notice("error", f"음성 인식에 실패했어요: {e}")

        # 하단: 워드마크 + history n / 10 + clear
        z1, z2 = st.columns([2, 1], vertical_alignment="bottom")
        z1.markdown('<span class="able-mark-sm">able.</span>', unsafe_allow_html=True)
        z2.markdown(f'<div class="able-foot">history {count_turns(st.session_state.messages)} / {MAX_TURNS}</div>', unsafe_allow_html=True)
        if z2.button("clear conversation", key="btn_clear"):
            st.session_state.messages = []
            st.session_state.pending_actions = []
            st.session_state.tts_audio = None
            st.session_state.tts_autoplay = False
            st.rerun()

        # 이번 rerun 에 들어온 발화 처리 (버튼 / 텍스트 / 음성 중 하나)
        if incoming:
            handle_user_message(incoming, incoming_via, messages_box)

# ---- 푸터 ----
st.markdown('<div class="able-footer"><span>LISTEN · SUMMARIZE · SCHEDULE · SEND</span>'
            '<span>KT AIVLE SCHOOL — MINI PROJECT 03</span></div>', unsafe_allow_html=True)
