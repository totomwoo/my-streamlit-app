
# AIVLE School 학습 도우미 (쿠키 선배)
# Colab에서 app.py 하나로 배포할 수 있도록 모듈을 한 파일로 합친 버전입니다.



# ======================================================================
# 마스코트 SVG
# ======================================================================
# 인라인 SVG 상수 모음 (마스코트 '쿠키 선배').
from urllib.parse import quote

MASCOT_SVG = (
    '<svg viewBox="0 0 200 190" xmlns="http://www.w3.org/2000/svg"><defs>'
    '<radialGradient id="ckA" cx="38%" cy="30%" r="75%"><stop offset="0%" stop-color="#FFE7B8"/>'
    '<stop offset="55%" stop-color="#F7BC62"/><stop offset="100%" stop-color="#DE8A2E"/></radialGradient></defs>'
    '<ellipse cx="100" cy="178" rx="62" ry="8" fill="#5B4BE0" opacity="0.12"/>'
    # 포춘쿠키 실루엣: 둥근 윗면 + 아래 양 끝이 접힌 날개 + 가운데가 올라간 접힘
    '<path d="M14 156 C 4 96, 46 34, 100 34 C 154 34, 196 96, 186 156 C 182 168, 166 170, 154 160 '
    'C 138 148, 120 142, 100 145 C 80 142, 62 148, 46 160 C 34 170, 18 168, 14 156 Z" fill="url(#ckA)"/>'
    # 접혀 내려온 앞날개(살짝 어둡게) + 접힌 선 + 하이라이트
    '<path d="M24 150 C 56 116, 144 116, 176 150 C 178 160, 168 166, 156 160 C 138 148, 120 142, 100 145 '
    'C 80 142, 62 148, 44 160 C 32 166, 22 160, 24 150 Z" fill="#C9781F" opacity="0.28"/>'
    '<path d="M30 141 C 60 111, 140 111, 170 141" fill="none" stroke="#FFFFFF" stroke-width="2.5" '
    'stroke-linecap="round" opacity="0.4"/>'
    '<path d="M24 150 C 56 116, 144 116, 176 150" fill="none" stroke="#B5651A" stroke-width="3.5" '
    'stroke-linecap="round" opacity="0.75"/>'
    # 접힌 틈 + 삐져나온 쪽지
    '<path d="M84 146 C 92 136, 108 136, 116 146 C 108 142, 92 142, 84 146 Z" fill="#7A3E0E" opacity="0.6"/>'
    '<g transform="rotate(22 100 146)"><rect x="98" y="139" width="62" height="15" rx="2.5" fill="#FFFFFF" '
    'stroke="#EADBC2" stroke-width="2"/><path d="M110 146.5 H150" stroke="#F28A8A" stroke-width="2" '
    'stroke-linecap="round" stroke-dasharray="4 4"/></g>'
    '<ellipse cx="62" cy="76" rx="20" ry="9" fill="#FFFFFF" opacity="0.5" transform="rotate(-30 62 76)"/>'
    '<ellipse cx="60" cy="106" rx="12" ry="7" fill="#FF8FA3" opacity="0.5"/>'
    '<ellipse cx="140" cy="106" rx="12" ry="7" fill="#FF8FA3" opacity="0.5"/>'
    '<ellipse cx="78" cy="94" rx="7.5" ry="9" fill="#3A2614"/><ellipse cx="122" cy="94" rx="7.5" ry="9" fill="#3A2614"/>'
    '<circle cx="80.5" cy="90.5" r="2.6" fill="#FFFFFF"/><circle cx="124.5" cy="90.5" r="2.6" fill="#FFFFFF"/>'
    '<path d="M92 106 Q100 114 108 106" fill="none" stroke="#3A2614" stroke-width="3.5" stroke-linecap="round"/>'
    '<path d="M58 40 L104 20 L150 40 L104 60 Z" fill="#2E2660"/>'
    '<path d="M78 48 L78 58 C 78 66, 130 66, 130 58 L130 48 L104 60 Z" fill="#3D3480"/>'
    '<path d="M150 40 L152 62" stroke="#F7BC62" stroke-width="3" stroke-linecap="round"/>'
    '<circle cx="152" cy="65" r="4.5" fill="#F7BC62"/></svg>'
)

# CSS background / <img src> 용 URL 인코딩 data-URI
MASCOT_URI = "data:image/svg+xml," + quote(MASCOT_SVG)


def mascot_img(width: int, cls: str = "") -> str:
    """마스코트를 <img> 태그로 반환 (비율 200:190 유지)."""
    height = round(width * 190 / 200)
    return (
        '<img class="' + cls + '" src="' + MASCOT_URI + '" width="' + str(width)
        + '" height="' + str(height) + '" alt="쿠키 선배"/>'
    )



# ======================================================================
# CSS (inject_css)
# ======================================================================
# 모든 CSS 는 여기 inject_css() 한 곳에서만 주입한다 (Streamlit 1.64.0 기준).
import streamlit as st


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@700&family=Noto+Sans+KR:wght@400;500;700;800&family=Poppins:wght@700&display=swap');

/* :root 디자인 토큰 */
:root{
  --primary:#5B4BE0; --primary-hover:#4B3CD0; --primary-soft:#EEEBFF;
  --text:#1E1B3A; --text-sub:#5E6278; --muted:#94A3B8;
  --surface:#FFFFFF; --bg:#F6F5FF; --border:#E6E4F2;
  --cookie:#F7BC62; --cookie-deep:#B45309; --cookie-soft:#FFF1DE; --project:#C2410C;
  --ink:#2E2660;
  --pastel-1:#EEEBFF; --pastel-2:#E3F6EC; --pastel-3:#FFF1DE; --pastel-4:#E4F1FF; --pastel-5:#FFE9EF;
  --ic-1:#5B4BE0; --ic-2:#1E9E6A; --ic-3:#B45309; --ic-4:#2F7BD9; --ic-5:#D6497A;
  --radius-lg:20px; --radius-md:14px; --radius-sm:10px;
  --shadow:0 4px 18px rgba(40,30,120,.06);
  --font:'Noto Sans KR',sans-serif;
}

/* 전역 폰트: html, body, [class*="css"], stAppViewContainer, stSidebar, 입력 요소 */
html, body, [class*="css"], [data-testid="stAppViewContainer"], [data-testid="stSidebar"],
[data-testid="stMarkdownContainer"], button, input, textarea{font-family:var(--font);}
body{color:var(--text);}

/* stApp / stMain / stBottom 배경, stHeader 투명, #MainMenu/footer 숨김 */
[data-testid="stApp"], [data-testid="stAppViewContainer"], [data-testid="stMain"]{background:var(--bg);}
[data-testid="stBottom"], [data-testid="stBottom"] > div{background:var(--bg);}
[data-testid="stHeader"]{background:transparent;}
#MainMenu, footer{visibility:hidden;}

/* stMainBlockContainer / stBottomBlockContainer: 본문 폭/여백은 여기 한 곳에서만 */
[data-testid="stMainBlockContainer"]{max-width:760px;padding:56px 20px 40px;}
[data-testid="stBottomBlockContainer"]{max-width:760px;padding:8px 20px 28px;}

/* button[kind="primary"]: 기본 primary 버튼 */
button[kind="primary"]{background:var(--primary);color:var(--surface);border:1px solid var(--primary);
  border-radius:var(--radius-md);font-weight:600;}
button[kind="primary"]:hover{background:var(--primary-hover);border-color:var(--primary-hover);color:var(--surface);}
/* button[kind="secondary"]: 기본 secondary 버튼 */
button[kind="secondary"]{background:var(--surface);color:var(--text);border:1px solid var(--border);
  border-radius:var(--radius-md);}
button[kind="secondary"]:hover{border-color:var(--primary);color:var(--primary);}

/* [data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"]: 입력창 */
[data-baseweb="input"], [data-baseweb="textarea"]{border-radius:var(--radius-sm);border-color:var(--border);}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within{border-color:var(--primary);}

/* role="dialog": 다이얼로그 모서리/배경 */
div[role="dialog"]{border-radius:var(--radius-lg);background:var(--surface);}

/* ============ 사이드바 ============ */
/* stSidebar: 흰 배경 + 오른쪽 경계선 */
[data-testid="stSidebar"]{background:var(--surface);border-right:1px solid var(--border);}
/* stSidebar 버튼 공통: 메뉴형(왼쪽 정렬, 테두리 없음) */
[data-testid="stSidebar"] button[kind="secondary"], [data-testid="stSidebar"] button[kind="primary"]{
  border:none;background:transparent;color:var(--text);min-height:36px;padding:6px 10px;
  border-radius:var(--radius-sm);font-weight:500;box-shadow:none;justify-content:flex-start;}
[data-testid="stSidebar"] button[kind="secondary"]:hover{background:var(--bg);color:var(--text);}
[data-testid="stSidebar"] button[kind="primary"]{background:var(--primary-soft);color:var(--primary);font-weight:700;}
[data-testid="stSidebar"] button > div{justify-content:flex-start;text-align:left;min-width:0;}
[data-testid="stSidebar"] button [data-testid="stMarkdownContainer"]{justify-content:flex-start;text-align:left;
  min-width:0;overflow:hidden;}
[data-testid="stSidebar"] button [data-testid="stMarkdownContainer"] p{white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;font-size:14px;}
[data-testid="stSidebar"] [data-testid="stIconMaterial"]{color:var(--primary);}

/* st-key-logo_home: 로고 버튼 (마스코트 + AIVLE + 학습 도우미) */
[data-testid="stSidebar"] .st-key-logo_home button{background:url("__MASCOT__") no-repeat 4px center/40px auto;
  padding:6px 8px 6px 54px;min-height:52px;margin-bottom:6px;}
[data-testid="stSidebar"] .st-key-logo_home button:hover{background-color:transparent;}
[data-testid="stSidebar"] .st-key-logo_home button [data-testid="stMarkdownContainer"] p{font-size:13px;
  color:var(--text-sub);display:flex;align-items:baseline;gap:8px;}
[data-testid="stSidebar"] .st-key-logo_home button strong{font-family:'Poppins',sans-serif;font-weight:700;
  font-size:22px;color:var(--primary);letter-spacing:.5px;}

/* st-key-sbhead_*: 사이드바 섹션 헤더 (제목 + 작은 액션 버튼) */
[data-testid="stSidebar"] [class*="st-key-sbhead_"]{margin-top:10px;padding:0 4px 0 10px;}
[data-testid="stSidebar"] [class*="st-key-sbhead_"] [data-testid="stMarkdownContainer"] p{font-size:12px;
  font-weight:700;color:var(--text-sub);letter-spacing:.4px;}
[data-testid="stSidebar"] [class*="st-key-sbhead_"] button{min-height:28px;padding:2px 8px;color:var(--primary);}
[data-testid="stSidebar"] [class*="st-key-sbhead_"] button [data-testid="stMarkdownContainer"] p{font-size:12px;
  font-weight:700;color:var(--primary);}
[data-testid="stSidebar"] [class*="st-key-sbhead_"] button:hover{background:var(--primary-soft);}

/* st-key-sblist_*: 사이드바 목록 간격 */
[data-testid="stSidebar"] [class*="st-key-sblist_"]{gap:4px;}

/* st-key-chatrow_*: 대화 목록 한 줄 (오른쪽 위 × 삭제 버튼) */
[data-testid="stSidebar"] [class*="st-key-chatrow_"]{position:relative;gap:0;}
[data-testid="stSidebar"] [class*="st-key-chatrow_"] [class*="st-key-chat_"] button{padding-right:34px;}
[data-testid="stSidebar"] [class*="st-key-chat_"] [data-testid="stIconMaterial"]{color:var(--muted);}
/* st-key-del_*: 절대 위치 × 버튼 */
[class*="st-key-del_"]{position:absolute!important;top:6px;right:8px;width:auto!important;z-index:5;}
[data-testid="stSidebar"] [class*="st-key-del_"] button, [class*="st-key-del_"] button{min-height:0;width:auto;
  padding:2px 4px;border:none;background:transparent;box-shadow:none;color:var(--text-sub);opacity:.35;}
[data-testid="stSidebar"] [class*="st-key-del_"] button:hover, [class*="st-key-del_"] button:hover{opacity:.9;
  background:transparent;color:var(--text-sub);}
[class*="st-key-del_"] button [data-testid="stMarkdownContainer"] p{font-size:16px;line-height:1.2;}

/* st-key-stepc_* (닫힘) / st-key-stepo_* (열림): STEP 아코디언 헤더 + 셰브런 */
[data-testid="stSidebar"] [class*="st-key-stepc_"] button, [data-testid="stSidebar"] [class*="st-key-stepo_"] button{
  position:relative;padding-right:30px;font-weight:700;}
[data-testid="stSidebar"] [class*="st-key-stepc_"] button::after,
[data-testid="stSidebar"] [class*="st-key-stepo_"] button::after{content:"";position:absolute;right:14px;top:50%;
  width:7px;height:7px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);
  transform:translateY(-70%) rotate(45deg);transition:transform .15s;}
[data-testid="stSidebar"] [class*="st-key-stepo_"] button::after{transform:translateY(-30%) rotate(-135deg);}
[data-testid="stSidebar"] [class*="st-key-stepc_"] p > span:first-child,
[data-testid="stSidebar"] [class*="st-key-stepo_"] p > span:first-child{background:var(--primary-soft)!important;
  color:var(--primary)!important;font-size:10.5px;font-weight:800;padding:3px 7px;border-radius:999px;
  margin-right:6px;letter-spacing:.3px;}
/* st-key-stepitems_*: 아코디언 패널 (들여쓰기 + 페이드인) */
[data-testid="stSidebar"] [class*="st-key-stepitems_"]{margin-left:14px;width:calc(100% - 14px)!important;
  border-left:2px solid var(--border);padding-left:6px;gap:2px;animation:ckFade .18s ease-out;}
@keyframes ckFade{from{opacity:0;transform:translateY(-4px);}to{opacity:1;transform:none;}}
[data-testid="stSidebar"] [class*="st-key-stepitems_"] button{min-height:32px;padding:4px 8px;}
/* st-key-roomp_*: 미니프로젝트 항목 아이콘은 주황 */
[data-testid="stSidebar"] [class*="st-key-roomp_"] [data-testid="stIconMaterial"]{color:var(--project);}
/* st-key-rooml_* / roomp_* 의 '지금' 배지 */
[data-testid="stSidebar"] [class*="st-key-stepitems_"] p > span{background:var(--cookie-soft)!important;
  color:var(--cookie-deep)!important;font-size:10.5px;font-weight:800;padding:2px 7px;border-radius:999px;margin-left:4px;}

/* ck-doc: 사이드바 하단 연결 문서 카드 (st.html) */
.ck-doc{display:flex;align-items:center;gap:10px;margin-top:14px;padding:12px 14px;background:var(--bg);
  border:1px solid var(--border);border-radius:var(--radius-md);}
.ck-doc-dot{width:8px;height:8px;border-radius:50%;background:var(--ic-2);flex:none;}
.ck-doc-name{font-size:12.5px;font-weight:700;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.ck-doc-sub{font-size:11.5px;color:var(--text-sub);}

/* ============ 홈 ============ */
/* ck-hero: 히어로 (왼쪽 문구 + 오른쪽 마스코트/말풍선) */
.ck-hero{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:4px 4px 0;}
.ck-hero-txt{flex:1 1 300px;}
.ck-hero-small{font-size:14px;color:var(--text-sub);font-weight:500;margin-bottom:6px;}
.ck-hero-big{font-size:36px;font-weight:800;color:var(--text);letter-spacing:-1px;line-height:1.25;}
.ck-hero-sub{font-size:15px;color:var(--text-sub);margin-top:10px;}
.ck-hero-art{position:relative;flex:0 0 250px;height:190px;}
.ck-hero-art img{position:absolute;right:26px;bottom:0;}
.ck-bubble{position:absolute;background:var(--ink);color:var(--surface);font-size:12.5px;font-weight:700;
  padding:7px 12px;border-radius:14px;white-space:nowrap;box-shadow:var(--shadow);}
.ck-bubble.b1{left:0;top:26px;border-bottom-right-radius:4px;}
.ck-bubble.b2{right:0;top:0;border-bottom-left-radius:4px;}

/* st-key-cattile_*: 카테고리 타일 (파스텔 아이콘 사각형 + 라벨, 선택 = 2px primary 테두리) */
[class*="st-key-cattile_"] button{flex-direction:column;gap:8px;min-height:104px;padding:14px 6px;
  background:var(--surface);border:2px solid transparent;border-radius:var(--radius-lg);box-shadow:var(--shadow);
  color:var(--text);font-weight:700;}
[class*="st-key-cattile_"] button > div, [class*="st-key-cattile_"] button > div > span{display:flex;
  flex-direction:column;align-items:center;gap:8px;}
[class*="st-key-cattile_"] button:hover{border-color:var(--border);color:var(--text);background:var(--surface);}
[class*="st-key-cattile_"] button[kind="primary"], [class*="st-key-cattile_"] button[kind="primary"]:hover{
  border-color:var(--primary);background:var(--surface);color:var(--text);}
[class*="st-key-cattile_"] button [data-testid="stMarkdownContainer"] p{font-size:13.5px;font-weight:700;}
[class*="st-key-cattile_"] [data-testid="stIconMaterial"]{width:44px;height:44px;border-radius:var(--radius-md);
  display:flex;align-items:center;justify-content:center;font-size:24px;margin:0;flex:none;}
.st-key-cattile_0 [data-testid="stIconMaterial"]{background:var(--pastel-1);color:var(--ic-1);}
.st-key-cattile_1 [data-testid="stIconMaterial"]{background:var(--pastel-2);color:var(--ic-2);}
.st-key-cattile_2 [data-testid="stIconMaterial"]{background:var(--pastel-3);color:var(--ic-3);}
.st-key-cattile_3 [data-testid="stIconMaterial"]{background:var(--pastel-4);color:var(--ic-4);}
.st-key-cattile_4 [data-testid="stIconMaterial"]{background:var(--pastel-5);color:var(--ic-5);}

/* st-key-qcard_*: 질문 카드 (태그 pill + 질문 + 둥근 셰브런) */
[class*="st-key-qcard_"] button{position:relative;min-height:104px;padding:18px 58px 18px 20px;
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);box-shadow:var(--shadow);
  justify-content:flex-start;align-items:flex-start;}
[class*="st-key-qcard_"] button:hover{border-color:var(--primary);color:var(--text);}
[class*="st-key-qcard_"] button > div{justify-content:flex-start;text-align:left;}
[class*="st-key-qcard_"] button [data-testid="stMarkdownContainer"]{justify-content:flex-start;text-align:left;}
[class*="st-key-qcard_"] button [data-testid="stMarkdownContainer"] p{font-size:15.5px;font-weight:700;
  color:var(--text);line-height:1.45;}
[class*="st-key-qcard_"] button p > span:first-child{display:block;width:fit-content;margin-bottom:10px;
  background:var(--primary-soft)!important;color:var(--primary)!important;font-size:11.5px;font-weight:700;
  padding:3px 10px;border-radius:999px;}
[class*="st-key-qcard_"] button::after{content:"›";position:absolute;right:18px;top:50%;transform:translateY(-50%);
  width:30px;height:30px;border-radius:50%;background:var(--primary-soft);color:var(--primary);font-size:20px;
  line-height:27px;text-align:center;font-weight:700;}

/* ============ 대화 / 학습방 ============ */
/* ck-chat-head: 대화 헤더 (제목 + 연결 칩) */
.ck-chat-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;}
.ck-title{font-size:22px;font-weight:800;color:var(--text);letter-spacing:-.4px;}
.ck-chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;color:var(--primary);
  background:var(--primary-soft);padding:5px 11px;border-radius:999px;white-space:nowrap;}
.ck-chip i{width:7px;height:7px;border-radius:50%;background:var(--ic-2);display:inline-block;}
/* ck-user: 사용자 말풍선 (오른쪽 정렬, primary) */
.ck-user{display:flex;justify-content:flex-end;}
.ck-user > div{max-width:78%;background:var(--primary);color:var(--surface);padding:11px 16px;font-size:15px;
  border-radius:var(--radius-lg);border-bottom-right-radius:6px;line-height:1.55;white-space:pre-wrap;word-break:break-word;}
/* st-key-card_*: 카드 공통 (assistant 답변 카드 포함) */
[class*="st-key-card_"]{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  box-shadow:var(--shadow);padding:20px 22px;}
/* ck-head: 답변 카드 머리 (아바타 + 이름) */
.ck-head{display:flex;align-items:center;gap:10px;}
.ck-head img{background:var(--cookie-soft);border-radius:50%;padding:3px;}
.ck-name{font-size:14px;font-weight:700;color:var(--text);}
/* ck-box.note: 안내 박스 (키 없음 등) */
.ck-box{border-radius:var(--radius-md);padding:13px 16px;font-size:14.5px;line-height:1.6;color:var(--text);}
.ck-box b{display:block;font-size:12px;font-weight:800;margin-bottom:4px;letter-spacing:.2px;}
.ck-box.note{background:var(--bg);border:1px dashed var(--border);} .ck-box.note b{color:var(--text-sub);}
/* button[kind=pillsActive|segmented_controlActive]: config.toml 없이 app.py 하나로 배포해도 선택 상태를 보라색으로 */
button[kind="pillsActive"],button[kind="segmented_controlActive"]{background:var(--primary-soft)!important;
  border-color:var(--primary)!important;color:var(--primary-hover)!important;}
/* ck-extra: 선배 한마디 / 오늘 해 볼 것 (색 박스 대신 구분선 + 아이콘 줄) */
.ck-extra{border-top:1px solid var(--border);padding-top:14px;display:flex;flex-direction:column;gap:12px;}
.ck-row{display:flex;gap:12px;align-items:flex-start;}
.ck-ic{flex:none;width:28px;height:28px;border-radius:9px;display:flex;align-items:center;justify-content:center;}
.ck-ic.q{background:var(--cookie-soft);color:var(--cookie-deep);}
.ck-ic.t{background:var(--primary-soft);color:var(--primary);}
.ck-row b{display:block;font-size:12px;font-weight:700;color:var(--text-sub);margin-bottom:2px;}
.ck-row p{margin:0;font-size:14.5px;line-height:1.65;color:var(--text);}
/* ck-srcs: 출처 (배경 없는 작은 회색 글자) */
.ck-srcs{display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;}
.ck-src-lbl{font-size:12.5px;font-weight:700;color:var(--text-sub);}
.ck-src{font-size:12.5px;font-weight:500;color:var(--text-sub);background:none;border:none;padding:0;text-decoration:none;}
a.ck-src:hover{color:var(--primary);text-decoration:underline;}
/* st-key-card_msg_*: 답변 카드 안 목록(굵은 제목 + 회색 설명), 근거 문단 펼침(테두리 없음) */
[class*="st-key-card_msg_"] li:has(strong){color:var(--text-sub);}
[class*="st-key-card_msg_"] li strong{color:var(--text);}
[class*="st-key-card_msg_"] details{border:none!important;background:transparent!important;}
[class*="st-key-card_msg_"] details summary{padding-left:0!important;color:var(--text-sub);font-size:13px;}
.ck-label{font-size:12px;font-weight:800;color:var(--text-sub);letter-spacing:.2px;}
/* st-key-fu_*: 이어서 물어보기 버튼 (왼쪽 정렬) / st-key-cmd_*: 명령어/추천 버튼 */
[class*="st-key-fu_"] button, [class*="st-key-cmd_"] button{justify-content:flex-start;min-height:38px;
  border-radius:var(--radius-sm);}
[class*="st-key-fu_"] button > div, [class*="st-key-cmd_"] button > div{justify-content:flex-start;text-align:left;}
[class*="st-key-fu_"] button [data-testid="stMarkdownContainer"],
[class*="st-key-cmd_"] button [data-testid="stMarkdownContainer"]{justify-content:flex-start;text-align:left;}
[class*="st-key-fu_"] button [data-testid="stMarkdownContainer"] p,
[class*="st-key-cmd_"] button [data-testid="stMarkdownContainer"] p{font-size:14px;}
[class*="st-key-fu_"] [data-testid="stIconMaterial"], [class*="st-key-cmd_"] [data-testid="stIconMaterial"]{color:var(--primary);}

/* ck-room: 학습방 헤더 */
.ck-crumb{font-size:12.5px;font-weight:700;color:var(--primary);margin-bottom:6px;}
.ck-room-title{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
.ck-now{font-size:11px;font-weight:800;color:var(--cookie-deep);background:var(--cookie-soft);
  padding:3px 9px;border-radius:999px;}
.ck-desc{font-size:14px;color:var(--text-sub);margin-top:6px;}
/* ck-curr: /커리큘럼 카드 */
.ck-curr-step{font-size:13px;font-weight:800;color:var(--primary);margin:10px 0 6px;}
.ck-curr-items{display:flex;flex-wrap:wrap;gap:6px;}
.ck-curr-items span{font-size:12.5px;padding:4px 10px;border-radius:999px;background:var(--bg);color:var(--text);
  border:1px solid var(--border);}
.ck-curr-items span.p{color:var(--project);background:var(--cookie-soft);border-color:var(--cookie-soft);font-weight:700;}
.ck-curr-items span.cur{border-color:var(--primary);box-shadow:0 0 0 1px var(--primary);}

/* stChatInput: 입력창 모서리 */
[data-testid="stChatInput"]{border-radius:var(--radius-lg);}

/* st-key-float_wrap / st-key-float_cookie: 떠다니는 포춘쿠키 (오른쪽 여백, 1280px 미만에서는 숨김) */
.st-key-float_wrap{position:fixed!important;right:34px;bottom:150px;width:92px!important;z-index:50;
  animation:ckBob 5s ease-in-out infinite;}
@keyframes ckBob{0%,100%{transform:translateY(0) rotate(-2deg);}50%{transform:translateY(-12px) rotate(3deg);}}
.st-key-float_cookie button, .st-key-float_cookie button:hover, .st-key-float_cookie button:active,
.st-key-float_cookie button:focus{width:92px;height:88px;min-height:0;padding:0;border:none;box-shadow:none;
  background:url("__MASCOT__") no-repeat center/contain;position:relative;overflow:visible;}
.st-key-float_cookie button [data-testid="stMarkdownContainer"]{position:absolute;top:-12px;right:-12px;
  background:var(--ink);color:var(--surface);border-radius:12px;border-bottom-left-radius:3px;padding:2px 8px;}
.st-key-float_cookie button [data-testid="stMarkdownContainer"] p{font-size:11.5px;font-weight:700;color:var(--surface);}
@media (max-width:1279px){.st-key-float_wrap{display:none!important;}}

/* ck-fortune: 포춘쿠키 다이얼로그 (쪽지 = Gaegu) */
.ck-fortune{text-align:center;}
.ck-slip{margin:10px auto 0;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);
  box-shadow:var(--shadow);padding:18px 20px;position:relative;}
.ck-slip-q{font-family:'Gaegu',cursive;font-weight:700;font-size:25px;line-height:1.35;color:var(--text);}
.ck-slip-w{font-size:12px;color:var(--text-sub);margin-top:6px;}
.ck-adv{margin-top:12px;text-align:left;background:var(--cookie-soft);}
.ck-adv b{color:var(--cookie-deep);}

/* st-key-edrow_*: 학습방 편집 행의 ↑ ↓ × 버튼 */
[class*="st-key-edrow_"] button{min-height:38px;padding:0 8px;}

/* 좁은 화면: 타일은 가로형, 히어로 축소 */
@media (max-width:640px){
  [data-testid="stMainBlockContainer"]{padding:56px 16px 32px;}
  .ck-hero-big{font-size:28px;}
  .ck-hero-art{flex:1 1 100%;height:150px;}
  .ck-hero-art img{width:130px;height:auto;right:calc(50% - 65px);}
  .ck-bubble.b1{left:4px;} .ck-bubble.b2{right:4px;}
  [class*="st-key-cattile_"] button, [class*="st-key-cattile_"] button > div,
  [class*="st-key-cattile_"] button > div > span{flex-direction:row;justify-content:flex-start;gap:12px;}
  [class*="st-key-cattile_"] button{min-height:60px;padding:8px 16px;}
  [class*="st-key-cattile_"] button > div{width:100%;padding-left:8px;}
  [class*="st-key-cattile_"] button > div > span > span{margin:0;}
  .ck-user > div{max-width:90%;}
  [class*="st-key-card_"]{padding:16px 16px;}
}
"""


def inject_css():
    st.html("<style>" + CSS.replace("__MASCOT__", MASCOT_URI) + "</style>")



# ======================================================================
# RAG 파이프라인
# ======================================================================
# RAG 파이프라인 (미션 2 팀 표준 rag_pipeline 재사용 + 구조화 출력/출처 반환).
import os
import warnings
from operator import itemgetter
from pathlib import Path
from typing import List

warnings.filterwarnings(action="ignore")

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent
CHROMA_DIR = str(APP_DIR / "chroma_db")
CHAT_MODEL = "gpt-4o-mini"
EMBED_MODEL = "text-embedding-3-small"

IMPORT_ERROR = None
try:
    import pymupdf

    pymupdf.set_messages(path=os.devnull)
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePassthrough, RunnableLambda
    from langchain_pymupdf4llm import PyMuPDF4LLMLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_chroma import Chroma
    from pydantic import BaseModel, Field
except Exception as e:  # 패키지 미설치/DLL 차단 시에도 UI 는 떠야 한다
    IMPORT_ERROR = repr(e)
    from pydantic import BaseModel, Field


# ---------------------------------------------------------------- API KEY
def load_api_key() -> bool:
    """os.environ → st.secrets → api_key.txt(KEY=VALUE) 순서로 키를 찾는다."""
    if os.environ.get("OPENAI_API_KEY"):
        return True
    try:
        import streamlit as st

        key = st.secrets["OPENAI_API_KEY"]
        if key:
            os.environ["OPENAI_API_KEY"] = str(key)
            return True
    except Exception:
        pass
    for folder in (PROJECT_DIR, APP_DIR):
        fp = folder / "api_key.txt"
        if fp.exists():
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and "=" in line:
                            key, value = line.split("=", 1)
                            os.environ[key.strip()] = value.strip().strip('"').strip("'")
            except Exception:
                pass
    return bool(os.environ.get("OPENAI_API_KEY"))


def ready() -> bool:
    return IMPORT_ERROR is None and load_api_key()


# ---------------------------------------------------------------- 구조화 출력
class SeniorAnswer(BaseModel):
    """쿠키 선배의 답변 형식"""

    answer: str = Field(description="핵심 답변. 마크다운, 번호 목록 2~4개, 짧게. 해요체.")
    senior_quote: str = Field(
        description="문서의 [재학생 경험] 문단에서 가져온 선배의 한마디 1~2문장. 해당 문단이 없으면 빈 문자열."
    )
    challenge: str = Field(description="오늘 바로 해 볼 수 있는 구체적인 행동 한 가지. 한 문장.")
    followups: List[str] = Field(description="이어서 물어볼 만한 질문 3개. 각 25자 이내.")


def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)


SYSTEM_PROMPT = (
    "당신은 KT AIVLE School 을 먼저 수료한 다정한 선배 '쿠키 선배'입니다.\n"
    "사실에 관한 질문은 반드시 아래 [문서] 내용만 근거로 답변하세요.\n"
    "문서에 없는 내용이면 추측하지 말고 '백서에서 확인할 수 없는 내용이에요.'라고 말한 뒤, "
    "AIVLE-EDU 공지사항이나 1:1 문의, 담당 에이블매니저에게 확인하도록 안내하세요.\n"
    "말투는 따뜻한 해요체로, 결론을 먼저 말하고 번호 목록으로 짧게 정리하세요.\n"
    "후배가 바로 움직일 수 있도록 행동을 권하고 응원해 주세요.\n"
    "문서의 장, 절 번호나 '~장을 참고하세요' 같은 문서 위치 안내는 쓰지 말고 내용을 직접 설명하세요.\n"
    "가운뎃점 기호(·)는 쓰지 말고 쉼표나 '와/과'로 이어 쓰세요.\n"
    "senior_quote 는 [문서]에 '[재학생 경험]' 문단이 있을 때만 그 내용을 옮겨 쓰고, 없으면 비워 두세요.\n\n"
    "[이전 대화]\n{history}\n\n[문서]\n{context}"
)


# ---------------------------------------------------------------- RAG 파이프라인 함수
def rag_pipeline(filepath, collection_name="aivle_docs", k=4, with_retriever=False):
    """PDF → 분할 → 임베딩 → Chroma → 검색기 → 체인.

    체인은 {"input": 질문, "history": (선택)} 을 받아
    {"answer": SeniorAnswer, "docs": [검색된 Document]} 를 돌려준다.
    collection_name 을 문서마다 다르게 주어 reset_collection 이 서로를 지우지 않게 한다.
    """
    # PDF 파일 읽기
    loader = PyMuPDF4LLMLoader(filepath)
    docs = loader.load()

    # 텍스트 분할
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splits = splitter.split_documents(docs)

    # Embedding 모델
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)

    # 벡터저장소 만들기
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    # 기존 데이터 비우기
    vectorstore.reset_collection()

    # 문서 추가
    vectorstore.add_documents(splits)

    # 검색기 구성
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    rag_chain = build_chain(retriever)
    if with_retriever:
        return rag_chain, retriever
    return rag_chain


def has_collection(collection_name="aivle_docs"):
    """Colab에서 만들어 GitHub에 올린 chroma_db 폴더에 해당 컬렉션이 있는지."""
    if IMPORT_ERROR or not os.path.isdir(CHROMA_DIR):
        return False
    try:
        import chromadb
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        return client.get_collection(collection_name).count() > 0
    except Exception:
        return False


def load_collection(collection_name="aivle_docs", k=4):
    """저장된 chroma_db 컬렉션을 다시 벡터화하지 않고 그대로 불러와 (체인, 검색기)를 만든다."""
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=OpenAIEmbeddings(model=EMBED_MODEL),
        persist_directory=CHROMA_DIR,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return build_chain(retriever), retriever


def build_chain(retriever):
    """검색기 → {"answer": SeniorAnswer, "docs": [Document]} 를 돌려주는 RAG 체인."""
    # LLM 선언 (구조화 출력)
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0).with_structured_output(SeniorAnswer)

    # 프롬프트 구성
    prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", "{input}")])

    # RAG 체인 구성
    rag_chain = (
        RunnablePassthrough.assign(
            docs=itemgetter("input") | retriever,
            history=RunnableLambda(lambda x: x.get("history") or "(없음)"),
        )
        | RunnablePassthrough.assign(context=RunnableLambda(lambda x: format_docs(x["docs"])))
        | RunnablePassthrough.assign(answer=prompt | llm)
        | RunnableLambda(lambda x: {"answer": x["answer"], "docs": x["docs"]})
    )
    return rag_chain


# ---------------------------------------------------------------- 출처 정리
def doc_source(doc, kind):
    """Document → 화면용 출처 dict."""
    page = doc.metadata.get("page")
    label = kind
    if isinstance(page, int):
        label = kind + " p." + str(page + 1)
    elif page not in (None, ""):
        label = kind + " p." + str(page)
    return {"kind": kind, "label": label, "snippet": doc.page_content.strip()[:420], "url": ""}


def to_message(result, kind="백서"):
    """체인 결과 → 화면용 assistant 메시지 dict."""
    ans = result["answer"]
    return {
        "role": "assistant",
        "answer": ans.answer,
        "quote": ans.senior_quote,
        "challenge": ans.challenge,
        "followups": list(ans.followups)[:3],
        "sources": [doc_source(d, kind) for d in result.get("docs", [])],
    }


# ---------------------------------------------------------------- 웹 검색
def _block_text(content):
    if isinstance(content, str):
        return content, []
    texts, cites = [], []
    for b in content or []:
        if isinstance(b, dict) and b.get("type") == "text":
            texts.append(b.get("text", ""))
            for a in b.get("annotations") or []:
                url = a.get("url")
                if url:
                    cites.append({"title": a.get("title") or url, "url": url})
    return "\n".join(texts), cites


def web_search(question, topic):
    """OpenAI 내장 웹 검색(Responses API). 실패하면 (None, []) 을 돌려준다."""
    try:
        llm = ChatOpenAI(model=CHAT_MODEL, use_responses_api=True).bind_tools([{"type": "web_search_preview"}])
        resp = llm.invoke(
            "학습 주제 '" + topic + "' 에 대한 질문이에요. 웹에서 찾아 핵심만 한국어 5문장 이내로 정리해 주세요.\n질문: "
            + question
        )
        text, cites = _block_text(resp.content)
        if not text.strip():
            return None, []
        seen, uniq = set(), []
        for c in cites:
            if c["url"] not in seen:
                seen.add(c["url"])
                uniq.append(c)
        return text, uniq[:4]
    except Exception:
        return None, []


ROOM_PROMPT = (
    "당신은 KT AIVLE School 을 먼저 수료한 다정한 선배 '쿠키 선배'입니다.\n"
    "지금은 '{topic}' 학습방이에요. 이 주제에 맞춰서만 답하고, 주제와 무관한 질문은 일반 대화로 안내하세요.\n"
    "아래 자료를 종합해 답하세요. 교육 과정 운영/규정 같은 사실은 [백서]에 있을 때만 말하고, "
    "없으면 AIVLE-EDU 공지사항을 확인하도록 안내하세요. 개념 설명은 [교안]과 [{web_label}]을 활용하세요.\n"
    "말투는 따뜻한 해요체, 결론 먼저, 번호 목록으로 짧게, 바로 해 볼 행동을 권하세요.\n"
    "senior_quote 는 [백서]에 '[재학생 경험]' 문단이 있을 때만 옮겨 쓰고, 없으면 비워 두세요.\n\n"
    "[이전 대화]\n{history}\n\n[백서]\n{wp}\n\n[교안]\n{lecture}\n\n[{web_label}]\n{web}"
)


def room_answer(question, topic, sources, wp_retriever=None, lecture_retriever=None, history=""):
    """학습방 답변: 켜진 자료(백서/교안/웹 검색)를 종합한다."""
    srcs, wp_docs, lec_docs = [], [], []
    query = topic + " " + question
    if "백서" in sources and wp_retriever is not None:
        wp_docs = wp_retriever.invoke(query)[:3]
        srcs += [doc_source(d, "백서") for d in wp_docs]
    if "교안" in sources and lecture_retriever is not None:
        lec_docs = lecture_retriever.invoke(query)
        srcs += [doc_source(d, "교안") for d in lec_docs]

    web_label, web_text = "웹 검색", "(사용 안 함)"
    if "웹 검색" in sources:
        text, cites = web_search(question, topic)
        if text:
            web_text = text
            if cites:
                for c in cites:
                    srcs.append({"kind": "웹", "label": "웹 " + c["title"][:24], "snippet": c["url"], "url": c["url"]})
            else:
                srcs.append({"kind": "웹", "label": "웹 검색", "snippet": text[:420], "url": ""})
        else:
            web_label = "AI 일반 지식"
            web_text = "(웹 검색을 쓸 수 없어요. 당신이 알고 있는 일반 지식으로 개념을 설명하세요.)"
            srcs.append({"kind": "AI", "label": "AI 일반 지식", "snippet": "웹 검색을 쓸 수 없어 모델의 일반 지식으로 답했어요.", "url": ""})

    prompt = ChatPromptTemplate.from_messages([("system", ROOM_PROMPT), ("human", "{input}")])
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0).with_structured_output(SeniorAnswer)
    ans = (prompt | llm).invoke(
        {
            "topic": topic,
            "web_label": web_label,
            "history": history or "(없음)",
            "wp": format_docs(wp_docs) or "(없음)",
            "lecture": format_docs(lec_docs) or "(없음)",
            "web": web_text,
            "input": question,
        }
    )
    msg = to_message({"answer": ans, "docs": []})
    msg["sources"] = srcs
    return msg


def summarize(history):
    """현재 대화를 요약한다 (/요약)."""
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0)
    resp = llm.invoke(
        "다음은 AIVLE School 교육생과 선배 도우미의 대화예요. 핵심을 번호 목록 3~5개로, 해요체로 요약해 주세요.\n\n" + history
    )
    text, _ = _block_text(resp.content)
    return text



# ======================================================================
# 세션 상태와 데이터
# ======================================================================
# 데이터 로딩, 세션 상태, 화면 전환 헬퍼.
import copy
import json
import random
import time
import uuid
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR / "data"
WHITEPAPER = DATA_DIR / "AIVLE School 백서.pdf"
CURRICULUM_FILE = DATA_DIR / "curriculum.json"


def _items(prefix, rows):
    out = []
    for n, row in enumerate(rows, 1):
        item = {"id": prefix + "-" + str(n), "name": row[0], "type": row[1]}
        if len(row) > 2:
            item["current"] = True
        out.append(item)
    return out


DEFAULT_CURRICULUM = {
    "cohort": "10기 DX 컨설턴트 트랙",
    "steps": [
        {"id": "s1", "name": "분석/생성형 AI", "items": _items("s1", [
            ("파이썬 기초", "learn"), ("데이터 분석", "learn"), ("미니프로젝트 1차", "project"),
            ("머신러닝/딥러닝", "learn"), ("미니프로젝트 2차", "project"), ("생성형 AI", "learn"),
            ("미니프로젝트 3차", "project"), ("LangChain RAG", "learn"), ("미니프로젝트 4차", "project", True)])},
        {"id": "s2", "name": "Cloud/서비스 제안", "items": _items("s2", [
            ("IT 인프라", "learn"), ("Cloud 인프라", "learn"), ("Cloud 설계", "learn"), ("제안 전략", "learn"),
            ("제안서 작성", "learn"), ("프로젝트 관리", "learn"), ("미니프로젝트", "project")])},
        {"id": "s3", "name": "빅프로젝트", "items": _items("s3", [
            ("과제 선정 워크숍", "learn"), ("현직자 코칭", "learn"), ("과제 수행", "learn"), ("발표회", "learn")])},
    ],
}

FALLBACK_CATEGORIES = {"categories": [{"id": "study", "label": "공부 방법", "icon": "menu_book", "questions": [
    {"q": "무엇부터 공부해야 하나요?", "tag": "선배 경험"},
    {"q": "복습은 어떻게 하면 효과적인가요?", "tag": "선배 경험"}]}]}
FALLBACK_FORTUNES = {
    "quotes": [{"text": "천 리 길도 한 걸음부터 시작된다.", "who": "노자 『도덕경』"}],
    "advice": [{"text": "그날 배운 건 그날 10분만 다시 봐요.", "who": "쿠키 선배", "ask": "복습은 어떻게 하면 효과적인가요?"}],
}


def _load_json(path, fallback):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return copy.deepcopy(fallback)


@st.cache_data
def categories():
    return _load_json(DATA_DIR / "categories.json", FALLBACK_CATEGORIES)["categories"]


@st.cache_data
def fortunes():
    return _load_json(DATA_DIR / "fortunes.json", FALLBACK_FORTUNES)


def new_id():
    return uuid.uuid4().hex[:8]


# ---------------------------------------------------------------- 세션 상태
def init_state():
    ss = st.session_state
    if "view" in ss:
        return
    ss.view = "home"
    ss.chats = {}
    ss.current_chat = None
    ss.rooms = {}
    ss.current_room = None
    ss.curriculum = _load_json(CURRICULUM_FILE, DEFAULT_CURRICULUM)
    ss.cat = categories()[0]["id"]
    ss.doc_name = WHITEPAPER.name
    ss.upload_chain = None
    ss.upload_retriever = None
    ss.room_retrievers = {}
    ss.step_open = {}
    cur = current_item()
    for s in ss.curriculum["steps"]:
        ss.step_open[s["id"]] = bool(cur and cur[0]["id"] == s["id"])
    if not any(ss.step_open.values()) and ss.curriculum["steps"]:
        ss.step_open[ss.curriculum["steps"][0]["id"]] = True
    new_fortune()
    if st.query_params.get("demo") == "1":
        seed_demo()


def find_item(item_id):
    """(step, step 번호, item) 또는 None."""
    for n, s in enumerate(st.session_state.curriculum["steps"], 1):
        for it in s["items"]:
            if it["id"] == item_id:
                return s, n, it
    return None


def current_item():
    for n, s in enumerate(st.session_state.curriculum["steps"], 1):
        for it in s["items"]:
            if it.get("current"):
                return s, n, it
    return None


def room(item_id):
    rooms = st.session_state.rooms
    if item_id not in rooms:
        rooms[item_id] = {"messages": [], "doc_name": None}
    return rooms[item_id]


def new_fortune():
    f = fortunes()
    st.session_state.fortune = {"quote": random.choice(f["quotes"]), "advice": random.choice(f["advice"])}


# ---------------------------------------------------------------- 화면 전환 (버튼 콜백)
def go_home():
    st.session_state.view = "home"
    st.session_state.current_chat = None
    st.session_state.current_room = None


def open_chat(cid):
    st.session_state.view = "chat"
    st.session_state.current_chat = cid
    st.session_state.current_room = None


def open_room(item_id):
    room(item_id)
    st.session_state.view = "room"
    st.session_state.current_room = item_id
    st.session_state.current_chat = None


def toggle_step(sid):
    st.session_state.step_open[sid] = not st.session_state.step_open.get(sid, False)


def select_cat(cid):
    st.session_state.cat = cid


def new_chat(first_text):
    cid = new_id()
    title = first_text.strip().replace("\n", " ")
    if len(title) > 22:
        title = title[:22] + "…"
    st.session_state.chats[cid] = {"title": title or "새 대화", "messages": [], "created": time.time()}
    open_chat(cid)
    return cid


def current_messages(create_title=None):
    """현재 화면(대화/학습방)의 메시지 리스트. 홈이면 새 대화를 만든다."""
    ss = st.session_state
    if ss.view == "room" and ss.current_room:
        return room(ss.current_room)["messages"]
    if ss.view == "chat" and ss.current_chat in ss.chats:
        return ss.chats[ss.current_chat]["messages"]
    cid = new_chat(create_title or "새 대화")
    return ss.chats[cid]["messages"]


def send(text):
    """질문을 현재 대화/학습방에 넣는다. 답변은 화면이 그려질 때 생성된다."""
    current_messages(create_title=text).append({"role": "user", "text": text})


def start_chat(text):
    """홈의 질문 카드: 새 대화를 만들고 질문을 보낸다."""
    cid = new_chat(text)
    st.session_state.chats[cid]["messages"].append({"role": "user", "text": text})


# ---------------------------------------------------------------- 데모 (?demo=1)
def seed_demo():
    ss = st.session_state
    q = "복습은 어떻게 하면 효과적인가요?"
    cid = new_chat(q)
    ss.chats[cid]["messages"] = [
        {"role": "user", "text": q},
        {
            "role": "assistant",
            "answer": "복습은 **그날 배운 것을 그날 짧게** 다시 보는 게 가장 효과적이에요.\n\n"
                      "1. 수업 직후 10분, 오늘 배운 개념을 내 말로 3줄 정리해요.\n"
                      "2. 실습 코드는 빈 노트북에서 처음부터 다시 쳐 봐요.\n"
                      "3. 주말에는 한 주 동안 막혔던 오류만 모아 다시 풀어 봐요.",
            "quote": "실습 코드를 그대로 따라 치기만 했을 때는 남는 게 없었는데, 빈 셀에서 다시 짜 보니 "
                     "어디를 모르는지 바로 보였어요.",
            "challenge": "오늘 실습 파일에서 셀 3개만 골라, 보지 않고 다시 작성해 보세요.",
            "followups": ["오류가 나거나 막히면 어떻게 하나요?", "주말 복습 루틴을 추천해 주세요", "스터디는 어떻게 꾸리나요?"],
            "sources": [
                {"kind": "백서", "label": "백서 p.12", "snippet": "[재학생 경험] 실습 코드를 빈 노트북에서 다시 작성해 보는 방식이 가장 도움이 되었다…", "url": ""},
                {"kind": "백서", "label": "백서 p.13", "snippet": "복습은 당일에 짧게 하는 것이 효과적이며, 주말에는 한 주간 막혔던 부분을 모아…", "url": ""},
            ],
        },
    ]
    ss.chats[new_id()] = {"title": "훈련장려금은 얼마인가요?", "messages": [], "created": time.time() - 3600}
    cur = current_item()
    if cur:
        rid = cur[2]["id"]
        room(rid)["messages"] = [
            {"role": "user", "text": "RAG 파이프라인에서 chunk_size 는 어떻게 정하나요?"},
            {
                "role": "assistant",
                "answer": "문서 성격에 맞춰 **작게 시작해서 검색 결과를 보며 조정**하는 게 좋아요.\n\n"
                          "1. 교안 기준은 `chunk_size=500`, `chunk_overlap=100` 이에요.\n"
                          "2. 답이 문단 중간에서 잘리면 overlap 을 늘려요.\n"
                          "3. 엉뚱한 문단이 섞이면 chunk 를 줄이고 k 값을 조정해요.",
                "quote": "",
                "challenge": "같은 질문을 chunk_size 300 / 500 / 800 으로 돌려 보고 검색된 문단을 비교해 보세요.",
                "followups": ["k 값은 몇으로 두면 좋나요?", "Chroma 컬렉션은 왜 나누나요?", "발표 때 무엇을 보여 주면 좋나요?"],
                "sources": [
                    {"kind": "교안", "label": "교안 p.21", "snippet": "RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)…", "url": ""},
                    {"kind": "백서", "label": "백서 p.18", "snippet": "미니프로젝트는 팀 단위로 진행되며…", "url": ""},
                    {"kind": "웹", "label": "웹 LangChain Docs", "snippet": "https://python.langchain.com", "url": "https://python.langchain.com"},
                ],
            },
        ]
    view = st.query_params.get("view", "chat")
    if view == "room" and cur:
        open_room(cur[2]["id"])
    elif view == "home":
        go_home()
    else:
        open_chat(cid)

# 앱 데이터: data/*.json 내용을 그대로 포함 (data 폴더가 없어도 동작)
DEFAULT_CURRICULUM = {'cohort': '10기 DX 컨설턴트 트랙',
 'steps': [{'id': 's1',
            'name': '분석/생성형 AI',
            'items': [{'id': 's1-1', 'name': '파이썬 기초', 'type': 'learn'},
                      {'id': 's1-2', 'name': '데이터 분석', 'type': 'learn'},
                      {'id': 's1-3', 'name': '미니프로젝트 1차', 'type': 'project'},
                      {'id': 's1-4', 'name': '머신러닝/딥러닝', 'type': 'learn'},
                      {'id': 's1-5', 'name': '미니프로젝트 2차', 'type': 'project'},
                      {'id': 's1-6', 'name': '생성형 AI', 'type': 'learn'},
                      {'id': 's1-7', 'name': '미니프로젝트 3차', 'type': 'project'},
                      {'id': 's1-8', 'name': 'LangChain RAG', 'type': 'learn'},
                      {'id': 's1-9', 'name': '미니프로젝트 4차', 'type': 'project', 'current': True}]},
           {'id': 's2',
            'name': 'Cloud/서비스 제안',
            'items': [{'id': 's2-1', 'name': 'IT 인프라', 'type': 'learn'},
                      {'id': 's2-2', 'name': 'Cloud 인프라', 'type': 'learn'},
                      {'id': 's2-3', 'name': 'Cloud 설계', 'type': 'learn'},
                      {'id': 's2-4', 'name': '제안 전략', 'type': 'learn'},
                      {'id': 's2-5', 'name': '제안서 작성', 'type': 'learn'},
                      {'id': 's2-6', 'name': '프로젝트 관리', 'type': 'learn'},
                      {'id': 's2-7', 'name': '미니프로젝트', 'type': 'project'}]},
           {'id': 's3',
            'name': '빅프로젝트',
            'items': [{'id': 's3-1', 'name': '과제 선정 워크숍', 'type': 'learn'},
                      {'id': 's3-2', 'name': '현직자 코칭', 'type': 'learn'},
                      {'id': 's3-3', 'name': '과제 수행', 'type': 'learn'},
                      {'id': 's3-4', 'name': '발표회', 'type': 'learn'}]}]}
FALLBACK_CATEGORIES = {'categories': [{'id': 'study',
                 'label': '공부 방법',
                 'icon': 'menu_book',
                 'questions': [{'q': '무엇부터 공부해야 하나요?', 'tag': '선배 경험'},
                               {'q': '복습은 어떻게 하면 효과적인가요?', 'tag': '선배 경험'},
                               {'q': '오류가 나거나 막히면 어떻게 하나요?', 'tag': '선배 경험'},
                               {'q': '생성형 AI 는 학습에 어떻게 활용하나요?', 'tag': '선배 경험'}]},
                {'id': 'growth',
                 'label': '자기계발',
                 'icon': 'eco',
                 'questions': [{'q': '수학이나 통계가 약해도 괜찮을까요?', 'tag': '선배 경험'},
                               {'q': '기술 역량은 어떻게 쌓아야 하나요?', 'tag': '선배 경험'},
                               {'q': '수업을 놓치거나 의욕이 떨어지면 어떻게 하나요?', 'tag': '선배 경험'},
                               {'q': '후배에게 꼭 전하고 싶은 조언은 무엇인가요?', 'tag': '선배 경험'}]},
                {'id': 'project',
                 'label': '프로젝트',
                 'icon': 'rocket_launch',
                 'questions': [{'q': '프로젝트는 어떻게 준비해야 하나요?', 'tag': '선배 경험'},
                               {'q': '팀 프로젝트에서 어려웠던 점은 무엇이고 어떻게 해결하나요?', 'tag': '선배 경험'},
                               {'q': '빅프로젝트는 어떻게 준비하면 좋을까요?', 'tag': '선배 경험'},
                               {'q': '프로젝트가 끝나면 무엇을 남기나요?', 'tag': '선배 경험'}]},
                {'id': 'career',
                 'label': '취업 준비',
                 'icon': 'work',
                 'questions': [{'q': '취업을 잘하려면 무엇이 중요한가요?', 'tag': '선배 경험'},
                               {'q': '잡페어는 어떻게 활용하면 좋을까요?', 'tag': '선배 경험'},
                               {'q': '에이블스쿨은 어떤 취업 지원 프로그램을 제공하나요?', 'tag': '공식 안내'},
                               {'q': '수료하면 취업에 도움이 되나요? KT 입사에도 도움이 되나요?', 'tag': '공식 안내'}]},
                {'id': 'life',
                 'label': '교육 생활',
                 'icon': 'event',
                 'questions': [{'q': '에이블스쿨 하루 일과는 어떻게 되나요?', 'tag': '공식 안내'},
                               {'q': '하루 공부 시간은 어느 정도가 적당한가요?', 'tag': '선배 경험'},
                               {'q': '온라인 교육이면 혼자 공부하나요?', 'tag': '공식 안내'},
                               {'q': '에이블스쿨 수료 기준은 무엇인가요?', 'tag': '공식 안내'}]}]}
FALLBACK_FORTUNES = {'quotes': [{'text': '배우고 때때로 익히면 또한 기쁘지 아니한가.', 'who': '공자 『논어』'},
            {'text': '천 리 길도 한 걸음부터 시작된다.', 'who': '노자 『도덕경』'},
            {'text': '배우기만 하고 생각하지 않으면 어둡고, 생각하기만 하고 배우지 않으면 위태롭다.', 'who': '공자 『논어』'},
            {'text': '아는 것을 안다 하고 모르는 것을 모른다 하는 것, 이것이 아는 것이다.', 'who': '공자 『논어』'},
            {'text': '세 사람이 길을 가면 그 가운데 반드시 나의 스승이 있다.', 'who': '공자 『논어』'},
            {'text': '천재는 1퍼센트의 영감과 99퍼센트의 땀으로 이루어진다.', 'who': '토머스 에디슨'},
            {'text': '배움은 그만둘 수 없다. 푸른색은 쪽에서 나왔지만 쪽보다 더 푸르다.', 'who': '순자 『권학』'},
            {'text': '남을 아는 사람은 지혜롭고, 스스로를 아는 사람은 밝다.', 'who': '노자 『도덕경』'},
            {'text': '큰 그릇은 늦게 이루어진다.', 'who': '노자 『도덕경』'},
            {'text': '나는 내가 아무것도 모른다는 것을 안다.', 'who': '소크라테스'},
            {'text': '가장 어두운 때는 해뜨기 직전이다.', 'who': '토머스 풀러'},
            {'text': '흐르는 물은 썩지 않는다.', 'who': '『여씨춘추』'}],
 'advice': [{'text': '그날 배운 내용을 먼저 복습하고, pandas와 시각화를 확실히 익힌 뒤 머신러닝과 생성형 AI로 넓혀 가세요. 진도보다 앞서 나가기보다 그날 배운 것을 '
                     '내 것으로 만드는 게 가장 중요해요.',
             'who': '10기 DX 재학생',
             'ask': '무엇부터 공부해야 하나요?'},
            {'text': '학습 속도가 빨라서 코드를 외우기보다 원리와 흐름을 이해하는 데 집중하는 편이 좋아요.',
             'who': '10기 DX 재학생',
             'ask': '무엇부터 공부해야 하나요?'},
            {'text': '정규 교육에 더해 하루 최소 1시간 복습을 권해요. 복습은 당일에 끝내세요. 하루라도 미루면 쌓여서 다음 진도를 따라가기 힘들어요.',
             'who': '10기 DX 재학생',
             'ask': '하루 공부 시간은 어느 정도가 적당한가요?'},
            {'text': '같은 강의를 반복해서 보기보다 간격을 두고 기억을 다시 꺼내 보는 방식이 효과적이에요.',
             'who': '10기 DX 재학생',
             'ask': '복습은 어떻게 하면 효과적인가요?'},
            {'text': '초반 2주는 모르는 게 당연하니 완벽히 이해하려 하기보다 실습 코드를 끝까지 실행하는 데 집중하세요.',
             'who': '10기 DX 재학생',
             'ask': '코딩 경험이 적은데 어떻게 따라가나요?'},
            {'text': '코드는 빈칸이 많아도 일단 내 방식대로 써 본 뒤, 답안과 어느 줄부터 달라지는지 비교해 보세요.',
             'who': '10기 DX 재학생',
             'ask': '코딩 경험이 적은데 어떻게 따라가나요?'},
            {'text': '질문할 때는 기대한 결과, 실제 결과, 오류 코드와 메시지를 함께 보여 주세요. 해결 기록을 남기면 같은 실수를 줄일 수 있어요.',
             'who': '10기 DX 재학생',
             'ask': '오류가 나거나 막히면 어떻게 하나요?'},
            {'text': '먼저 15분은 스스로 풀고, 막힌 지점만 구체적으로 물어보세요. 받은 코드는 반드시 실행해서 검증해야 해요.',
             'who': '10기 DX 재학생',
             'ask': '생성형 AI 는 학습에 어떻게 활용하나요?'},
            {'text': '의욕이 떨어지면 목표를 작게 줄여 30분 안에 끝낼 행동을 정해 보세요.',
             'who': '10기 DX 재학생',
             'ask': '수업을 놓치거나 의욕이 떨어지면 어떻게 하나요?'},
            {'text': '수식을 외우기보다 왜 이 모델을 골랐는지 말로 설명하는 연습이 더 효과적이었어요.',
             'who': '10기 DX 재학생',
             'ask': '수학이나 통계가 약해도 괜찮을까요?'},
            {'text': '발표 전날 한꺼번에 합치지 말고, 작은 단위로 자주 합치는 것이 핵심이에요.',
             'who': '10기 DX 재학생',
             'ask': '팀 프로젝트에서 어려웠던 점은 무엇이고 어떻게 해결하나요?'},
            {'text': '프로젝트가 많은 만큼 소통 능력이 정말 중요했어요.',
             'who': '10기 DX 재학생',
             'ask': '팀 프로젝트에서 어려웠던 점은 무엇이고 어떻게 해결하나요?'},
            {'text': '조원은 경쟁자가 아니라 동료예요. 모르는 것을 묻고 아는 것을 설명하면 둘 다 성장해요.',
             'who': '10기 DX 재학생',
             'ask': '후배에게 꼭 전하고 싶은 조언은 무엇인가요?'},
            {'text': '6개월은 장기전이니 생활 리듬을 지키고, 쉬는 시간에는 확실히 쉬세요.',
             'who': '10기 DX 재학생',
             'ask': '후배에게 꼭 전하고 싶은 조언은 무엇인가요?'},
            {'text': '포기한 가설까지 적어 두면 의사결정 과정을 설명하기 좋아요.', 'who': '10기 DX 재학생', 'ask': '프로젝트가 끝나면 무엇을 남기나요?'}]}



# ======================================================================
# 화면 구성
# ======================================================================
# 화면 구성: 사이드바, 홈, 대화, 학습방, 다이얼로그, 슬래시 명령어.
import copy
import hashlib
import html
import json
import random
import tempfile

import streamlit as st


esc = html.escape
PLACEHOLDER = "질문을 입력하세요 (/ 로 명령어 보기)"
SOURCE_OPTIONS = ["백서", "교안", "웹 검색"]
COMMANDS = [
    ("/커리큘럼", "우리 기수 커리큘럼 한눈에 보기", "account_tree"),
    ("/추천", "지금 물어볼 만한 질문 3개", "lightbulb"),
    ("/쿠키", "포춘쿠키 하나 열기", "cookie"),
    ("/계획", "백서 학습 전략으로 개인 학습 계획 짜기", "event_note"),
    ("/요약", "지금까지의 대화 요약", "summarize"),
    ("/새대화", "새 대화 시작", "add_comment"),
]
PLAN_ASK = "백서에 나온 학습 전략과 선배들의 공부 루틴을 바탕으로, 이번 주 개인 학습 계획을 요일별로 짜 주세요."


def spacer(px):
    st.html(f'<div style="height:{px}px"></div>')


def md(text):
    return (text or "").replace("$", "\\$")


# ================================================================ RAG 연결
@st.cache_data(show_spinner=False)
def _file_hash(path, mtime):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


@st.cache_resource(show_spinner=False)
def _load_whitepaper(file_hash, path):
    return rag_pipeline(path, collection_name="aivle_docs", with_retriever=True)


def whitepaper():
    """(chain, retriever). 업로드한 문서가 있으면 그것을, 없으면 기본 백서를 쓴다."""
    ss = st.session_state
    if ss.upload_chain is not None:
        return ss.upload_chain, ss.upload_retriever
    path = WHITEPAPER
    if path.exists():
        with st.spinner("문서를 읽고 벡터화하는 중이에요."):
            return _load_whitepaper(_file_hash(str(path), path.stat().st_mtime), str(path))
    # 단일 app.py 배포(Colab → GitHub): 저장소의 chroma_db 컬렉션을 그대로 사용
    if has_collection("aivle_docs"):
        return _load_saved_whitepaper()
    raise RuntimeError("백서가 아직 연결되지 않았어요. 입력창의 + 버튼으로 백서 PDF를 올려 주세요.")


@st.cache_resource(show_spinner=False)
def _load_saved_whitepaper():
    return load_collection("aivle_docs")


def note(title, body):
    return {"role": "assistant", "note_title": title, "note": body}


NO_KEY = (
    "OpenAI API 키가 없어요",
    "환경 변수 OPENAI_API_KEY, Streamlit secrets, 또는 프로젝트 폴더의 api_key.txt 에 키를 넣으면 "
    "쿠키 선배가 백서를 읽고 답해 드려요. 지금은 화면만 둘러볼 수 있어요.",
)


def not_ready_note():
    if IMPORT_ERROR:
        return note("RAG 패키지를 불러오지 못했어요", "requirements.txt 의 패키지를 설치해 주세요. (" + IMPORT_ERROR[:160] + ")")
    return note(*NO_KEY)


def history_text(msgs, limit=6):
    lines = []
    for m in msgs[-limit:]:
        if m["role"] == "user":
            lines.append("후배: " + m.get("ask", m["text"]))
        elif m.get("answer"):
            lines.append("선배: " + m["answer"][:400])
    return "\n".join(lines)


def generate(msgs):
    """마지막 사용자 메시지에 대한 답변을 만들어 msgs 에 붙인다."""
    ss = st.session_state
    last = msgs[-1]
    question = last.get("ask", last["text"])
    if not ready():
        msgs.append(not_ready_note())
        return
    try:
        hist = history_text(msgs[:-1])
        if last.get("cmd") == "summary":
            with st.spinner("대화를 요약하는 중이에요."):
                text = summarize(history_text(msgs[:-1], limit=20))
            msgs.append({"role": "assistant", "answer": text})
        elif ss.view == "room":
            rid = ss.current_room
            _, _, item = find_item(rid)
            sources = ss.get("src_" + rid) or []
            wp_ret = None
            if "백서" in sources:
                wp_ret = whitepaper()[1]
            with st.spinner("쿠키 선배가 자료를 찾아보는 중이에요."):
                msgs.append(room_answer(question, item["name"], sources, wp_ret,
                                            ss.room_retrievers.get(rid), hist))
        else:
            chain, _ = whitepaper()
            with st.spinner("쿠키 선배가 백서를 찾아보는 중이에요."):
                result = chain.invoke({"input": question, "history": hist})
            msgs.append(to_message(result, "백서"))
    except Exception as e:
        msgs.append(note("답변을 만들다가 문제가 생겼어요", "잠시 뒤 다시 시도해 주세요. (" + str(e)[:200] + ")"))


def attach(file):
    """첨부 PDF: 대화에서는 백서를 대체하고, 학습방에서는 그 방의 교안이 된다."""
    ss = st.session_state
    in_room = ss.view == "room" and ss.current_room
    msgs = current_messages(create_title=file.name)
    if not ready():
        msgs.append(not_ready_note())
        return
    current_name = room(ss.current_room)["doc_name"] if in_room else ss.doc_name
    if file.name == current_name:
        return  # 같은 문서는 다시 벡터화하지 않는다
    try:
        with st.spinner("문서를 읽고 벡터화하는 중이에요."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.getvalue())
            if in_room:
                rid = ss.current_room
                _, retriever = rag_pipeline(tmp.name, collection_name="room_" + rid, with_retriever=True)
                ss.room_retrievers[rid] = retriever
                room(rid)["doc_name"] = file.name
                msgs.append(note("교안을 연결했어요", "「" + file.name + "」 을 이 학습방의 교안으로 읽었어요."))
            else:
                chain, retriever = rag_pipeline(tmp.name, collection_name="aivle_upload", with_retriever=True)
                ss.upload_chain, ss.upload_retriever = chain, retriever
                ss.doc_name = file.name
                msgs.append(note("문서를 연결했어요", "이제부터 「" + file.name + "」 을 근거로 답해요."))
    except Exception as e:
        msgs.append(note("문서를 읽지 못했어요", str(e)[:200]))


# ================================================================ 슬래시 명령어
def run_command(text):
    ss = st.session_state
    cmd = text.strip().split()[0]
    if cmd == "/새대화":
        go_home()
        return
    if cmd == "/쿠키":
        new_fortune()
        ss.open_fortune = True
        return
    msgs = current_messages(create_title="명령어 " + cmd)
    if cmd == "/계획":
        msgs.append({"role": "user", "text": "/계획", "ask": PLAN_ASK})
    elif cmd == "/요약":
        if any(m.get("answer") for m in msgs):
            msgs.append({"role": "user", "text": "/요약", "cmd": "summary"})
        else:
            msgs.append({"role": "user", "text": "/요약"})
            msgs.append(note("아직 요약할 대화가 없어요", "먼저 궁금한 것을 물어봐 주세요."))
    elif cmd == "/커리큘럼":
        msgs.append({"role": "user", "text": cmd})
        msgs.append({"role": "assistant", "card": "curriculum"})
    elif cmd == "/추천":
        pool = [q["q"] for c in categories() for q in c["questions"]]
        msgs.append({"role": "user", "text": cmd})
        msgs.append({"role": "assistant", "card": "recommend", "qs": random.sample(pool, min(3, len(pool)))})
    else:
        msgs.append({"role": "user", "text": text})
        msgs.append({"role": "assistant", "card": "help", "unknown": cmd not in ("/", "/도움말")})


def handle_input(value):
    if not value:
        return
    if isinstance(value, str):
        text, files = value.strip(), []
    else:
        text, files = (value.text or "").strip(), list(value.files or [])
    if files:
        attach(files[0])
    if text.startswith("/"):
        run_command(text)
    elif text:
        send(text)
    st.rerun()


def chat_input(key):
    handle_input(st.chat_input(placeholder=PLACEHOLDER, accept_file=True, file_type=["pdf"], key=key))


# ================================================================ 다이얼로그
@st.dialog("오늘의 포춘쿠키")
def fortune_dialog():
    f = st.session_state.fortune
    st.html(
        '<div class="ck-fortune">' + mascot_img(96)
        + '<div class="ck-slip"><div class="ck-slip-q">' + esc(f["quote"]["text"]) + "</div>"
        + '<div class="ck-slip-w">' + esc(f["quote"]["who"]) + "</div></div>"
        + '<div class="ck-box quote ck-adv"><b>선배의 조언 (' + esc(f["advice"]["who"]) + ")</b>"
        + esc(f["advice"]["text"]) + "</div></div>"
    )
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        st.button("쿠키 하나 더", key="fc_more", on_click=new_fortune)
        if st.button("이 조언으로 더 물어보기", key="fc_ask", type="primary"):
            send(f["advice"]["ask"])
            st.rerun()


@st.dialog("대화를 삭제할까요?")
def delete_dialog(cid):
    ss = st.session_state
    title = ss.chats.get(cid, {}).get("title", "")
    st.write("「" + title + "」 대화가 목록에서 사라져요.")
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        if st.button("취소", key="dd_cancel"):
            st.rerun()
        if st.button("삭제", key="dd_ok", type="primary"):
            ss.chats.pop(cid, None)
            if ss.current_chat == cid:
                go_home()
            st.rerun()


# ---- 학습방 편집 콜백
def _draft():
    return st.session_state.cur_draft


def _draft_step(sid):
    for s in _draft()["steps"]:
        if s["id"] == sid:
            return s
    return None


def _clear_edit_keys():
    for k in list(st.session_state.keys()):
        if isinstance(k, str) and k.startswith("ed_"):
            del st.session_state[k]


def _ed_add_step():
    sid = "s" + new_id()
    _draft()["steps"].append({"id": sid, "name": "새 STEP", "items": []})
    st.session_state.ed_step = sid


def _ed_del_step(sid):
    d = _draft()
    d["steps"] = [s for s in d["steps"] if s["id"] != sid]
    st.session_state.ed_step = d["steps"][0]["id"]


def _ed_add_item(sid):
    _draft_step(sid)["items"].append({"id": "i" + new_id(), "name": "새 항목", "type": "learn"})


def _ed_del_item(sid, iid):
    step = _draft_step(sid)
    step["items"] = [i for i in step["items"] if i["id"] != iid]


def _ed_move(sid, iid, delta):
    items = _draft_step(sid)["items"]
    idx = next(n for n, i in enumerate(items) if i["id"] == iid)
    new = idx + delta
    if 0 <= new < len(items):
        items[idx], items[new] = items[new], items[idx]


def _ed_current(iid):
    on = st.session_state.get("ed_cur_" + iid, False)
    for s in _draft()["steps"]:
        for i in s["items"]:
            i["current"] = bool(on and i["id"] == iid)
            if i["id"] != iid and ("ed_cur_" + i["id"]) in st.session_state:
                st.session_state["ed_cur_" + i["id"]] = False


def _ed_reset():
    _clear_edit_keys()
    st.session_state.cur_draft = copy.deepcopy(DEFAULT_CURRICULUM)


def open_curriculum_dialog():
    _clear_edit_keys()
    st.session_state.cur_draft = copy.deepcopy(st.session_state.curriculum)
    curriculum_dialog()


@st.dialog("학습방 편집", width="large")
def curriculum_dialog():
    ss = st.session_state
    d = _draft()
    ids = [s["id"] for s in d["steps"]]
    if ss.get("ed_step") not in ids:
        ss.ed_step = ids[0]
    st.caption("기수와 트랙마다 커리큘럼이 달라요. 우리 반에 맞게 고쳐 쓰세요.")
    d["cohort"] = st.text_input("기수와 트랙", value=d.get("cohort", ""), key="ed_cohort")
    with st.container(horizontal=True, vertical_alignment="center", gap="small"):
        st.segmented_control("STEP", ids, format_func=lambda i: "STEP " + str(ids.index(i) + 1),
                             key="ed_step", label_visibility="collapsed")
        st.button("STEP 추가", icon=":material/add:", key="ed_add_step", on_click=_ed_add_step)
    sid = ss.get("ed_step") or ids[0]
    step = _draft_step(sid)
    step["name"] = st.text_input("STEP 이름", value=step["name"], key="ed_sname_" + sid)

    types = ["learn", "project"]
    for item in step["items"]:
        iid = item["id"]
        with st.container(key="edrow_" + iid):
            c = st.columns([0.55, 0.55, 1.9, 3.6, 1.0, 0.55], vertical_alignment="center", gap="small")
            c[0].button("↑", key="ed_up_" + iid, on_click=_ed_move, args=(sid, iid, -1), width="stretch")
            c[1].button("↓", key="ed_dn_" + iid, on_click=_ed_move, args=(sid, iid, 1), width="stretch")
            item["type"] = c[2].selectbox(
                "유형", types, index=types.index(item.get("type", "learn")), key="ed_type_" + iid,
                format_func=lambda t: "학습" if t == "learn" else "미니프로젝트", label_visibility="collapsed")
            item["name"] = c[3].text_input("이름", value=item["name"], key="ed_name_" + iid,
                                           label_visibility="collapsed")
            c[4].checkbox("지금", value=bool(item.get("current")), key="ed_cur_" + iid,
                          on_change=_ed_current, args=(iid,))
            c[5].button("×", key="ed_del_" + iid, on_click=_ed_del_item, args=(sid, iid), width="stretch")
    if not step["items"]:
        st.caption("아직 항목이 없어요.")
    with st.container(horizontal=True, gap="small"):
        st.button("항목 추가", icon=":material/add:", key="ed_add_item", on_click=_ed_add_item, args=(sid,))
        if len(ids) > 1:
            st.button("이 STEP 삭제", icon=":material/delete:", key="ed_del_step", on_click=_ed_del_step, args=(sid,))

    spacer(4)
    foot = st.columns([1, 1], vertical_alignment="center")
    with foot[0]:
        st.button("기본값으로 되돌리기", icon=":material/restart_alt:", key="ed_reset", on_click=_ed_reset)
    with foot[1]:
        with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
            if st.button("취소", key="ed_cancel"):
                st.rerun()
            if st.button("저장", key="ed_save", type="primary"):
                for s in d["steps"]:
                    for i in s["items"]:
                        if not i.get("current"):
                            i.pop("current", None)
                ss.curriculum = copy.deepcopy(d)
                for s in d["steps"]:
                    ss.step_open.setdefault(s["id"], False)
                try:
                    with open(CURRICULUM_FILE, "w", encoding="utf-8") as f:
                        json.dump(d, f, ensure_ascii=False, indent=1)
                except Exception:
                    pass  # Community Cloud 등 쓰기 불가 환경에서는 세션에만 저장
                if ss.current_room and not find_item(ss.current_room):
                    go_home()
                st.rerun()


# ================================================================ 사이드바
def render_sidebar():
    ss = st.session_state
    with st.sidebar:
        st.button("**AIVLE** 학습 도우미", key="logo_home", on_click=go_home, width="stretch")

        # 대화
        with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center",
                          key="sbhead_chat"):
            st.markdown("대화", width="content")
            st.button("새 대화", icon=":material/add:", key="new_chat", on_click=go_home)
        chats = sorted(ss.chats.items(), key=lambda kv: kv[1]["created"], reverse=True)
        if not chats:
            st.caption("아직 대화가 없어요. 궁금한 걸 물어보세요.")
        with st.container(key="sblist_chat"):
            for cid, chat in chats:
                with st.container(key="chatrow_" + cid):
                    current = ss.view == "chat" and ss.current_chat == cid
                    st.button(chat["title"], key="chat_" + cid, icon=":material/chat_bubble:",
                              type="primary" if current else "secondary", width="stretch",
                              on_click=open_chat, args=(cid,))
                    if st.button("×", key="del_chat_" + cid):
                        delete_dialog(cid)

        # 학습방
        with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center",
                          key="sbhead_room"):
            st.markdown("학습방", width="content")
            edit = st.button("편집", icon=":material/edit:", key="edit_curr")
        st.caption(ss.curriculum.get("cohort", ""))
        with st.container(key="sblist_step"):
            for n, step in enumerate(ss.curriculum["steps"], 1):
                sid = step["id"]
                is_open = ss.step_open.get(sid, False)
                st.button(":violet[STEP " + str(n) + "] " + step["name"],
                          key=("stepo_" if is_open else "stepc_") + sid, width="stretch",
                          on_click=toggle_step, args=(sid,))
                if is_open:
                    with st.container(key="stepitems_" + sid):
                        for item in step["items"]:
                            project = item.get("type") == "project"
                            label = item["name"]
                            if item.get("current"):
                                label += " :orange[지금]"
                            current = ss.view == "room" and ss.current_room == item["id"]
                            st.button(label, key=("roomp_" if project else "rooml_") + item["id"],
                                      icon=":material/flag:" if project else ":material/menu_book:",
                                      type="primary" if current else "secondary", width="stretch",
                                      on_click=open_room, args=(item["id"],))

        st.html(
            '<div class="ck-doc"><span class="ck-doc-dot"></span><div style="min-width:0">'
            '<div class="ck-doc-name">' + esc(ss.doc_name) + '</div>'
            '<div class="ck-doc-sub">연결됨, 답변의 근거 문서</div></div></div>'
        )
    if edit:
        open_curriculum_dialog()


# ================================================================ 메시지 렌더링
def _chip_class(kind):
    return {"백서": "k-wp", "교안": "k-lec", "웹": "k-web"}.get(kind, "")


ICON_QUOTE = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
              'stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/>'
              '<path d="M15 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/></svg>')
ICON_FLAG = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
             'stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/>'
             '<path d="M4 22v-7"/></svg>')


def _tidy_answer(text):
    """목록 항목의 '**제목** — 설명' / '**제목**: 설명' 을 '제목(굵게) 줄바꿈 설명' 으로 정리."""
    import re
    return re.sub(r"^(\s*(?:\d+\.|[-*])\s+\*\*[^*\n]+\*\*)\s*(?:—|–|-|:)\s*", r"\1  \n", text or "", flags=re.M)


def render_sources(sources):
    seen, chips = set(), []
    for s in sources:
        if s["label"] in seen:
            continue
        seen.add(s["label"])
        cls = "ck-src " + _chip_class(s["kind"])
        if s.get("url"):
            chips.append('<a class="' + cls + '" href="' + esc(s["url"], quote=True) + '" target="_blank">'
                         + esc(s["label"]) + "</a>")
        else:
            chips.append('<span class="' + cls + '">' + esc(s["label"]) + "</span>")
    st.html('<div class="ck-srcs"><span class="ck-src-lbl">근거</span>' + "".join(chips) + "</div>")
    with st.expander("근거 문단 보기"):
        for s in sources:
            st.markdown("**" + md(s["label"]) + "**")
            st.caption(md(s["snippet"]))


def curriculum_html():
    cur = st.session_state.curriculum
    parts = ['<div class="ck-label">' + esc(cur.get("cohort", "")) + "</div>"]
    for n, step in enumerate(cur["steps"], 1):
        parts.append('<div class="ck-curr-step">STEP ' + str(n) + " " + esc(step["name"]) + "</div>")
        parts.append('<div class="ck-curr-items">')
        for it in step["items"]:
            cls = ("p" if it.get("type") == "project" else "") + (" cur" if it.get("current") else "")
            parts.append('<span class="' + cls.strip() + '">' + esc(it["name"]) + "</span>")
        parts.append("</div>")
    return "".join(parts)


def render_assistant(m, key, is_last):
    with st.container(key="card_msg_" + key):
        st.html('<div class="ck-head">' + mascot_img(34) + '<span class="ck-name">쿠키 선배</span></div>')
        card = m.get("card")
        if card == "help":
            if m.get("unknown"):
                st.markdown("그런 명령어는 없어요. 아래에서 골라 보세요.")
            else:
                st.markdown("이런 명령어를 쓸 수 있어요.")
            for n, (cmd, desc, icon) in enumerate(COMMANDS):
                st.button(cmd + " — " + desc, key="cmd_" + key + "_" + str(n), icon=":material/" + icon + ":",
                          width="stretch", on_click=run_command, args=(cmd,))
        elif card == "curriculum":
            st.html(curriculum_html())
            st.caption("사이드바의 학습방에서 항목을 누르면 그 주제만 깊게 물어볼 수 있어요.")
        elif card == "recommend":
            st.markdown("지금 이런 걸 물어보면 좋아요.")
            for n, q in enumerate(m.get("qs", [])):
                st.button(q, key="cmd_" + key + "_r" + str(n), icon=":material/lightbulb:", width="stretch",
                          on_click=send, args=(q,))
        elif m.get("note"):
            st.html('<div class="ck-box note"><b>' + esc(m.get("note_title", "안내")) + "</b>" + esc(m["note"]) + "</div>")
        else:
            st.markdown(md(_tidy_answer(m.get("answer", ""))))
            rows = []
            if m.get("quote"):
                rows.append('<div class="ck-row"><span class="ck-ic q">' + ICON_QUOTE + '</span><div><b>선배 한마디</b><p>'
                            + esc(m["quote"]) + "</p></div></div>")
            if m.get("challenge"):
                rows.append('<div class="ck-row"><span class="ck-ic t">' + ICON_FLAG + '</span><div><b>오늘 해 볼 것</b><p>'
                            + esc(m["challenge"]) + "</p></div></div>")
            if rows:
                st.html('<div class="ck-extra">' + "".join(rows) + "</div>")
            if m.get("sources"):
                render_sources(m["sources"])
            if is_last and m.get("followups"):
                st.html('<div class="ck-label">이어서 물어보기</div>')
                for n, q in enumerate(m["followups"][:3]):
                    st.button(q, key="fu_" + key + "_" + str(n), icon=":material/subdirectory_arrow_right:",
                              width="stretch", on_click=send, args=(q,))


def render_messages(msgs, scope):
    for n, m in enumerate(msgs):
        if m["role"] == "user":
            st.html('<div class="ck-user"><div>' + esc(m["text"]) + "</div></div>")
        else:
            render_assistant(m, scope + "_" + str(n), n == len(msgs) - 1)
    if msgs and msgs[-1]["role"] == "user":
        generate(msgs)
        st.rerun()


def float_cookie():
    with st.container(key="float_wrap"):
        if st.button("콕!", key="float_cookie"):
            new_fortune()
            st.session_state.open_fortune = True


# ================================================================ 홈
def render_home():
    ss = st.session_state
    st.html(
        '<div class="ck-hero"><div class="ck-hero-txt">'
        '<div class="ck-hero-small">선배들의 경험이 다 들어 있어요!</div>'
        '<div class="ck-hero-big">오늘은 뭐가 궁금해요?</div>'
        '<div class="ck-hero-sub">AIVLE School 백서에서 찾아, 쿠키 선배가 바로 알려 드려요.</div></div>'
        '<div class="ck-hero-art"><span class="ck-bubble b1"># 공부 루틴</span>'
        '<span class="ck-bubble b2"># 미니프로젝트 꿀팁</span>' + mascot_img(170) + "</div></div>"
    )
    spacer(6)
    cats = categories()
    cols = st.columns(len(cats), gap="small")
    for n, cat in enumerate(cats):
        with cols[n]:
            with st.container(key="cattile_" + str(n)):
                st.button(cat["label"], key="catbtn_" + cat["id"], icon=":material/" + cat["icon"] + ":",
                          type="primary" if ss.cat == cat["id"] else "secondary", width="stretch",
                          on_click=select_cat, args=(cat["id"],))
    spacer(2)
    selected = next((c for c in cats if c["id"] == ss.cat), cats[0])
    qs = selected["questions"]
    for row in range(0, len(qs), 2):
        cols = st.columns(2, gap="medium")
        for k, q in enumerate(qs[row:row + 2]):
            with cols[k]:
                st.button(":violet[" + q.get("tag", "질문") + "] " + q["q"],
                          key="qcard_" + selected["id"] + "_" + str(row + k), width="stretch",
                          on_click=start_chat, args=(q["q"],))
    chat_input("input_home")


# ================================================================ 대화
def render_chat():
    ss = st.session_state
    chat = ss.chats.get(ss.current_chat)
    if chat is None:
        go_home()
        st.rerun()
    st.html(
        '<div class="ck-chat-head"><div class="ck-title">' + esc(chat["title"]) + "</div>"
        '<span class="ck-chip"><i></i>' + ("백서 연결됨" if ss.doc_name == WHITEPAPER.name else esc(ss.doc_name) + " 연결됨")
        + "</span></div>"
    )
    float_cookie()
    render_messages(chat["messages"], "c" + ss.current_chat)
    chat_input("input_chat")


# ================================================================ 학습방
def starters(item):
    name = item["name"]
    if item.get("type") == "project":
        return [name + " 는 어떻게 진행되나요?", "팀 역할은 어떻게 나누면 좋을까요?", "발표 준비 꿀팁을 알려 주세요"]
    return [name + " 는 무엇부터 공부하면 좋을까요?", name + " 에서 자주 막히는 부분을 알려 주세요",
            name + " 복습 루틴을 추천해 주세요"]


def render_room():
    ss = st.session_state
    found = find_item(ss.current_room)
    if not found:
        go_home()
        st.rerun()
    step, step_no, item = found
    rid = item["id"]
    r = room(rid)
    project = item.get("type") == "project"
    desc = ("팀 프로젝트를 하면서 막히는 것을 백서, 교안, 웹에서 함께 찾아봐요." if project
            else "이 과목을 배우는 동안 궁금한 것을 백서, 교안, 웹에서 함께 찾아봐요.")
    with st.container(key="card_roomhead"):
        st.html(
            '<div class="ck-crumb">STEP ' + str(step_no) + " " + esc(step["name"]) + "</div>"
            '<div class="ck-room-title"><span class="ck-title">' + esc(item["name"]) + "</span>"
            + ('<span class="ck-now">지금</span>' if item.get("current") else "") + "</div>"
            '<div class="ck-desc">' + desc + "</div>"
        )
        st.pills("답변 자료", SOURCE_OPTIONS, selection_mode="multi", default=SOURCE_OPTIONS, key="src_" + rid)
        if r["doc_name"]:
            st.caption("교안: " + r["doc_name"])
        else:
            st.caption("교안 PDF 를 입력창에 첨부하면 이 방의 교안으로 연결돼요.")
    float_cookie()
    if not r["messages"]:
        st.html('<div class="ck-label">이런 것부터 물어보세요</div>')
        for n, q in enumerate(starters(item)):
            st.button(q, key="fu_start_" + rid + "_" + str(n), icon=":material/subdirectory_arrow_right:",
                      width="stretch", on_click=send, args=(q,))
    render_messages(r["messages"], "r" + rid)
    chat_input("input_room")


def finish():
    """한 번의 실행에 다이얼로그는 하나만: 포춘쿠키는 맨 끝에서 연다."""
    if st.session_state.pop("open_fortune", False):
        fortune_dialog()



# ======================================================================
# 앱 실행
# ======================================================================
# AIVLE School 학습 도우미 — 진입점 (실행: streamlit run app.py).
import streamlit as st


st.set_page_config(page_title="AIVLE School 학습 도우미", page_icon=":material/cookie:",
                   layout="centered", initial_sidebar_state="auto")
inject_css()
init_state()
render_sidebar()

view = st.session_state.view
if view == "chat":
    render_chat()
elif view == "room":
    render_room()
else:
    render_home()

# 데모 전용: ?demo=1&dlg=fortune|edit 로 다이얼로그를 바로 연다 (발표/화면 점검용)
dlg = st.query_params.get("dlg")
if st.query_params.get("demo") == "1" and dlg and not st.session_state.get("_dlg_done"):
    st.session_state._dlg_done = True
    if dlg == "edit":
        open_curriculum_dialog()
    else:
        st.session_state.open_fortune = True
finish()
