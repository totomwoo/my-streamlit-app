
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


def line_icon(paths: str, color: str, size: int = 16) -> str:
    """선 아이콘을 <img> 로 반환. st.html 은 인라인 <svg> 를 지우므로 data-URI 로 넣고 선 색을 미리 굽는다."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="'
        + color + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + paths + "</svg>"
    )
    return (
        '<img src="data:image/svg+xml,' + quote(svg) + '" width="' + str(size) + '" height="' + str(size)
        + '" alt="" draggable="false"/>'
    )


# 답변 카드 / 교안 박스 / 편집 행에서 쓰는 아이콘 (색은 ui_css 의 :root 토큰 값과 같게 유지)
ICON_QUOTE = line_icon(
    '<path d="M3 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/>'
    '<path d="M15 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/>',
    "#B45309")  # --cookie-deep
ICON_FLAG = line_icon(
    '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><path d="M4 22v-7"/>',
    "#5B4BE0")  # --primary
ICON_FILE = line_icon(
    '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'
    '<path d="M9 13h6"/><path d="M9 17h4"/>',
    "#5B4BE0", 18)  # --primary
ICON_FILE_OFF = line_icon(
    '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>',
    "#94A3B8", 18)  # --muted
ICON_GRIP = line_icon(
    '<circle cx="9" cy="6" r="1"/><circle cx="15" cy="6" r="1"/><circle cx="9" cy="12" r="1"/>'
    '<circle cx="15" cy="12" r="1"/><circle cx="9" cy="18" r="1"/><circle cx="15" cy="18" r="1"/>',
    "#94A3B8", 18)  # --muted



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
  --activity:#0E7C86; --activity-soft:#DDF3F4;
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
/* stTextInputRootElement / stChatInput 안쪽 상자 / [data-baseweb="select"] 의 포커스 테두리 (DOM 확인): 기본 테마 빨강 대신 primary */
[data-testid="stTextInputRootElement"]:focus-within{border-color:var(--primary)!important;}
[data-testid="stChatInput"] div:focus-within{border-color:var(--primary)!important;}
[data-baseweb="select"] > div:focus-within{border-color:var(--primary)!important;}

/* role="dialog": 다이얼로그 모서리/배경 */
div[role="dialog"]{border-radius:var(--radius-lg);background:var(--surface);}

/* ============ 사이드바 ============ */
/* stSidebar: 흰 배경 + 오른쪽 경계선 */
[data-testid="stSidebar"]{background:var(--surface);border-right:1px solid var(--border);}
/* stSidebar 버튼 공통: 메뉴형(왼쪽 정렬, 테두리 없음) */
[data-testid="stSidebar"] button[kind="secondary"], [data-testid="stSidebar"] button[kind="primary"]{
  border:none;background:transparent;color:var(--text);min-height:36px;padding:6px 10px;
  border-radius:var(--radius-sm);font-weight:500;box-shadow:none;justify-content:flex-start;}
[data-testid="stSidebar"] button[kind="secondary"]:hover{background-color:var(--bg);color:var(--text);}
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
/* hover: 배경색만 바꾼다 (background 축약형을 쓰면 마스코트 배경 이미지가 지워진다) */
[data-testid="stSidebar"] .st-key-logo_home button:hover, [data-testid="stSidebar"] .st-key-logo_home button:active,
[data-testid="stSidebar"] .st-key-logo_home button:focus{background-color:var(--bg);
  background-image:url("__MASCOT__");background-repeat:no-repeat;background-position:4px center;background-size:40px auto;}
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
/* st-key-stepitems_*: 아코디언 패널 (세로선 없이 들여쓰기만, 고른 간격, 페이드인) */
[data-testid="stSidebar"] [class*="st-key-stepitems_"]{margin-left:8px;width:calc(100% - 8px)!important;
  gap:2px;padding-bottom:4px;animation:ckFade .18s ease-out;}
@keyframes ckFade{from{opacity:0;transform:translateY(-4px);}to{opacity:1;transform:none;}}
[data-testid="stSidebar"] [class*="st-key-stepitems_"] button{min-height:32px;padding:4px 10px;}
[data-testid="stSidebar"] [class*="st-key-stepitems_"] button [data-testid="stMarkdownContainer"] p{font-size:13.5px;}
/* st-key-rooml_* (학습) / roomp_* (미니프로젝트) / rooma_* (활동): 항목 아이콘은 작고 옅게, 유형별 색 */
[data-testid="stSidebar"] [class*="st-key-stepitems_"] [data-testid="stIconMaterial"]{font-size:16px;opacity:.7;
  margin-right:2px;}
[data-testid="stSidebar"] [class*="st-key-roomp_"] [data-testid="stIconMaterial"]{color:var(--project);}
[data-testid="stSidebar"] [class*="st-key-rooma_"] [data-testid="stIconMaterial"]{color:var(--activity);}
/* st-key-rooml_* / roomp_* 의 '지금' 배지 */
[data-testid="stSidebar"] [class*="st-key-stepitems_"] p > span{background:var(--cookie-soft)!important;
  color:var(--cookie-deep)!important;font-size:10.5px;font-weight:800;padding:2px 7px;border-radius:999px;margin-left:4px;}

/* stSidebarContent > stSidebarUserContent > div > stVerticalBlock (DOM 확인): 세로 flex 로 늘려 카드를 맨 아래로 민다 */
[data-testid="stSidebarContent"]{display:flex;flex-direction:column;}
[data-testid="stSidebarUserContent"]{flex:1 0 auto;display:flex;flex-direction:column;padding-bottom:0;}
[data-testid="stSidebarUserContent"] > div{flex:1 0 auto;display:flex;flex-direction:column;}
[data-testid="stSidebarUserContent"] > div > [data-testid="stVerticalBlock"]{flex:1 0 auto;}
/* st-key-sbdoc 을 감싼 stLayoutWrapper (DOM 확인): 사이드바 스크롤 영역 바닥에 고정, 배경으로 아래 내용을 가린다 */
[data-testid="stSidebar"] [data-testid="stLayoutWrapper"]:has(> .st-key-sbdoc){position:sticky;bottom:0;margin-top:auto;
  z-index:2;background:var(--surface);padding:10px 0 14px;border-top:1px solid var(--border);}
/* ck-doc: 사이드바 하단 연결 문서 카드 (st.html) */
.ck-doc{display:flex;align-items:center;gap:10px;padding:12px 14px;background:var(--bg);
  border:1px solid var(--border);border-radius:var(--radius-md);}
.ck-doc-dot{width:8px;height:8px;border-radius:50%;background:var(--ic-2);flex:none;}
.ck-doc-name{font-size:12.5px;font-weight:700;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.ck-doc-sub{font-size:11.5px;color:var(--text-sub);}

/* ============ 홈 ============ */
/* ck-hero: 히어로 (왼쪽 문구 + 오른쪽 마스코트) */
.ck-hero{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:4px 4px 0;}
.ck-hero-txt{flex:1 1 300px;}
.ck-hero-small{font-size:14px;color:var(--text-sub);font-weight:500;margin-bottom:6px;}
.ck-hero-big{font-size:36px;font-weight:800;color:var(--text);letter-spacing:-1px;line-height:1.25;}
.ck-hero-sub{font-size:15px;color:var(--text-sub);margin-top:10px;}
.ck-hero-art{flex:0 0 200px;display:flex;justify-content:center;align-items:flex-end;}
.ck-hero-art img{display:block;}

/* st-key-cattile_*: 카테고리 타일 (파스텔 아이콘 사각형 + 라벨, 선택 = 2px primary 테두리) */
[class*="st-key-cattile_"] button{flex-direction:column;gap:14px;min-height:112px;padding:16px 6px 14px;
  background:var(--surface);border:2px solid transparent;border-radius:var(--radius-lg);box-shadow:var(--shadow);
  color:var(--text);font-weight:700;}
[class*="st-key-cattile_"] button > div, [class*="st-key-cattile_"] button > div > span{display:flex;
  flex-direction:column;align-items:center;gap:14px;}
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
/* stButtonGroup button[data-variant="pills"|"segmented_control"], 선택 = [data-selected="true"]
   (Streamlit 1.64 실제 DOM 에서 확인. kind="pillsActive" 는 더 이상 붙지 않는다)
   config.toml 없이 app.py 하나로 배포해도 기본 테마의 빨강 대신 토큰 색을 쓴다 */
[data-testid="stButtonGroup"] button[data-variant]{background:var(--surface)!important;
  border-color:var(--border)!important;color:var(--text-sub)!important;}
[data-testid="stButtonGroup"] button[data-variant]:hover{border-color:var(--primary)!important;
  color:var(--primary)!important;}
[data-testid="stButtonGroup"] button[data-variant][data-selected="true"]{background:var(--primary-soft)!important;
  border-color:var(--primary)!important;color:var(--primary-hover)!important;}
[data-testid="stButtonGroup"] button[data-variant]:focus-visible{outline:2px solid var(--primary)!important;
  box-shadow:none!important;}
[data-testid="stButtonGroup"] button[data-variant] [data-testid="stMarkdownContainer"] p{color:inherit;}
/* ck-extra: 선배 한마디 / 오늘 해 볼 것 (색 박스 대신 구분선 + 아이콘 줄) */
.ck-extra{border-top:1px solid var(--border);padding-top:14px;display:flex;flex-direction:column;gap:12px;}
.ck-row{display:flex;gap:12px;align-items:flex-start;}
.ck-ic{flex:none;width:28px;height:28px;border-radius:9px;display:flex;align-items:center;justify-content:center;}
.ck-ic.q{background:var(--cookie-soft);}
.ck-ic.t{background:var(--primary-soft);}
.ck-ic img{display:block;width:16px;height:16px;}
.ck-row b{display:block;font-size:12px;font-weight:700;color:var(--text-sub);margin-bottom:2px;}
.ck-row p{margin:0;font-size:14.5px;line-height:1.65;color:var(--text);}
/* ck-srcs: 출처 (배경 없는 작은 회색 글자) */
.ck-srcs{display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;}
.ck-src-lbl{font-size:12.5px;font-weight:700;color:var(--text-sub);}
.ck-src{font-size:12.5px;font-weight:500;color:var(--text-sub);background:none;border:none;padding:0;text-decoration:none;}
a.ck-src:hover{color:var(--primary);text-decoration:underline;}
/* st-key-card_msg_*: 답변 카드 안 목록(굵은 제목 + 회색 설명) */
[class*="st-key-card_msg_"] li:has(strong){color:var(--text-sub);}
[class*="st-key-card_msg_"] li strong{color:var(--text);}
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
/* st-key-fu_* 의 stIconMaterial: 앞 아이콘과 질문 글자 사이를 넓게 */
[class*="st-key-fu_"] button [data-testid="stIconMaterial"]{margin-right:10px;}

/* ck-room: 학습방 헤더 */
/* st-key-card_roomhead: 헤더 카드 안 간격 */
.st-key-card_roomhead{gap:8px;}
/* st-key-roomkind_l|p|a: 유형 아이콘 + 유형 이름 + STEP 경로 (markdown 안 아이콘은 span[role="img"], DOM 확인) */
[class*="st-key-roomkind_"] [data-testid="stMarkdownContainer"] p{display:flex;align-items:center;gap:6px;
  font-size:12.5px;font-weight:600;color:var(--text-sub);margin:0;}
[class*="st-key-roomkind_"] [data-testid="stMarkdownContainer"] p span[role="img"]{font-size:17px;color:var(--primary);}
[class*="st-key-roomkind_"] [data-testid="stMarkdownContainer"] p strong{color:var(--primary);font-weight:800;}
.st-key-roomkind_p [data-testid="stMarkdownContainer"] p span[role="img"],
.st-key-roomkind_p [data-testid="stMarkdownContainer"] p strong{color:var(--project);}
.st-key-roomkind_a [data-testid="stMarkdownContainer"] p span[role="img"],
.st-key-roomkind_a [data-testid="stMarkdownContainer"] p strong{color:var(--activity);}
/* st-key-roomsrc: 답변 자료 (작은 라벨 + 작은 칩 한 줄) */
.st-key-roomsrc{margin-top:2px;}
.st-key-roomsrc [data-testid="stMarkdownContainer"] p{font-size:12px;font-weight:700;color:var(--text-sub);}
.st-key-roomsrc button[data-variant="pills"]{min-height:26px;padding:2px 11px;border-radius:999px;}
.st-key-roomsrc button[data-variant="pills"] [data-testid="stMarkdownContainer"] p{color:inherit;font-weight:600;}
/* st-key-roomdoc: 교안 박스 (파일 아이콘 + 이름 + 연결됨, 아래에 PDF 올리기) */
.st-key-roomdoc{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  box-shadow:var(--shadow);padding:16px 22px;gap:8px;}
.ck-lec{display:flex;align-items:center;gap:12px;}
.ck-lec-ic{flex:none;width:36px;height:36px;border-radius:var(--radius-sm);background:var(--bg);display:flex;
  align-items:center;justify-content:center;}
.ck-lec-ic.on{background:var(--primary-soft);}
.ck-lec-txt{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px;}
.ck-lec-txt b{font-size:12px;font-weight:800;color:var(--text-sub);letter-spacing:.2px;}
.ck-lec-txt span{font-size:14px;font-weight:500;color:var(--text-sub);}
.ck-lec-txt span.ck-lec-name{font-weight:700;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.st-key-roomdoc [data-testid="stCaptionContainer"] p{font-size:12.5px;color:var(--text-sub);}
/* st-key-roomdoc 의 stFileUploaderDropzone (DOM 확인): 얇은 점선 상자 */
.st-key-roomdoc [data-testid="stFileUploaderDropzone"]{background:var(--bg);border:1px dashed var(--border);
  border-radius:var(--radius-md);padding:8px 12px;min-height:0;}
.st-key-roomdoc [data-testid="stFileUploaderDropzone"] button{min-height:32px;border-radius:var(--radius-sm);}
.ck-room-title{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
.ck-now{font-size:11px;font-weight:800;color:var(--cookie-deep);background:var(--cookie-soft);
  padding:3px 9px;border-radius:999px;}
.ck-desc{font-size:14px;color:var(--text-sub);margin-top:6px;}
/* ck-ref: /계획 답변 맨 위 기준 줄 (오늘 날짜, 지금 과정) */
.ck-ref{display:inline-block;font-size:12px;font-weight:700;color:var(--primary);background:var(--primary-soft);
  padding:4px 10px;border-radius:999px;margin-bottom:2px;}
/* ck-tl: /커리큘럼 카드 타임라인 (STEP 마다 한 줄, 얇은 선 위에 같은 간격의 점) */
.ck-tl{container-type:inline-size;}
.ck-tl-step{font-size:13.5px;font-weight:700;color:var(--text);margin:18px 0 4px;}
.ck-tl-step b{font-family:'Poppins',sans-serif;font-size:11px;font-weight:700;color:var(--primary);
  letter-spacing:.6px;margin-right:8px;}
.ck-tl-row{--pt:8px;display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));}
/* ck-tl-row.now: '지금' 라벨이 올라갈 자리를 그 줄에만 만든다 */
.ck-tl-row.now{--pt:24px;}
.ck-tl-it{position:relative;padding:var(--pt) 3px 0;text-align:center;min-width:0;}
/* 선: 항목마다 왼쪽 절반(::before)과 오른쪽 절반(::after), 지난 구간은 진하게 */
.ck-tl-it::before, .ck-tl-it::after{content:"";position:absolute;top:calc(var(--pt) + 5px);height:2px;width:50%;background:var(--border);}
.ck-tl-it::before{left:0;} .ck-tl-it::after{right:0;}
.ck-tl-it:first-child::before, .ck-tl-it:last-child::after{display:none;}
.ck-tl-it.done::before, .ck-tl-it.done::after, .ck-tl-it.cur::before{background:var(--primary);}
/* 점: 학습 = 속이 빈 보라 고리, 미니프로젝트 = 주황, 활동 = 청록 */
.ck-tl-nd{position:relative;z-index:1;display:block;box-sizing:border-box;width:12px;height:12px;margin:0 auto;
  border-radius:50%;background:var(--surface);border:2px solid var(--primary);}
.t-p > .ck-tl-nd{background:var(--project);border-color:var(--project);}
.t-a > .ck-tl-nd{background:var(--activity);border-color:var(--activity);}
.ck-tl-it.cur .ck-tl-nd{box-shadow:0 0 0 4px var(--cookie-soft),0 0 0 5px var(--cookie);}
.ck-tl-it.todo .ck-tl-nd{opacity:.45;}
.ck-tl-nm{display:block;margin-top:9px;font-size:11.5px;line-height:1.35;color:var(--text);word-break:keep-all;
  overflow-wrap:anywhere;}
.ck-tl-it.todo .ck-tl-nm{color:var(--muted);}
.ck-tl-it.cur .ck-tl-nm{font-weight:700;}
.ck-tl-now{position:absolute;top:0;left:50%;transform:translateX(-50%);font-size:10px;font-weight:800;line-height:1;
  color:var(--cookie-deep);background:var(--cookie-soft);padding:3px 7px;border-radius:999px;white-space:nowrap;}
/* ck-tl-legend: 유형 범례 (학습 / 미니프로젝트 / 활동) */
.ck-tl-legend{display:flex;flex-wrap:wrap;gap:4px 16px;margin-top:20px;padding-top:12px;border-top:1px solid var(--border);
  font-size:11.5px;color:var(--text-sub);}
.ck-tl-legend span{display:inline-flex;align-items:center;gap:6px;}
.ck-tl-legend .ck-tl-nd{width:10px;height:10px;margin:0;}
/* 카드 폭이 좁으면 세로 타임라인 (점 왼쪽, 이름 오른쪽) */
@container (max-width:560px){
  .ck-tl-row{display:block;}
  .ck-tl-it{display:flex;align-items:center;gap:10px;padding:5px 0 5px 2px;text-align:left;}
  .ck-tl-it::before, .ck-tl-it::after{left:7px;right:auto;width:2px;height:50%;}
  .ck-tl-it::before{top:0;} .ck-tl-it::after{top:50%;}
  .ck-tl-nd{margin:0;flex:none;}
  .ck-tl-nm{margin-top:0;font-size:12.5px;}
  .ck-tl-now{position:static;transform:none;}
}

/* stChatInputSubmitButton (DOM 확인, aria-label "Send message"): 보내기 버튼을 기본 빨강 대신 primary 로 */
[data-testid="stChatInputSubmitButton"]:not(:disabled){background:var(--primary)!important;color:var(--surface)!important;}
[data-testid="stChatInputSubmitButton"]:not(:disabled):hover{background:var(--primary-hover)!important;}
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

/* st-key-edrow_*: 학습방 편집 행 (손잡이, 유형 아이콘, 유형, 이름, 지금, 삭제) 높이 맞춤 */
[class*="st-key-edrow_"]{border-radius:var(--radius-sm);background:var(--surface);}
[class*="st-key-edrow_"] button{min-height:38px;padding:0 8px;color:var(--text-sub);}
/* ck-grip: 드래그 손잡이 (st.html) */
.ck-grip{display:flex;align-items:center;justify-content:center;height:38px;border-radius:var(--radius-sm);
  cursor:grab;touch-action:none;user-select:none;}
.ck-grip:hover{background:var(--bg);}
.ck-grip img{pointer-events:none;}
/* st-key-edrow_* 의 드래그 상태 (edit_sorter 컴포넌트가 붙이는 클래스) */
[class*="st-key-edrow_"].ck-dragging{position:relative;z-index:10;background:var(--primary-soft);
  box-shadow:var(--shadow);opacity:.92;}
[class*="st-key-edrow_"].ck-dragging .ck-grip{cursor:grabbing;}
[class*="st-key-edrow_"].ck-drop-before{box-shadow:0 -3px 0 0 var(--primary);}
[class*="st-key-edrow_"].ck-drop-after{box-shadow:0 3px 0 0 var(--primary);}
/* st-key-edic_l|p|a_*: 편집 행의 유형 아이콘 (markdown 안 아이콘 span[role="img"]) */
[class*="st-key-edic_"] [data-testid="stMarkdownContainer"]{margin-bottom:0;}
[class*="st-key-edic_"] [data-testid="stMarkdownContainer"] p{display:flex;justify-content:center;
  align-items:center;height:38px;margin:0;}
[class*="st-key-edic_"] [data-testid="stMarkdownContainer"] p span[role="img"]{font-size:20px;color:var(--primary);}
[class*="st-key-edic_p_"] [data-testid="stMarkdownContainer"] p span[role="img"]{color:var(--project);}
[class*="st-key-edic_a_"] [data-testid="stMarkdownContainer"] p span[role="img"]{color:var(--activity);}
/* stCheckbox[data-selected="true"] 의 체크 상자 (label > span + div, DOM 확인): 기본 테마 빨강 대신 primary */
[data-testid="stCheckbox"][data-selected="true"] label > span + div{background:var(--primary)!important;
  border-color:var(--primary)!important;}
/* st-key-edsort: 드래그 정렬용 JS 컴포넌트 자리 (화면에 보일 것이 없음) */
.st-key-edsort{display:none!important;}
/* st-key-slashmenu: 슬래시 메뉴 JS 컴포넌트 자리 (화면에 보일 것이 없음) */
.st-key-slashmenu{display:none!important;}
/* ck-slash: 입력창에 / 를 치면 뜨는 명령어 팝업 (slash_menu 컴포넌트가 body 에 붙임) */
.ck-slash{position:fixed;z-index:1000;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius-md);box-shadow:var(--shadow);padding:8px;max-height:60vh;overflow:auto;box-sizing:border-box;}
.ck-slash-h{font-size:12px;font-weight:700;color:var(--text-sub);padding:6px 10px 4px;}
.ck-slash-row{display:flex;align-items:center;gap:12px;padding:8px 10px;border-radius:var(--radius-sm);cursor:pointer;}
.ck-slash-row.on{background:var(--primary-soft);}
.ck-slash-row.on::after{content:"Enter";margin-left:auto;font-size:11px;font-weight:600;color:var(--primary);
  border:1px solid var(--primary);border-radius:6px;padding:1px 7px;}
.ck-slash-ic{flex:none;width:32px;height:32px;border-radius:9px;background:var(--bg);color:var(--text-sub);
  display:flex;align-items:center;justify-content:center;}
.ck-slash-row.on .ck-slash-ic{background:var(--surface);color:var(--primary);}
.ck-slash-t{display:flex;flex-direction:column;min-width:0;}
.ck-slash-t b{font-size:14.5px;font-weight:700;color:var(--text);}
.ck-slash-t small{font-size:12.5px;color:var(--text-sub);}
.ck-slash-f{font-size:11.5px;color:var(--text-sub);padding:8px 10px 4px;border-top:1px solid var(--border);margin-top:4px;}

/* st-key-pf_open: 학습방 헤더의 '포트폴리오 만들기' 버튼 (답변 자료 줄의 오른쪽 끝) */
.st-key-pf_open{margin-left:auto;}
.st-key-pf_open button{min-height:30px;padding:2px 12px;border-radius:999px;}
/* st-key-pfneed_*: '[숫자 입력 필요]' 가 남아 있는 포트폴리오 입력칸 (노란 바탕 + 왼쪽 노란 표시 + 아래 안내) */
[class*="st-key-pfneed_"]{background:var(--cookie-soft);border-radius:var(--radius-sm);padding:8px 10px;
  box-shadow:inset 3px 0 0 var(--cookie);gap:4px;}
.ck-need{font-size:12px;font-weight:700;color:var(--cookie-deep);}
/* ck-pf-sec: 포트폴리오 편집 화면의 SPARK 블록 제목 */
.ck-pf-sec{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:800;color:var(--text);margin-top:6px;}
.ck-pf-sec i{font-style:normal;width:24px;height:24px;border-radius:8px;background:var(--primary-soft);color:var(--primary);
  display:inline-flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;}
/* ck-pf-ex: 예시 포트폴리오 안내 (배지 + 한 줄) */
.ck-pf-ex{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:13px;color:var(--text-sub);}
.ck-pf-ex span{flex:none;font-size:11px;font-weight:800;color:var(--cookie-deep);background:var(--cookie-soft);
  border-radius:999px;padding:1px 9px;}
/* ck-pf-sum: 편집 화면 맨 위 점검표 요약 줄 */
.ck-pf-sum{display:flex;align-items:center;gap:6px 12px;flex-wrap:wrap;font-size:12.5px;color:var(--text-sub);
  background:var(--bg);border-radius:var(--radius-sm);padding:8px 12px;}
.ck-pf-sum b{font-size:13.5px;color:var(--primary);}
.ck-pf-sum .need{margin-left:auto;font-weight:700;color:var(--cookie-deep);}
/* ck-pfc: 점검표 (O/X 목록) */
.ck-pfc{list-style:none;margin:6px 0 0;padding:0;}
.ck-pfc-row{display:flex;align-items:flex-start;gap:10px;padding:7px 0;border-top:1px solid var(--border);
  font-size:13.5px;line-height:1.5;color:var(--text);}
.ck-pfc-row > span{flex:none;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:800;background:var(--pastel-2);color:var(--ic-2);}
.ck-pfc-row.x > span{background:var(--cookie-soft);color:var(--cookie-deep);}
.ck-pfc-row small{display:block;font-size:12.5px;color:var(--cookie-deep);}

/* 좁은 화면: 타일은 가로형, 히어로 축소 */
@media (max-width:640px){
  [data-testid="stMainBlockContainer"]{padding:56px 16px 32px;}
  .ck-hero-big{font-size:28px;}
  .ck-hero-art{flex:1 1 100%;}
  .ck-hero-art img{width:130px;height:auto;}
  [class*="st-key-cattile_"] button, [class*="st-key-cattile_"] button > div,
  [class*="st-key-cattile_"] button > div > span{flex-direction:row;justify-content:flex-start;gap:16px;}
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
    from langchain_core.output_parsers import StrOutputParser
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
    is_study: bool = Field(
        description="질문이 공부 방법, 학습, 복습, 개념 이해, 프로젝트 준비, 자기계발처럼 '어떻게 배우고 준비할지'에 관한 것이면 true. "
                    "출결, 장려금, 일정, 규정, 지원 자격, 수료 기준 같은 행정/사실 확인 질문이면 false."
    )
    senior_quote: str = Field(
        description="is_study 가 true 이고 문서에 [재학생 경험] 문단이 있을 때만, 그 문단에서 가져온 선배의 한마디 1~2문장. "
                    "그 외에는 반드시 빈 문자열."
    )
    challenge: str = Field(
        description="is_study 가 true 일 때만, 오늘 바로 해 볼 수 있는 구체적인 학습 행동 한 가지. 한 문장. "
                    "is_study 가 false 이면 반드시 빈 문자열."
    )
    followups: List[str] = Field(
        description="후배(사용자)가 이어서 직접 물어볼 법한 질문 3개. 사용자 입장의 의문문으로 쓰고 반드시 물음표(?)로 끝낸다. "
                    "각 25자 이내. 예: '출석 인정 사유는 어떤 게 있나요?'. "
                    "'~해 보세요', '~확인하세요', '~추천해 주세요' 같은 조언, 평서문, 요청문은 금지."
    )


def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)


# ---------------------------------------------------------------- 검색 질의 재작성 (교안: 쿼리 최적화 - Query Rewriting)
# "그럼 오픽은?"처럼 앞 대화를 받아 묻는 질문은 그대로 검색하면 엉뚱한 문단이 나온다.
# 이전 대화가 있을 때만 LLM 으로 '독립형 검색 질의'로 바꾼 뒤 검색한다. (첫 질문은 그대로 검색)
REWRITE_PROMPT = (
    "당신은 검색 질의 최적화 도우미입니다.\n"
    "[이전 대화]를 참고해 후배의 마지막 질문을 벡터 검색에 적합한 '독립형 검색 질의' 한 줄로 한국어로 재작성하세요.\n"
    "'그건', '그럼', '거기', '그거'처럼 앞 대화를 가리키는 말이나 생략된 대상은 이전 대화에 나온 구체적인 말로 채우세요.\n"
    "마지막 질문이 이전 대화와 다른 새 주제이거나 그 자체로 뜻이 분명하면 원래 질문을 그대로 출력하세요.\n"
    "질문에 쓰인 단어(줄임말 포함)는 지우지 말고, 답변이나 설명 없이 질의 한 줄만 출력하세요.\n\n"
    "[이전 대화]\n{history}"
)


def dedup_docs(docs):
    """같은 청크가 여러 번 검색되면 한 번만 남긴다."""
    seen, out = set(), []
    for d in docs:
        key = (d.metadata.get("source"), d.metadata.get("page"), d.page_content[:200])
        if key not in seen:
            seen.add(key)
            out.append(d)
    return out


def rewrite_query(question, history=""):
    """이전 대화가 있으면 질문을 독립형 검색 질의로 바꾼다. 실패하면 원래 질문을 쓴다."""
    if not history or history == "(없음)":
        return question
    try:
        prompt = ChatPromptTemplate.from_messages([("system", REWRITE_PROMPT), ("human", "{input}")])
        chain = prompt | ChatOpenAI(model=CHAT_MODEL, temperature=0) | StrOutputParser()
        lines = [s.strip() for s in chain.invoke({"input": question, "history": history}).splitlines() if s.strip()]
        return lines[0] if lines else question
    except Exception:
        return question


def search_docs(retriever, question, history=""):
    """검색: 재작성한 질의로 찾는다."""
    return dedup_docs(retriever.invoke(rewrite_query(question, history)))


# 두 프롬프트(일반 대화 / 학습방)가 함께 쓰는 출력 규칙
ANSWER_RULES = (
    "is_study 는 질문이 공부 방법, 학습, 복습, 개념 이해, 프로젝트 준비, 자기계발에 관한 것일 때만 true 입니다. "
    "출결, 장려금, 일정, 규정, 지원 자격처럼 행정이나 사실을 확인하는 질문은 false 입니다.\n"
    "is_study 가 false 이면 senior_quote 와 challenge 는 반드시 빈 문자열로 두세요.\n"
    "senior_quote 는 is_study 가 true 이고 자료에 '[재학생 경험]' 문단이 있을 때만 그 내용을 옮겨 쓰고, 없으면 비워 두세요.\n"
    "followups 는 후배가 이어서 직접 물어볼 질문 3개입니다. 후배의 말투로 쓴 의문문이어야 하고 반드시 '?' 로 끝나야 합니다. "
    "(좋은 예: '출석 인정 사유는 어떤 게 있나요?' / 나쁜 예: '출석 인정 사유를 다시 확인해보세요.')\n"
)

SYSTEM_PROMPT = (
    "당신은 KT AIVLE School 을 먼저 수료한 다정한 선배 '쿠키 선배'입니다.\n"
    "사실에 관한 질문은 반드시 아래 [문서] 내용만 근거로 답변하세요.\n"
    "문서에 없는 내용이면 추측하지 말고 '백서에서 확인할 수 없는 내용이에요.'라고 말한 뒤, "
    "AIVLE-EDU 공지사항이나 1:1 문의, 담당 에이블매니저에게 확인하도록 안내하세요.\n"
    "말투는 따뜻한 해요체로, 결론을 먼저 말하고 번호 목록으로 짧게 정리하세요.\n"
    "후배가 바로 움직일 수 있도록 행동을 권하고 응원해 주세요.\n"
    "문서의 장, 절 번호나 '~장을 참고하세요' 같은 문서 위치 안내는 쓰지 말고 내용을 직접 설명하세요.\n"
    "가운뎃점 기호(·)는 쓰지 말고 쉼표나 '와/과'로 이어 쓰세요.\n"
    + ANSWER_RULES
    + "\n[이전 대화]\n{history}\n\n[문서]\n{context}"
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
    if not splits:
        raise ValueError("PDF에서 글자를 찾지 못했어요. 스캔 이미지로만 된 PDF는 읽을 수 없어요.")

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


class PdfLocked(Exception):
    """비밀번호가 걸린 PDF (비밀번호가 없거나 틀림)."""


def unlock_pdf(path, password=None):
    """비밀번호가 걸린 PDF면 풀어서 사본 경로를, 아니면 원래 경로를 돌려준다.
    비밀번호는 입력값 → 환경 변수/Streamlit Secrets 의 PDF_PASSWORD 순서로 시도한다 (코드에는 적지 않는다)."""
    doc = pymupdf.open(path)
    try:
        if not doc.needs_pass:
            return path
        for pw in [p for p in (password, os.environ.get("PDF_PASSWORD")) if p]:
            if doc.authenticate(pw):
                out = path[:-4] + "_unlocked.pdf"
                doc.save(out, encryption=pymupdf.PDF_ENCRYPT_NONE)
                return out
        raise PdfLocked("비밀번호가 맞지 않아요. 다시 입력해 주세요." if password else "비밀번호를 입력하면 풀어서 읽을게요.")
    finally:
        doc.close()


def collection_id(collection_name="aivle_docs"):
    """chroma_db 에 문서가 든 해당 컬렉션이 있으면 그 id(재생성되면 바뀜), 없으면 None."""
    if IMPORT_ERROR or not os.path.isdir(CHROMA_DIR):
        return None
    try:
        import chromadb
        col = chromadb.PersistentClient(path=CHROMA_DIR).get_collection(collection_name)
        return str(col.id) if col.count() > 0 else None
    except Exception:
        return None


def has_collection(collection_name="aivle_docs"):
    return collection_id(collection_name) is not None


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
            docs=RunnableLambda(lambda x: search_docs(retriever, x["input"], x.get("history"))),
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


QUESTION_ENDINGS = ("나요", "까요", "가요", "을까", "할까", "인가", "는지요", "죠", "니까")
ADVICE_ENDINGS = ("세요", "십시오", "합니다", "습니다", "해요", "봐요", "돼요", "좋아요")


def clean_followups(items, limit=3):
    """이어서 물어보기: '?' 로 끝나는 질문만 남긴다.

    물음표만 빠진 의문문('~나요', '~까요')은 '?' 를 붙여 고치고,
    조언/평서문('~확인해보세요.')은 버린다.
    """
    out = []
    for raw in items or []:
        q = " ".join(str(raw or "").split()).lstrip("-•0123456789. ").strip()
        if not q:
            continue
        body = q.rstrip("?.!~ ")
        if body.endswith(ADVICE_ENDINGS):
            continue  # '~해 보세요?' 처럼 물음표만 붙은 조언도 버린다
        if not q.endswith("?"):
            if not body.endswith(QUESTION_ENDINGS):
                continue
            q = body + "?"
        if q not in out:
            out.append(q)
    return out[:limit]


EMPTY_ANSWER = (
    "백서에서 확인할 수 없는 내용이에요. 질문을 조금 더 구체적으로 적어 주시거나, "
    "AIVLE-EDU 공지사항이나 1:1 문의, 담당 에이블매니저에게 확인해 주세요."
)


def to_message(result, kind="백서"):
    """체인 결과 → 화면용 assistant 메시지 dict."""
    ans = result["answer"]
    study = bool(getattr(ans, "is_study", False))
    quote_text, challenge_text = "", ""
    if study:
        quote_text = (ans.senior_quote or "").strip()
        challenge_text = (ans.challenge or "").strip()
    # 모델이 answer 를 비워 보내는 경우가 있어(예: 앞뒤 맥락 없는 '청년수당 받는 중이면?') 빈 말풍선 대신 안내 문구
    answer_text = (ans.answer or "").strip() or EMPTY_ANSWER
    return {
        "role": "assistant",
        "answer": answer_text,
        "is_study": study,
        "quote": quote_text,
        "challenge": challenge_text,
        "followups": clean_followups(ans.followups),
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
    + ANSWER_RULES
    + "\n[이전 대화]\n{history}\n\n[백서]\n{wp}\n\n[교안]\n{lecture}\n\n[{web_label}]\n{web}"
)


def room_answer(question, topic, sources, wp_retriever=None, lecture_retriever=None, history=""):
    """학습방 답변: 켜진 자료(백서/교안/웹 검색)를 종합한다."""
    srcs, wp_docs, lec_docs = [], [], []
    search_q = rewrite_query(question, history)  # 앞 대화를 받아 묻는 질문도 검색되게
    query = topic + " " + search_q
    if "백서" in sources and wp_retriever is not None:
        wp_docs = wp_retriever.invoke(query)[:3]
        srcs += [doc_source(d, "백서") for d in wp_docs]
    if "교안" in sources and lecture_retriever is not None:
        lec_docs = lecture_retriever.invoke(query)
        srcs += [doc_source(d, "교안") for d in lec_docs]

    web_label, web_text = "웹 검색", "(사용 안 함)"
    if "웹 검색" in sources:
        text, cites = web_search(search_q, topic)
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


# 학습방 항목 유형: 라벨 / Material 아이콘 / 키 접두어(CSS 색 지정용)
ITEM_TYPES = {
    "learn": {"label": "학습", "icon": "menu_book", "tag": "l"},
    "project": {"label": "미니프로젝트", "icon": "flag", "tag": "p"},
    "activity": {"label": "활동", "icon": "groups", "tag": "a"},
}


def item_type(item):
    """항목의 유형 코드 (알 수 없는 값은 learn 으로)."""
    t = (item or {}).get("type", "learn")
    if t in ITEM_TYPES:
        return t
    return "learn"


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
            ("과제 선정 워크숍", "activity"), ("현직자 코칭", "activity"), ("과제 수행", "project"),
            ("발표회", "activity")])},
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
# 데모 학습방 대화 (?demo=1): 포트폴리오 만들기 시연용. {학습방 이름: [(질문, 답변)]}
DEMO_ROOM_TALKS = {
    "미니프로젝트 4차": [
        ("서버를 켤 때마다 첫 답변이 2분 넘게 걸려요. 백서 PDF를 매번 다시 벡터화하는 것 같은데 어떻게 줄일 수 있을까요?",
         "원인을 잘 짚었어요. **이미 만든 벡터 DB를 다시 쓰면** 첫 답변이 바로 나와요.\n\n"
         "1. `persist_directory` 에 저장된 chroma_db 컬렉션이 있으면 임베딩을 건너뛰고 바로 불러와요.\n"
         "2. 백서 파일의 해시를 저장해 두고, 파일이 바뀐 경우에만 다시 벡터화해요.\n"
         "3. 불러온 검색기는 `st.cache_resource` 로 묶어 세션끼리 함께 써요.\n\n"
         "고치기 전후의 대기 시간을 꼭 재 두세요. 발표와 포트폴리오에서 가장 좋은 근거가 돼요."),
        ("적용했더니 재시작해도 첫 답변이 바로 나와요. 그런데 두 명이 동시에 교안을 올리면 서로의 업로드가 지워져요.",
         "모두가 같은 컬렉션 이름을 쓰고 있어서 그래요. **세션마다 컬렉션을 나누면** 해결돼요.\n\n"
         "1. 세션 ID를 만들어 컬렉션 이름 뒤에 붙여요. 예: `lecture_ab12cd34`\n"
         "2. 공용 백서 컬렉션은 읽기 전용으로 두고, 업로드 문서만 세션 컬렉션에 넣어요.\n"
         "3. 두 브라우저에서 동시에 올려 보고 서로의 문서가 남아 있는지 확인해요."),
        ("비밀번호가 걸린 교안 PDF는 로더에서 오류가 나요. 어떻게 처리하면 좋을까요?",
         "수집 전에 **잠금을 먼저 푸는 단계**를 하나 두면 돼요.\n\n"
         "1. PyMuPDF 로 열어 `needs_pass` 인지 확인해요.\n"
         "2. 잠겨 있으면 사용자에게 비밀번호를 물어 `authenticate` 한 뒤, 잠금이 풀린 사본을 저장해요.\n"
         "3. 그 사본을 로더에 넘겨요. 비밀번호 자체는 저장하지 않아요."),
        ("AI가 써 준 코드를 그대로 써도 될까요? 발표 때 검증을 어떻게 설명하면 좋을까요?",
         "그대로 쓰기보다 **검증한 기록을 남기는 것**이 중요해요.\n\n"
         "1. 자주 나올 질문 세트를 만들어, 답변의 근거 페이지가 백서 원문과 맞는지 대조해요.\n"
         "2. 근거가 어긋난 질문은 chunk_size 와 k 값을 바꿔 다시 확인하고, 바꾼 이유를 적어 둬요.\n"
         "3. 발표에서는 'AI가 제안한 것, 내가 확인한 것, 내가 고친 것'을 나눠서 보여 줘요."),
    ],
    "LangChain RAG": [
        ("RAG는 LLM에게 그냥 물어보는 것과 무엇이 다른가요?",
         "RAG는 **먼저 문서를 찾아서, 그 내용을 근거로 답하게** 하는 방식이에요.\n\n"
         "1. 문서를 잘게 나눠 벡터로 저장해 둬요.\n"
         "2. 질문과 비슷한 문단을 검색해 프롬프트에 함께 넣어요.\n"
         "3. 모델은 그 문단 안에서만 답하고, 어느 페이지를 봤는지 근거를 보여 줄 수 있어요."),
        ("retriever 의 k 값은 몇으로 두면 좋나요?",
         "교안 기준인 **k=4 에서 시작**해 검색 결과를 보며 조정해요.\n\n"
         "1. 답에 필요한 문단이 빠지면 k 를 늘려요.\n"
         "2. 관계없는 문단이 섞여 답이 흐려지면 k 를 줄이거나 chunk 를 작게 해요.\n"
         "3. 같은 질문으로 검색된 문단을 직접 읽어 보는 것이 가장 빠른 확인 방법이에요."),
        ("구조화 출력은 언제 쓰면 좋나요?",
         "답변을 **화면의 정해진 자리에 나눠 보여 줘야 할 때** 써요.\n\n"
         "1. Pydantic 모델로 답변, 후속 질문 같은 필드를 정의해요.\n"
         "2. `with_structured_output` 으로 모델이 그 형식대로만 답하게 해요.\n"
         "3. 문자열을 직접 자르는 것보다 오류가 적고, 필드별로 검증하기 쉬워요."),
    ],
    "데이터 분석": [
        ("결측치는 무조건 평균으로 채우면 되나요?",
         "아니에요. **왜 비어 있는지부터 확인**하고 방법을 골라요.\n\n"
         "1. 결측 비율과 어느 행에 몰려 있는지 먼저 봐요.\n"
         "2. 치우친 분포라면 평균보다 중앙값이 안전해요.\n"
         "3. 채우기 전후의 분포를 그려 비교하고, 달라진 점을 기록해 둬요."),
        ("groupby 로 집계한 결과가 맞는지 어떻게 확인하나요?",
         "**원본과 다시 맞춰 보는 검산**을 습관으로 만들어요.\n\n"
         "1. 집계 결과의 합계가 원본 행 수나 총합과 같은지 확인해요.\n"
         "2. 그룹 하나를 골라 직접 필터링한 값과 비교해요.\n"
         "3. 결측이 있는 키는 groupby 에서 빠지니 `dropna=False` 로 한 번 더 봐요."),
    ],
}


def _demo_answer(text):
    return {"role": "assistant", "answer": text, "is_study": True, "quote": "", "challenge": "", "followups": [],
            "sources": []}


def seed_demo_rooms():
    """이름이 같은 학습방을 찾아 데모 대화를 이어 붙인다 (커리큘럼을 고쳐서 방이 없으면 건너뜀)."""
    for s in st.session_state.curriculum["steps"]:
        for it in s["items"]:
            for q, a in DEMO_ROOM_TALKS.get(it["name"], []):
                room(it["id"])["messages"] += [{"role": "user", "text": q}, _demo_answer(a)]


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
            "is_study": True,
            "followups": ["오류가 나거나 막히면 어떻게 하나요?", "주말 복습 루틴은 어떻게 짜나요?", "스터디는 어떻게 꾸리나요?"],
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
                "is_study": True,
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
    seed_demo_rooms()
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
            'items': [{'id': 's3-1', 'name': '과제 선정 워크숍', 'type': 'activity'},
                      {'id': 's3-2', 'name': '현직자 코칭', 'type': 'activity'},
                      {'id': 's3-3', 'name': '과제 수행', 'type': 'project'},
                      {'id': 's3-4', 'name': '발표회', 'type': 'activity'}]}]}
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
# 포트폴리오 만들기
# ======================================================================
# 포트폴리오 만들기: 학습방 대화 → 10초 요약 + SPARK 프로젝트 페이지 + 점검표 (초안 스키마, 프롬프트, 예시, 내보내기).
import copy
import html
import re
from typing import List

from pydantic import BaseModel, Field


PF_NEED = "[숫자 입력 필요]"
PF_FOOTER = "AIVLE School 학습 도우미 쿠키 선배로 만든 초안"
PF_SPARK = [("S", "문제 정의"), ("P", "선택 이유"), ("A", "실행과 성과"), ("R", "회고와 검증"), ("K", "직무 키워드")]


# ---------------------------------------------------------------- 구조화 출력 스키마
class PortfolioMetric(BaseModel):
    """대표 수치 하나 (Before → After)"""

    label: str = Field(description="지표 이름. 예: 첫 답변 대기 시간")
    before: str = Field(description="시작값. 대화나 입력에 없는 숫자면 반드시 '" + PF_NEED + "'")
    after: str = Field(description="결과값. 대화나 입력에 없는 숫자면 반드시 '" + PF_NEED + "'")


class PortfolioStrength(BaseModel):
    """핵심 강점과 한 줄 근거"""

    title: str = Field(description="강점 이름. 12자 안팎의 명사구")
    evidence: str = Field(description="근거 한 줄. 어느 학습방/프로젝트에서 무엇을 했는지. '학습방 이름: 한 일' 형식")


class PortfolioAlternative(BaseModel):
    """대안 비교표의 한 줄"""

    option: str = Field(description="대안 이름. 기존 방식과 실제로 고른 방식을 포함")
    pros: str = Field(description="장점 한 줄")
    cons: str = Field(description="한계 한 줄")
    decision: str = Field(description="'선택' 또는 '제외'")


class PortfolioProject(BaseModel):
    """프로젝트 한 페이지 (SPARK 5블록)"""

    room: str = Field(description="근거가 된 학습방 이름 그대로")
    title: str = Field(description="S: 프로젝트 제목. 무엇을 만들었는지 한 줄")
    who_pain: str = Field(description="S: '누가 어떤 불편을 겪었는지'로 시작하는 문제 정의 1~2문장")
    summary: List[str] = Field(description="S: 프로젝트 3줄 요약. 정확히 3개")
    limits: str = Field(description="P: 기존 방식의 한계 1~2문장")
    alternatives: List[PortfolioAlternative] = Field(description="P: 대안 비교 2~3줄. 마지막 줄이 고른 방식")
    constraints: str = Field(description="P: 제약 조건 (기간, 인원, 환경 등). 대화에 없으면 빈 문자열")
    role: str = Field(description="A: 내 역할 한 줄")
    contribution: str = Field(description="A: 내 기여도(%). 사용자가 입력하지 않았으면 반드시 '" + PF_NEED + "'")
    metric_label: str = Field(description="A: 대표 지표 이름")
    before: str = Field(description="A: 시작값. 대화나 입력에 없으면 반드시 '" + PF_NEED + "'")
    after: str = Field(description="A: 결과값. 대화나 입력에 없으면 반드시 '" + PF_NEED + "'")
    methods: List[str] = Field(description="A: 방법별 기여 2~3개. '방법: 그 방법이 결과에 준 영향' 형식")
    stuck: str = Field(description="R: 막힌 지점과 해결 과정 2~3문장")
    ai_check: str = Field(description="R: AI 결과물을 어떻게 검증했는지. 대화에 없으면 빈 문자열")
    limitations: str = Field(description="R: 남은 한계와 다음에 할 일 1~2문장")
    keywords: List[str] = Field(description="K: 희망 직무 키워드 3~4개. '키워드: 이 프로젝트에서의 근거' 형식")


class PortfolioDraft(BaseModel):
    """포트폴리오 초안"""

    slogan: str = Field(description="일하는 방식 한 줄. '[문제]를 [방법]으로 해결하는 [정체성]' 공식. 40자 안팎")
    metrics: List[PortfolioMetric] = Field(description="대표 수치 1~3개")
    strengths: List[PortfolioStrength] = Field(description="핵심 강점. 정확히 3개")
    stack_main: List[str] = Field(description="주력 기술. '기술: 연결 프로젝트' 형식. 숙련도 %나 게이지 금지")
    stack_exp: List[str] = Field(description="경험 기술. '기술: 연결 프로젝트' 형식. 숙련도 %나 게이지 금지")
    projects: List[PortfolioProject] = Field(description="프로젝트 페이지. 요청한 학습방마다 하나씩, 같은 순서")


PF_SYSTEM = (
    "당신은 KT AIVLE School 교육생의 취업 포트폴리오 초안을 써 주는 선배 '쿠키 선배'입니다.\n"
    "아래 학습방 대화와 사용자가 입력한 값만 근거로, 10기 포트폴리오 로드맵의 '최근 방식'에 맞춰 씁니다.\n\n"
    "[구성]\n"
    "1. 첫 페이지(10초 요약): 일하는 방식 한 줄 슬로건 '[문제]를 [방법]으로 해결하는 [정체성]', 대표 수치 1~3개(Before → After), "
    "핵심 강점 3개와 한 줄 근거(어느 학습방/프로젝트인지), 기술 스택은 주력/경험 두 단계와 연결 프로젝트만.\n"
    "2. 프로젝트 페이지(SPARK): S 문제 정의(누가 어떤 불편을 겪었는지로 시작), P 선택 이유(기존 방식의 한계, 대안 비교, 제약), "
    "A 실행과 성과(내 역할과 기여도, 시작값 → 결과값, 방법별 기여), R 회고와 검증(막힌 지점과 해결, AI 검증 기록, 한계), "
    "K 직무 키워드(희망 직무와 연결).\n\n"
    "[숫자 규칙: 가장 중요]\n"
    "- 숫자는 사용자가 직접 입력한 값이나 대화에 실제로 나온 값만 씁니다.\n"
    "- 그 밖의 수치, 시작값, 결과값, 기여도(%)는 절대 지어내지 말고 정확히 '" + PF_NEED + "' 라고 씁니다.\n"
    "- 기술 숙련도를 %나 게이지로 표현하지 않습니다.\n\n"
    "[문체]\n"
    "- 합니다체, 한 문장은 짧게. 과장하는 형용사 대신 한 일과 결과를 씁니다.\n"
    "- 대화에 없는 경험을 만들어 내지 않습니다. 근거가 없으면 빈 문자열로 둡니다.\n"
    "- 가운뎃점 문자는 쓰지 않고 쉼표를 씁니다."
)


def pf_page_rooms(convos):
    """프로젝트 페이지로 만들 학습방: 미니프로젝트 유형이 있으면 그것만, 없으면 고른 방 전부."""
    projects = [c for c in convos if c["kind"] == "project"]
    return projects or list(convos)


def pf_convo_text(convos, per_room=12, answer_chars=500, total=14000):
    """고른 학습방의 문답을 프롬프트용 텍스트로 (긴 기록은 최근 것만, 답변은 앞부분만)."""
    blocks = []
    for c in convos:
        lines = ["## 학습방: " + c["name"] + " (" + c["label"] + ")"]
        for q, a in c["qa"][-per_room:]:
            lines.append("후배: " + q.strip()[:400])
            if a:
                lines.append("선배: " + a.strip()[:answer_chars])
        blocks.append("\n".join(lines))
    text = "\n\n".join(blocks)
    return text[-total:]


def pf_build_prompt(convos, info):
    """(system, human) 프롬프트 문자열. info: name, job, team, metrics{학습방 이름: {label, before, after, contribution}}."""
    pages = pf_page_rooms(convos)
    lines = ["[사용자 입력]",
             "이름: " + (info.get("name") or "(미입력)"),
             "희망 직무: " + (info.get("job") or "(미입력)"),
             "팀 규모: " + (info.get("team") or "(미입력)"),
             "", "[프로젝트 페이지로 쓸 학습방 (이 순서대로 하나씩)]"]
    for c in pages:
        m = (info.get("metrics") or {}).get(c["name"], {})
        lines.append("- " + c["name"] + " | 지표 이름: " + (m.get("label") or "(미입력)")
                     + " | 시작값: " + (m.get("before") or "(미입력: " + PF_NEED + " 로 쓸 것)")
                     + " | 결과값: " + (m.get("after") or "(미입력: " + PF_NEED + " 로 쓸 것)")
                     + " | 기여도: " + (m.get("contribution") or "(미입력: " + PF_NEED + " 로 쓸 것)"))
    lines += ["", "[학습방 대화]", pf_convo_text(convos)]
    return PF_SYSTEM, "\n".join(lines)


def _pf_guard(value, corpus):
    """대화/입력에 없는 숫자가 섞여 있으면 통째로 '[숫자 입력 필요]' 로 바꾼다 (모델이 지어낸 숫자 차단)."""
    value = (value or "").strip()
    if not value or PF_NEED in value:
        return PF_NEED
    nums = re.findall(r"\d+(?:[.,]\d+)?", value)
    if not nums or any(n not in corpus for n in nums):
        return PF_NEED
    return value


def pf_from_model(result, convos, info):
    """구조화 출력(PortfolioDraft) → 편집용 dict. 사용자 입력 숫자를 우선하고, 근거 없는 숫자는 지운다."""
    system, human = pf_build_prompt(convos, info)
    corpus = human
    pages = pf_page_rooms(convos)
    typed = info.get("metrics") or {}
    d = {"example": False, "name": info.get("name", ""), "job": info.get("job", ""), "team": info.get("team", ""),
         "slogan": result.slogan.strip(), "metrics": [], "strengths": [], "projects": [],
         "stack_main": "\n".join(result.stack_main), "stack_exp": "\n".join(result.stack_exp)}
    for s in list(result.strengths)[:3]:
        d["strengths"].append({"title": s.title.strip(), "evidence": s.evidence.strip()})
    while len(d["strengths"]) < 3:
        d["strengths"].append({"title": "", "evidence": ""})
    for n, p in enumerate(list(result.projects)[:max(1, len(pages))]):
        room = pages[n]["name"] if n < len(pages) else p.room
        m = typed.get(room, {})
        contribution = m.get("contribution") or _pf_guard(p.contribution, corpus)
        if contribution != PF_NEED and "%" not in contribution:
            contribution += "%"
        alts = [{"option": a.option, "pros": a.pros, "cons": a.cons, "decision": a.decision} for a in p.alternatives][:3]
        while len(alts) < 3:
            alts.append({"option": "", "pros": "", "cons": "", "decision": ""})
        d["projects"].append({
            "room": room, "title": p.title.strip(), "who_pain": p.who_pain.strip(),
            "summary": "\n".join(list(p.summary)[:3]), "limits": p.limits.strip(), "alts": alts,
            "constraints": p.constraints.strip() or (("팀 " + info["team"]) if info.get("team") else ""),
            "role": p.role.strip(), "contribution": contribution,
            "metric_label": m.get("label") or p.metric_label.strip(),
            "before": m.get("before") or _pf_guard(p.before, corpus),
            "after": m.get("after") or _pf_guard(p.after, corpus),
            "methods": "\n".join(p.methods), "stuck": p.stuck.strip(), "ai_check": p.ai_check.strip(),
            "limitations": p.limitations.strip(), "keywords": "\n".join(p.keywords),
        })
    # 대표 수치: 프로젝트 지표를 먼저, 모자라면 모델이 뽑은 것 중 근거 있는 것만
    for p in d["projects"]:
        d["metrics"].append({"label": p["metric_label"], "before": p["before"], "after": p["after"]})
    seen = {m["label"] for m in d["metrics"]}
    for m in result.metrics:
        before, after = _pf_guard(m.before, corpus), _pf_guard(m.after, corpus)
        if m.label not in seen and PF_NEED not in (before, after):
            d["metrics"].append({"label": m.label.strip(), "before": before, "after": after})
    d["metrics"] = d["metrics"][:3]
    return d


def pf_generate(convos, info):
    """LLM 한 번 호출로 초안을 만든다 (구조화 출력)."""
    system, human = pf_build_prompt(convos, info)
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0).with_structured_output(PortfolioDraft)
    result = llm.invoke([("system", system), ("human", human)])
    return pf_from_model(result, convos, info)


# ---------------------------------------------------------------- 점검표 (파이썬으로 계산)
def _pf_num(value):
    value = str(value or "")
    return PF_NEED not in value and bool(re.search(r"\d", value))


def _pf_filled(value):
    value = str(value or "").strip()
    return len(value) >= 8 and PF_NEED not in value


def pf_has_need(d):
    """초안 어디든 '[숫자 입력 필요]' 가 남아 있는지."""
    return PF_NEED in repr(d)


def pf_checklist(d):
    """가이드의 7개 기준 → [(기준, 통과 여부, 채울 질문)]. 질문은 면접 예상 질문이기도 하다."""
    ps = d.get("projects") or []
    top = any(_pf_num(m.get("after")) and str(m.get("label", "")).strip() for m in d.get("metrics") or [])
    alts_ok = all(len([a for a in p["alts"] if a["option"].strip() and (a["pros"].strip() or a["cons"].strip())]) >= 2
                  and _pf_filled(p["constraints"]) for p in ps)
    return [
        ("10초 요약: 맨 위 3줄 안에 숫자로 된 대표 성과가 있다", bool(d.get("slogan", "").strip()) and top,
         "이 프로젝트의 대표 성과를 숫자 하나로 말하면 무엇인가요?"),
        ("한눈에 보이는 형식이다 (요약 1쪽 + 프로젝트별 1쪽)", True, ""),
        ("시각 자료와 생각 과정: 선택 이유(P)와 회고(R)가 채워져 있다",
         bool(ps) and all(_pf_filled(p["limits"]) and _pf_filled(p["stuck"]) for p in ps),
         "기존 방식의 한계는 무엇이었고, 어디에서 막혔다가 어떻게 풀었나요?"),
        ("문제 정의가 '누가 어떤 불편'으로 시작한다", bool(ps) and all(_pf_filled(p["who_pain"]) for p in ps),
         "누가 어떤 불편을 겪고 있었나요?"),
        ("대안 비교와 제약 조건이 있다", bool(ps) and alts_ok,
         "다른 방법은 무엇을 검토했고, 왜 이 방법을 골랐나요? 어떤 제약이 있었나요?"),
        ("Before → After 수치가 있다", bool(ps) and all(_pf_num(p["before"]) and _pf_num(p["after"]) for p in ps),
         "시작값과 결과값은 각각 얼마였고, 어떻게 쟀나요?"),
        ("AI 검증 기록과 기여도(%)가 있다",
         bool(ps) and all(_pf_filled(p["ai_check"]) and _pf_num(p["contribution"]) for p in ps),
         "AI가 만든 결과를 어떻게 검증했나요? 본인 기여도는 몇 %인가요?"),
    ]


# ---------------------------------------------------------------- 예시 (API 호출 없음, 숫자는 설명용)
PF_EXAMPLE = {
    "example": True,
    "name": "김에이블",
    "job": "AI 서비스 기획, DX 컨설턴트",
    "team": "4명",
    "slogan": "흩어진 학습 정보를 근거가 보이는 RAG 서비스로 풀어내는 DX 컨설턴트",
    "metrics": [
        {"label": "첫 답변 대기 시간", "before": "2분 이상", "after": "3초 이내"},
        {"label": "근거 페이지가 붙은 답변", "before": "0%", "after": "100%"},
        {"label": "동시 업로드 충돌 (5회 재현)", "before": "5회", "after": "0회"},
    ],
    "strengths": [
        {"title": "원인을 수치로 좁히는 문제 해결",
         "evidence": "미니프로젝트 4차: 구간별 시간을 재서 첫 답변 지연의 원인을 재벡터화로 특정하고 해결"},
        {"title": "근거를 남기는 AI 활용",
         "evidence": "LangChain RAG 학습방: 모든 답변에 백서 근거 페이지를 붙이고 원문과 대조해 검증"},
        {"title": "데이터를 의심하고 확인하는 습관",
         "evidence": "데이터 분석 학습방: 결측치 처리 전후 분포를 비교하고 집계 결과를 원본 행 수로 검산"},
    ],
    "stack_main": "Python: 미니프로젝트 4차 (RAG 파이프라인 구현)\n"
                  "LangChain, Chroma: 미니프로젝트 4차 (문서 검색과 구조화 출력)\n"
                  "Streamlit: 미니프로젝트 4차 (화면 구성과 배포)",
    "stack_exp": "pandas: 데이터 분석 학습방 (전처리와 집계 검증)\n"
                 "OpenAI API: LangChain RAG 학습방 (임베딩과 구조화 출력 실습)",
    "projects": [{
        "room": "미니프로젝트 4차",
        "title": "근거 페이지가 보이는 AIVLE School 학습 도우미 '쿠키 선배'",
        "who_pain": "AIVLE School 교육생은 출결, 장려금, 학습 방법이 궁금할 때마다 수십 쪽짜리 백서 PDF를 직접 뒤져야 했고, "
                    "찾은 내용이 맞는지 확인할 방법도 마땅치 않았습니다.",
        "summary": "백서 PDF를 올리면 rag_pipeline이 문서를 나누고 벡터화해, 질문에 근거 페이지와 함께 답합니다.\n"
                   "과목별 학습방에 교안 PDF를 연결해 그 주제만 깊게 물어볼 수 있습니다.\n"
                   "Streamlit 한 파일로 배포해 설치 없이 링크로 바로 씁니다.",
        "limits": "백서는 PDF 검색(Ctrl+F)으로만 찾을 수 있어 표현이 조금만 달라도 놓쳤고, 일반 챗봇에 물으면 "
                  "우리 과정에 없는 내용을 그럴듯하게 지어냈습니다.",
        "alts": [
            {"option": "PDF 직접 검색", "pros": "추가 개발이 필요 없음", "cons": "표현이 다르면 못 찾고 요약이 안 됨",
             "decision": "제외"},
            {"option": "일반 LLM 챗봇", "pros": "답변이 자연스러움", "cons": "백서에 없는 내용을 지어내고 근거 확인 불가",
             "decision": "제외"},
            {"option": "RAG (백서 검색 + 근거 표시)", "pros": "백서 문장에 기반해 답하고 근거 페이지를 표시",
             "cons": "처음 벡터화에 시간이 들고 chunk 설정에 민감", "decision": "선택"},
        ],
        "constraints": "개발 기간 3일, 팀 4명, 무료 배포 환경(Streamlit), 교안 PDF는 외부 공유가 안 되어 세션 안에서만 처리",
        "role": "RAG 파이프라인 구현과 응답 속도 개선 담당 (4인 팀)",
        "contribution": "40%",
        "metric_label": "첫 답변 대기 시간",
        "before": "2분 이상",
        "after": "3초 이내",
        "methods": "미리 만든 chroma_db 재사용: 서버 시작마다 하던 백서 재벡터화를 없애 대기 시간 대부분을 줄임\n"
                   "파일 해시 비교와 캐시: 백서가 바뀐 경우에만 다시 벡터화해 재시작 뒤에도 바로 응답\n"
                   "세션별 Chroma 컬렉션: 동시 접속자의 업로드가 서로 지워지던 충돌을 0회로 줄임",
        "stuck": "서버를 켤 때마다 첫 답변이 2분 넘게 걸렸습니다. 구간별 시간을 재 보니 LLM 호출이 아니라 백서 재벡터화가 "
                 "원인이었고, 저장된 chroma_db 컬렉션이 있으면 임베딩을 건너뛰고 바로 불러오도록 바꿔 해결했습니다. "
                 "비밀번호가 걸린 교안 PDF는 로더에서 오류가 나서, 수집 전에 잠금을 푸는 단계를 추가했습니다.",
        "ai_check": "AI가 제안한 코드는 그대로 쓰지 않고, 질문 20개 세트로 답변의 근거 페이지를 백서 원문과 대조했습니다. "
                    "근거가 맞지 않은 3건은 chunk_size와 k 값을 조정한 뒤 다시 확인했습니다.",
        "limitations": "표와 이미지 안의 내용은 검색이 약하고, 백서가 개정되면 다시 벡터화해야 합니다. "
                       "다음에는 표 추출과 자동 재색인을 붙이고 싶습니다.",
        "keywords": "서비스 기획: 사용자 불편에서 출발해 '근거 표시'를 핵심 요구로 정의\n"
                    "성능 개선: 원인 구간을 측정한 뒤 대기 시간을 단축\n"
                    "AI 결과 검증: 질문 세트로 근거 페이지를 원문과 대조\n"
                    "RAG, LangChain, Streamlit: 설계부터 배포까지 직접 구현",
    }],
}


def pf_example():
    return copy.deepcopy(PF_EXAMPLE)


# ---------------------------------------------------------------- 내보내기 (마크다운 / HTML)
def _pf_lines(text):
    return [x.strip() for x in str(text or "").splitlines() if x.strip()]


def _pf_pair(line):
    """'기술: 연결 프로젝트' → (기술, 연결 프로젝트)."""
    head, sep, tail = line.partition(":")
    if sep:
        return head.strip(), tail.strip()
    return line.strip(), ""


def pf_markdown(d):
    tag = ""
    if d.get("example"):
        tag = " (예시)"
    out = ["# " + (d.get("name") or "포트폴리오") + tag, ""]
    if d.get("job"):
        out += ["희망 직무: " + d["job"], ""]
    out += ["## 10초 요약", "", "**" + d.get("slogan", "") + "**", ""]
    for m in d.get("metrics") or []:
        out.append("- " + m["label"] + ": " + m["before"] + " → **" + m["after"] + "**")
    out += ["", "### 핵심 강점", ""]
    for s in d.get("strengths") or []:
        out.append("- **" + s["title"] + "**: " + s["evidence"])
    out += ["", "### 기술 스택", ""]
    for label, key in (("주력", "stack_main"), ("경험", "stack_exp")):
        out.append("- " + label + ": " + ", ".join(_pf_lines(d.get(key))))
    for n, p in enumerate(d.get("projects") or [], 1):
        out += ["", "---", "", "## 프로젝트 " + str(n) + ". " + p["title"], "",
                "### S 문제 정의", "", p["who_pain"], ""]
        out += ["- " + x for x in _pf_lines(p["summary"])]
        out += ["", "### P 선택 이유", "", "기존 방식의 한계: " + p["limits"], "",
                "| 대안 | 장점 | 한계 | 판단 |", "| --- | --- | --- | --- |"]
        for a in p["alts"]:
            if a["option"].strip():
                out.append("| " + " | ".join([a["option"], a["pros"], a["cons"], a["decision"]]) + " |")
        out += ["", "제약 조건: " + p["constraints"], "", "### A 실행과 성과", "",
                "- 내 역할: " + p["role"], "- 기여도: " + p["contribution"],
                "- " + p["metric_label"] + ": " + p["before"] + " → **" + p["after"] + "**", "", "방법별 기여", ""]
        out += ["- " + x for x in _pf_lines(p["methods"])]
        out += ["", "### R 회고와 검증", "", "- 막힌 지점과 해결: " + p["stuck"], "- AI 검증 기록: " + p["ai_check"],
                "- 한계와 다음 단계: " + p["limitations"], "", "### K 직무 키워드", ""]
        out += ["- " + x for x in _pf_lines(p["keywords"])]
    out += ["", "---", "", "## 점검표", ""]
    for label, ok, ask in pf_checklist(d):
        mark = "O"
        if not ok:
            mark = "X"
        line = "- [" + mark + "] " + label
        if not ok and ask:
            line += " (채울 질문: " + ask + ")"
        out.append(line)
    foot = PF_FOOTER
    if d.get("example"):
        foot += " (예시: 숫자는 설명을 위한 값입니다)"
    out += ["", foot, ""]
    return "\n".join(out)


PF_HTML_CSS = """
:root{--primary:#5B4BE0;--primary-soft:#EEEBFF;--text:#1E1B3A;--text-sub:#5E6278;--muted:#94A3B8;
  --surface:#FFFFFF;--bg:#F6F5FF;--border:#E6E4F2;--cookie:#F7BC62;--cookie-deep:#B45309;--cookie-soft:#FFF1DE;
  --ok:#1E9E6A;--ok-soft:#E3F6EC;--font:'Noto Sans KR',sans-serif;}
*{box-sizing:border-box;}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--font);font-size:13.5px;line-height:1.65;
  word-break:keep-all;overflow-wrap:anywhere;}
[contenteditable]{outline:none;border-radius:4px;}
[contenteditable]:hover{background:var(--bg);}
[contenteditable]:focus{background:var(--primary-soft);}
mark.need{background:var(--cookie);color:var(--text);padding:0 4px;border-radius:3px;font-weight:700;}
.tip{max-width:820px;margin:20px auto 0;padding:10px 16px;border:1px dashed var(--border);border-radius:10px;
  background:var(--surface);color:var(--text-sub);font-size:12.5px;}
.tip b{color:var(--primary);}
.page{max-width:820px;margin:20px auto;background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:44px 48px;}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:16px;border-bottom:2px solid var(--text);
  padding-bottom:10px;}
.top .who{font-size:15px;font-weight:800;}
.top .job{font-size:12.5px;color:var(--text-sub);text-align:right;}
.badge{display:inline-block;margin-left:8px;padding:1px 9px;border-radius:999px;background:var(--cookie-soft);
  color:var(--cookie-deep);font-size:11px;font-weight:800;vertical-align:middle;}
.eyebrow{font-size:11px;font-weight:800;letter-spacing:1.6px;color:var(--primary);margin:26px 0 6px;}
.slogan{font-size:29px;line-height:1.36;font-weight:800;letter-spacing:-.5px;margin:0;}
.metrics{display:grid;grid-template-columns:repeat(var(--n),1fr);gap:0;margin-top:26px;border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);}
.metric{padding:16px 16px 18px;}
.metric + .metric{border-left:1px solid var(--border);}
.metric .lab{font-size:12px;font-weight:700;color:var(--text-sub);}
.ba{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 8px;margin-top:6px;}
.ba .b{font-size:15px;font-weight:500;color:var(--muted);}
.ba .ar{font-size:15px;color:var(--muted);}
.ba .a{font-size:31px;line-height:1.15;font-weight:800;color:var(--primary);letter-spacing:-.5px;}
h2{font-size:12px;font-weight:800;letter-spacing:1.2px;color:var(--text-sub);margin:28px 0 10px;}
.strengths{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;}
.strength .no{font-size:11px;font-weight:800;color:var(--primary);}
.strength b{display:block;font-size:15px;line-height:1.4;margin:2px 0 6px;}
.strength p{margin:0;font-size:12.5px;color:var(--text-sub);}
.stack{display:grid;grid-template-columns:64px 1fr;gap:10px 14px;align-items:start;}
.stack .lv{font-size:12px;font-weight:800;padding-top:5px;}
.stack ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px;}
.stack li{border:1px solid var(--border);border-radius:10px;padding:5px 12px;font-size:12.5px;}
.stack li b{font-weight:700;}
.stack li span{color:var(--text-sub);}
.ptitle{font-size:23px;line-height:1.38;font-weight:800;letter-spacing:-.4px;margin:0;}
.block{display:grid;grid-template-columns:104px 1fr;gap:18px;padding:15px 0;border-top:1px solid var(--border);
  break-inside:avoid;}
.block:first-of-type{margin-top:20px;}
.block .k{display:flex;flex-direction:column;gap:2px;}
.block .k i{font-style:normal;font-size:24px;line-height:1;font-weight:800;color:var(--primary);}
.block .k span{font-size:12px;font-weight:700;color:var(--text-sub);}
.block p{margin:0 0 6px;}
.block p:last-child{margin-bottom:0;}
.block .lead{font-size:14.5px;font-weight:700;line-height:1.6;}
.block ul{margin:4px 0 0;padding-left:18px;}
.block li{margin:2px 0;}
.lbl{font-size:11.5px;font-weight:800;color:var(--text-sub);margin-right:6px;}
table{width:100%;border-collapse:collapse;margin:8px 0;font-size:12.5px;table-layout:fixed;}
th{font-size:11.5px;font-weight:800;color:var(--text-sub);text-align:left;padding:6px 8px;border-bottom:1px solid var(--text);}
td{padding:7px 8px;border-bottom:1px solid var(--border);vertical-align:top;}
th:first-child,td:first-child{width:26%;font-weight:700;}
th:last-child,td:last-child{width:58px;}
tr.pick td{background:var(--primary-soft);}
tr.pick td:last-child{color:var(--primary);font-weight:800;}
.result{display:grid;grid-template-columns:1fr 150px;gap:18px;align-items:end;margin-bottom:8px;}
.result .lab{font-size:12px;font-weight:700;color:var(--text-sub);}
.result .contrib{text-align:right;}
.result .contrib .a{font-size:31px;line-height:1.15;font-weight:800;letter-spacing:-.5px;}
.kw{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px;}
.kw li{margin:0;font-size:12.5px;color:var(--text-sub);}
.kw li b{display:block;color:var(--text);font-size:13px;}
.check{list-style:none;margin:0;padding:0;}
.check li{display:grid;grid-template-columns:26px 1fr;gap:10px;padding:7px 0;border-top:1px solid var(--border);
  font-size:12.5px;}
.check .m{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:800;background:var(--ok-soft);color:var(--ok);}
.check .x .m{background:var(--cookie-soft);color:var(--cookie-deep);}
.check small{display:block;color:var(--cookie-deep);font-size:12px;}
.foot{margin-top:26px;padding-top:10px;border-top:1px solid var(--border);font-size:11px;color:var(--muted);
  display:flex;justify-content:space-between;gap:12px;}
@page{size:A4;margin:14mm 15mm;}
@media print{
  body{background:var(--surface);font-size:12px;}
  .tip{display:none;}
  .page{max-width:none;margin:0;border:0;border-radius:0;padding:0;}
  .page + .page{break-before:page;}
  .page.checkpage{break-before:auto;margin-top:22px;break-inside:avoid;}
  [contenteditable]:hover,[contenteditable]:focus{background:transparent;}
  mark.need{background:var(--cookie);}
}
@media (max-width:640px){
  .page{padding:24px 18px;margin:12px;}
  .tip{margin:12px 12px 0;}
  .slogan{font-size:23px;}
  .metrics,.strengths,.kw{grid-template-columns:1fr;}
  .metric + .metric{border-left:0;border-top:1px solid var(--border);}
  .block{grid-template-columns:1fr;gap:8px;}
  .result{grid-template-columns:1fr;}
  .result .contrib{text-align:left;}
}
"""


def _pf_h(text):
    """HTML 이스케이프 + 남은 '[숫자 입력 필요]' 노란 강조."""
    return html.escape(str(text or "")).replace(html.escape(PF_NEED), '<mark class="need">' + PF_NEED + "</mark>")


def _pf_ed(tag, text, cls=""):
    """클릭해서 고칠 수 있는 텍스트 요소."""
    attr = ""
    if cls:
        attr = ' class="' + cls + '"'
    return "<" + tag + attr + ' contenteditable="true">' + _pf_h(text) + "</" + tag + ">"


def _pf_foot(d, page):
    foot = PF_FOOTER
    if d.get("example"):
        foot += " (예시: 숫자는 설명을 위한 값입니다)"
    return '<div class="foot"><span>' + html.escape(foot) + "</span><span>" + page + "</span></div>"


def _pf_block(letter, name, body):
    return ('<section class="block"><div class="k"><i>' + letter + "</i><span>" + name + "</span></div><div>"
            + body + "</div></section>")


def _pf_project_html(d, p, n, total):
    rows = ""
    for a in p["alts"]:
        if not a["option"].strip():
            continue
        cls = ""
        if "선택" in a["decision"]:
            cls = ' class="pick"'
        rows += ("<tr" + cls + ">" + _pf_ed("td", a["option"]) + _pf_ed("td", a["pros"]) + _pf_ed("td", a["cons"])
                 + _pf_ed("td", a["decision"]) + "</tr>")
    table = ""
    if rows:
        table = "<table><thead><tr><th>대안</th><th>장점</th><th>한계</th><th>판단</th></tr></thead><tbody>" + rows + "</tbody></table>"
    kws = ""
    for line in _pf_lines(p["keywords"]):
        head, tail = _pf_pair(line)
        kws += "<li>" + _pf_ed("b", head) + _pf_ed("span", tail) + "</li>"
    s = (_pf_ed("p", p["who_pain"], "lead") + "<ul>" + "".join(_pf_ed("li", x) for x in _pf_lines(p["summary"])) + "</ul>")
    pp = ('<p><span class="lbl">기존 방식의 한계</span>' + _pf_ed("span", p["limits"]) + "</p>" + table
          + '<p><span class="lbl">제약 조건</span>' + _pf_ed("span", p["constraints"]) + "</p>")
    a = ('<div class="result"><div><div class="lab">' + _pf_h(p["metric_label"]) + '</div><div class="ba">'
         + _pf_ed("span", p["before"], "b") + '<span class="ar">→</span>' + _pf_ed("span", p["after"], "a")
         + '</div></div><div class="contrib"><div class="lab">내 기여도</div>' + _pf_ed("div", p["contribution"], "a")
         + '</div></div><p><span class="lbl">내 역할</span>' + _pf_ed("span", p["role"]) + "</p>"
         + '<p><span class="lbl">방법별 기여</span></p><ul>' + "".join(_pf_ed("li", x) for x in _pf_lines(p["methods"])) + "</ul>")
    r = ('<p><span class="lbl">막힌 지점과 해결</span>' + _pf_ed("span", p["stuck"]) + "</p>"
         + '<p><span class="lbl">AI 검증 기록</span>' + _pf_ed("span", p["ai_check"]) + "</p>"
         + '<p><span class="lbl">한계와 다음 단계</span>' + _pf_ed("span", p["limitations"]) + "</p>")
    k = '<ul class="kw">' + kws + "</ul>"
    bodies = [s, pp, a, r, k]
    blocks = "".join(_pf_block(letter, name, bodies[i]) for i, (letter, name) in enumerate(PF_SPARK))
    return ('<article class="page project"><div class="eyebrow" style="margin-top:0">PROJECT ' + str(n).zfill(2)
            + " | " + html.escape(p.get("room", "")) + "</div>" + _pf_ed("h1", p["title"], "ptitle") + blocks
            + _pf_foot(d, str(n + 1) + " / " + str(total)) + "</article>")


def pf_html(d):
    """한 파일로 완결되는 A4 인쇄용 HTML (텍스트는 브라우저에서 바로 고칠 수 있음)."""
    badge = ""
    if d.get("example"):
        badge = '<span class="badge">예시</span>'
    projects = d.get("projects") or []
    total = len(projects) + 2  # 10초 요약 + 프로젝트 장 + 점검표
    metrics = d.get("metrics") or []
    cells = ""
    for m in metrics:
        cells += ('<div class="metric">' + _pf_ed("div", m["label"], "lab") + '<div class="ba">' + _pf_ed("span", m["before"], "b")
                  + '<span class="ar">→</span>' + _pf_ed("span", m["after"], "a") + "</div></div>")
    strengths = ""
    for n, s in enumerate(d.get("strengths") or [], 1):
        strengths += ('<div class="strength"><span class="no">' + str(n).zfill(2) + "</span>" + _pf_ed("b", s["title"])
                      + _pf_ed("p", s["evidence"]) + "</div>")
    stack = ""
    for label, key in (("주력", "stack_main"), ("경험", "stack_exp")):
        items = ""
        for line in _pf_lines(d.get(key)):
            head, tail = _pf_pair(line)
            items += '<li contenteditable="true"><b>' + _pf_h(head) + "</b> <span>" + _pf_h(tail) + "</span></li>"
        stack += '<div class="lv">' + label + "</div><ul>" + items + "</ul>"
    checks = ""
    for label, ok, ask in pf_checklist(d):
        cls, mark, extra = "", "O", ""
        if not ok:
            cls, mark = ' class="x"', "X"
            extra = "<small>채울 질문: " + html.escape(ask) + "</small>"
        checks += "<li" + cls + '><span class="m">' + mark + "</span><div>" + html.escape(label) + extra + "</div></li>"
    first = ('<article class="page"><div class="top"><div class="who">' + _pf_ed("span", d.get("name") or "이름") + badge
             + '</div><div class="job">희망 직무 ' + _pf_ed("b", d.get("job") or "직무를 적어 주세요") + "</div></div>"
             + '<div class="eyebrow">10초 요약</div>' + _pf_ed("h1", d.get("slogan", ""), "slogan")
             + '<div class="metrics" style="--n:' + str(max(1, len(metrics))) + '">' + cells + "</div>"
             + "<h2>핵심 강점</h2>" + '<div class="strengths">' + strengths + "</div>"
             + "<h2>기술 스택</h2>" + '<div class="stack">' + stack + "</div>"
             + _pf_foot(d, "1 / " + str(total)) + "</article>")
    pages = "".join(_pf_project_html(d, p, n, total) for n, p in enumerate(projects, 1))
    check = ('<article class="page checkpage"><h2 style="margin-top:0">점검표' + badge + '</h2><ul class="check">' + checks
             + "</ul>" + _pf_foot(d, str(total) + " / " + str(total)) + "</article>")
    title = html.escape((d.get("name") or "포트폴리오") + " 포트폴리오")
    return ('<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1"><title>' + title + "</title>"
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet">'
            "<style>" + PF_HTML_CSS + "</style></head><body>"
            '<div class="tip"><b>고치는 방법</b> 글자를 클릭하면 바로 고칠 수 있어요. 다 고친 뒤 Ctrl+P 를 눌러 PDF 로 저장하세요. '
            "여기서 고친 내용은 이 HTML 파일에 저장되지 않아요.</div>"
            + first + pages + check + "</body></html>\n")



# ======================================================================
# 화면 구성
# ======================================================================
# 화면 구성: 사이드바, 홈, 대화, 학습방, 다이얼로그, 슬래시 명령어.
import copy
import datetime
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
    ("/포트폴리오", "학습방 대화로 포트폴리오 초안 만들기", "work"),
    ("/공식문서", "라이브러리 공식 문서 바로 열기", "menu_book"),
    ("/새대화", "새 대화 시작", "add_comment"),
]
# 공식문서 바로가기 (슬래시 팝업의 하위 목록과 파이썬 폴백이 함께 쓰는 단일 출처).
# 사이트 추가 = 아래에 한 줄: (이름, 명령어, 주소, (별칭, ...))
DOC_SITES = [
    ("Seaborn", "/seaborn", "https://seaborn.pydata.org/", ()),
    ("pandas", "/pandas", "https://pandas.pydata.org/", ()),
    ("Streamlit", "/streamlit", "https://docs.streamlit.io/", ()),
    ("Python", "/python", "https://docs.python.org/ko/3/", ()),
    ("scikit-learn", "/scikit", "https://scikit-learn.org/", ("/scikitlearn", "/scikit-learn")),
    ("TensorFlow", "/tensorflow", "https://www.tensorflow.org/", ()),
    ("NumPy", "/numpy", "https://numpy.org/", ()),
]


def doc_site(cmd):
    """명령어(별칭 포함, 대소문자 무시) → (이름, 주소) 또는 None."""
    cmd = (cmd or "").lower()
    for name, main, url, aliases in DOC_SITES:
        if cmd == main or cmd in aliases:
            return name, url
    return None
PLAN_TZ = datetime.timezone(datetime.timedelta(hours=9))  # Asia/Seoul (서머타임 없음, tzdata 불필요)
PLAN_WEEKDAYS = "월화수목금토일"


def plan_day(d):
    return str(d.month) + "월 " + str(d.day) + "일(" + PLAN_WEEKDAYS[d.weekday()] + ")"


def plan_request(now=None):
    """/계획 질문과 기준 줄을 만든다: 오늘 날짜(한국 시간) + 커리큘럼의 '지금' 항목과 다음 항목."""
    today = (now or datetime.datetime.now(PLAN_TZ)).date()
    days = [plan_day(today + datetime.timedelta(days=n)) for n in range(7)]
    flat = []
    for n, step in enumerate(st.session_state.curriculum["steps"], 1):
        for it in step["items"]:
            flat.append((n, step, it))
    pos = next((i for i, row in enumerate(flat) if row[2].get("current")), None)
    ref = "기준: " + days[0]
    ask = "오늘은 " + days[0] + "이에요. "
    if pos is not None:
        n, step, it = flat[pos]
        kind = ITEM_TYPES[item_type(it)]["label"]
        ref += ", 지금 " + it["name"]
        ask += ("저는 지금 STEP " + str(n) + " '" + step["name"] + "'의 '" + it["name"]
                + "'(" + kind + ") 과정을 하고 있어요. ")
        nxt = ["'" + row[2]["name"] + "'" for row in flat[pos + 1:pos + 3]]
        if nxt:
            ask += "그다음 과정은 " + ", ".join(nxt) + " 순서예요. "
    ask += ("백서에 나온 학습 전략과 선배들의 공부 루틴을 바탕으로, 오늘부터 7일 동안(" + days[0] + "부터 " + days[6]
            + "까지)의 개인 학습 계획을 날짜별로 짜 주세요. "
            "날짜는 " + ", ".join(days) + " 순서로 하나씩 쓰고, 날마다 지금 과정과 다음 과정에 맞춰 무엇을 할지 구체적으로 적어 주세요. "
            "이번 답변은 번호 목록 개수 제한 없이 7일을 모두 써 주세요. "
            "모든 문장은 '~해요', '~해 보세요'처럼 해요체로 쓰고 반말은 쓰지 마세요.")
    return ask, ref


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
    # 1) 저장된 chroma_db 의 백서 컬렉션을 그대로 사용 (Colab에서 만들어 GitHub에 올린 것).
    #    캐시 키가 컬렉션 id 라서, chroma_db 가 다시 만들어지면(id 변경) 자동으로 새로 불러온다.
    cid = collection_id("aivle_docs")
    if cid:
        return _load_saved_whitepaper(cid)
    # 2) 컬렉션이 없을 때만 PDF 로 한 번 만든다 (이후 실행부터는 1번 경로)
    path = WHITEPAPER
    if path.exists():
        with st.spinner("문서를 읽고 벡터화하는 중이에요."):
            return _load_whitepaper(_file_hash(str(path), path.stat().st_mtime), str(path))
    raise RuntimeError("백서가 아직 연결되지 않았어요. 입력창의 + 버튼으로 백서 PDF를 올려 주세요.")


@st.cache_resource(show_spinner=False)
def _load_saved_whitepaper(cid):
    return load_collection("aivle_docs")


def session_collection(base):
    """업로드 문서는 사용자(세션)마다 다른 컬렉션에 저장: 여러 명이 동시에 써도 서로의 컬렉션을 초기화하지 않게."""
    ss = st.session_state
    if "sid" not in ss:
        ss.sid = new_id()
    return base + "_" + ss.sid


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
        _generate_once(msgs, question)
    except Exception as first_err:
        err = first_err
        if "does not exist" in str(first_err):
            # 안전장치: 그래도 옛 컬렉션을 가리키면 캐시를 비우고 한 번만 다시 시도
            _load_whitepaper.clear()
            _load_saved_whitepaper.clear()
            try:
                _generate_once(msgs, question)
                return
            except Exception as second_err:
                err = second_err
        msgs.append(note("답변을 만들다가 문제가 생겼어요", "잠시 뒤 다시 시도해 주세요. (" + str(err)[:200] + ")"))


def _generate_once(msgs, question):
    ss = st.session_state
    last = msgs[-1]
    if True:
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
        if last.get("ref") and msgs[-1].get("answer"):
            msgs[-1]["ref"] = last["ref"]


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
    ingest(file.name, file.getvalue(), msgs)


def ingest(name, data, msgs, password=None):
    """PDF 바이트 → 임시 파일(잠겨 있으면 풀기) → rag_pipeline(경로). 잠긴 PDF는 비밀번호 입력 카드를 띄운다."""
    ss = st.session_state
    in_room = ss.view == "room" and ss.current_room
    try:
        with st.spinner("문서를 읽고 벡터화하는 중이에요. 교안처럼 페이지가 많으면 몇 분 걸릴 수 있어요."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(data)
            path = unlock_pdf(tmp.name, password)
            if in_room:
                rid = ss.current_room
                _, retriever = rag_pipeline(path, collection_name=session_collection("room_" + rid), with_retriever=True)
                ss.room_retrievers[rid] = retriever
                room(rid)["doc_name"] = name
                msgs.append(note("교안을 연결했어요", "「" + name + "」 을 이 학습방의 교안으로 읽었어요."))
            else:
                chain, retriever = rag_pipeline(path, collection_name=session_collection("upload"), with_retriever=True)
                ss.upload_chain, ss.upload_retriever = chain, retriever
                ss.doc_name = name
                msgs.append(note("문서를 연결했어요", "이제부터 「" + name + "」 을 근거로 답해요."))
        ss.locked_pdf = None
    except PdfLocked as e:
        ss.locked_pdf = {"name": name, "data": data}
        msgs.append({"role": "assistant", "card": "unlock", "name": name, "msg": str(e)})
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
    if cmd == "/포트폴리오":
        ss.open_portfolio = True
        return
    msgs = current_messages(create_title="명령어 " + cmd)
    if cmd == "/계획":
        ask, ref = plan_request()
        msgs.append({"role": "user", "text": "/계획", "ask": ask, "ref": ref})
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
    elif cmd == "/공식문서" or doc_site(cmd):
        # 팝업을 거치지 않고 명령어를 그대로 보낸 경우: 링크 카드로 답한다
        msgs.append({"role": "user", "text": cmd})
        msgs.append({"role": "assistant", "card": "docs", "site": cmd})
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


# 슬래시 메뉴: st.components.v2 의 JS 전용 컴포넌트 (패키지/빌드 없음).
# 입력창(.st-key-input_* textarea)에 '/' 로 시작하는 글자를 치면 명령어 팝업(.ck-slash)을 띄우고,
# ↑↓/Enter/클릭으로 고르면 입력창을 비우고 trigger 값 'cmd' 로 파이썬에 돌려준다.
SLASH_JS = r"""
export default function (component) {
  const { setTriggerValue } = component;
  const CMDS = __CMDS__;
  const SITES = __SITES__;  // [이름, 명령어, 주소, [별칭]]
  const DOCS = '/공식문서';
  const sv = (p) => '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + p + '</svg>';
  const ICON = {
    '/커리큘럼': sv('<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>'),
    '/추천': sv('<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>'),
    '/쿠키': sv('<path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01"/><path d="M16 15.5v.01"/><path d="M12 12v.01"/><path d="M11 17v.01"/><path d="M7 14v.01"/>'),
    '/계획': sv('<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>'),
    '/요약': sv('<path d="M8 6h13"/><path d="M8 12h13"/><path d="M8 18h13"/><path d="M3 6h.01"/><path d="M3 12h.01"/><path d="M3 18h.01"/>'),
    '/새대화': sv('<path d="M12 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.4 2.6a2.1 2.1 0 0 1 3 3L12 15l-4 1 1-4z"/>'),
    '/포트폴리오': sv('<rect width="20" height="14" x="2" y="6" rx="2"/><path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>'),
    '/공식문서': sv('<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>'),
  };
  const SITE_IC = sv('<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>');
  if (window.__ckSlashCleanup) window.__ckSlashCleanup();
  const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
  // items: {cmd, desc, url}. url 이 있으면 공식문서 사이트 줄. mode: 'cmd'(명령어) | 'docs'(공식문서 하위 목록)
  let ta = null, box = null, items = [], sel = 0, mode = 'cmd';
  const host = (u) => { try { return new URL(u).host; } catch (e) { return u; } };
  const cmdRow = (c) => ({ cmd: c[0], desc: c[1], url: '' });
  const siteRow = (s) => ({ cmd: s[1], desc: s[0] + ' 공식 문서, ' + host(s[2]), url: s[2] });
  const isDocs = (c) => !!c && !c.url && c.cmd === DOCS;
  const filter = (v) => {
    const out = CMDS.filter((c) => c[0].startsWith(v)).map(cmdRow);
    const q = v.toLowerCase();
    if (v.length > 1) SITES.forEach((s) => { if ([s[1]].concat(s[3]).some((a) => a.startsWith(q))) out.push(siteRow(s)); });
    return out;
  };
  const close = () => { mode = 'cmd'; if (box) { box.remove(); box = null; } };
  const mark = () => { if (box) box.querySelectorAll('.ck-slash-row').forEach((x, j) => x.classList.toggle('on', j === sel)); };
  const choose = (i) => {
    const c = items[i];
    if (!c || !ta) return;
    if (isDocs(c)) { mode = 'docs'; items = SITES.map(siteRow); sel = 0; render(); return; }
    close();
    setter.call(ta, '');
    ta.dispatchEvent(new Event('input', { bubbles: true }));
    if (c.url) { window.open(c.url, '_blank', 'noopener'); return; }
    setTriggerValue('cmd', c.cmd);
  };
  const back = () => {
    mode = 'cmd';
    items = filter(/^\/\S*$/.test(ta.value) ? ta.value : '/');
    sel = Math.max(0, items.findIndex(isDocs));
    if (items.length) { render(); } else { close(); }
  };
  const render = () => {
    if (!box) {
      box = document.createElement('div');
      box.className = 'ck-slash';
      box.setAttribute('role', 'listbox');
      document.body.appendChild(box);
    }
    const wrap = ta.closest('[class*="st-key-input_"]') || ta;
    const r = wrap.getBoundingClientRect();
    box.style.left = r.left + 'px';
    box.style.width = r.width + 'px';
    box.style.bottom = (window.innerHeight - r.top + 8) + 'px';
    box.innerHTML = '<div class="ck-slash-h">' + (mode === 'docs' ? '공식문서' : '명령어') + '</div>' + items.map((c, i) =>
      '<div class="ck-slash-row" role="option" data-i="' + i + '"><span class="ck-slash-ic">' + (c.url ? SITE_IC : (ICON[c.cmd] || '')) +
      '</span><span class="ck-slash-t"><b>' + c.cmd + (isDocs(c) ? ' ›' : '') + '</b><small>' + c.desc + '</small></span></div>').join('') +
      '<div class="ck-slash-f">' + (mode === 'docs' ? '↑↓ 이동, Enter 새 탭으로 열기, ← 뒤로' : '↑↓ 이동, Enter 선택, Esc 닫기') + '</div>';
    box.querySelectorAll('.ck-slash-row').forEach((el) => {
      el.addEventListener('mousedown', (e) => { e.preventDefault(); choose(+el.dataset.i); });
      el.addEventListener('mouseenter', () => { sel = +el.dataset.i; mark(); });
    });
    mark();
  };
  const onInput = () => {
    const v = ta.value;
    if (/^\/\S*$/.test(v)) {
      mode = 'cmd';
      items = filter(v);
      sel = 0;
      if (items.length) { render(); } else { close(); }
    } else {
      close();
    }
  };
  const onKey = (e) => {
    if (!box || e.isComposing) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); e.stopPropagation();
      sel = (sel + (e.key === 'ArrowDown' ? 1 : items.length - 1)) % items.length;
      mark();
    } else if ((e.key === 'Enter' && !e.shiftKey) || e.key === 'Tab') {
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      choose(sel);
    } else if (e.key === 'ArrowRight' && mode === 'cmd' && isDocs(items[sel])) {
      e.preventDefault(); e.stopPropagation();
      choose(sel);
    } else if (mode === 'docs' && (e.key === 'ArrowLeft' || e.key === 'Escape')) {
      e.preventDefault(); e.stopPropagation();
      back();
    } else if (e.key === 'Escape') {
      e.preventDefault(); close();
    }
  };
  const onBlur = () => setTimeout(close, 150);
  const unbind = () => {
    if (!ta) return;
    ta.removeEventListener('input', onInput);
    ta.removeEventListener('keydown', onKey, true);
    ta.removeEventListener('blur', onBlur);
  };
  const bind = () => {
    const t = document.querySelector('[class*="st-key-input_"] textarea');
    if (t === ta) return;
    unbind(); close();
    ta = t;
    if (!ta) return;
    ta.addEventListener('input', onInput);
    ta.addEventListener('keydown', onKey, true);
    ta.addEventListener('blur', onBlur);
  };
  bind();
  const timer = setInterval(bind, 700);
  const onResize = () => { if (box && ta) render(); };
  window.addEventListener('resize', onResize);
  const cleanup = () => { clearInterval(timer); unbind(); close(); window.removeEventListener('resize', onResize); };
  window.__ckSlashCleanup = cleanup;
  return cleanup;
}
""".replace("__CMDS__", json.dumps([[c, d] for c, d, _ in COMMANDS], ensure_ascii=False)).replace(
    "__SITES__", json.dumps([[n, c, u, list(a)] for n, c, u, a in DOC_SITES], ensure_ascii=False))
slash_menu = st.components.v2.component("ck_slash_menu", js=SLASH_JS)


def _slash_noop():
    return None


def chat_input(key):
    # 슬래시 메뉴 컴포넌트 (화면에는 보이지 않음): 팝업에서 고른 명령어를 바로 실행
    with st.container(key="slashmenu"):
        picked = slash_menu(key="slash_" + key, on_cmd_change=_slash_noop)
    cmd = picked.get("cmd") if picked else None
    if cmd:
        run_command(cmd)
        st.rerun()
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


# 편집 행 드래그 정렬: st.components.v2 의 JS 전용 컴포넌트 (패키지/빌드 없음).
# 화면에 그려진 실제 Streamlit 행(.st-key-edrow_<id>)의 손잡이(.ck-grip)를 끌면
# 새 순서(id 목록)를 trigger 값 'order' 로 파이썬에 돌려준다.
SORT_JS = """
export default function (component) {
  const { setTriggerValue } = component;
  const ROW = '[class*="st-key-edrow_"]';
  let drag = null;
  const rows = () => Array.from(document.querySelectorAll(ROW));
  const idOf = (row) => {
    const grip = row.querySelector('[data-iid]');
    return grip ? grip.getAttribute('data-iid') : null;
  };
  const clear = () => {
    rows().forEach((r) => {
      r.classList.remove('ck-dragging', 'ck-drop-before', 'ck-drop-after');
      r.style.transform = '';
    });
    document.body.style.userSelect = '';
  };
  const down = (e) => {
    const grip = e.target && e.target.closest ? e.target.closest('.ck-grip') : null;
    if (!grip || e.button > 0) { return; }
    const row = grip.closest(ROW);
    if (!row) { return; }
    e.preventDefault();
    drag = { row: row, startY: e.clientY, target: null, after: false };
    row.classList.add('ck-dragging');
    document.body.style.userSelect = 'none';
  };
  const move = (e) => {
    if (!drag) { return; }
    e.preventDefault();
    drag.row.style.transform = 'translateY(' + (e.clientY - drag.startY) + 'px)';
    const others = rows().filter((r) => r !== drag.row);
    others.forEach((r) => r.classList.remove('ck-drop-before', 'ck-drop-after'));
    drag.target = null;
    for (const r of others) {
      const box = r.getBoundingClientRect();
      if (e.clientY < box.top + box.height / 2) { drag.target = r; drag.after = false; break; }
    }
    if (!drag.target && others.length) { drag.target = others[others.length - 1]; drag.after = true; }
    if (drag.target) { drag.target.classList.add(drag.after ? 'ck-drop-after' : 'ck-drop-before'); }
  };
  const up = () => {
    if (!drag) { return; }
    const row = drag.row, target = drag.target, after = drag.after;
    drag = null;
    const before = rows().map(idOf);
    const order = rows().filter((r) => r !== row);
    if (target) { order.splice(order.indexOf(target) + (after ? 1 : 0), 0, row); }
    const ids = order.map(idOf);
    clear();
    if (target && ids.every(Boolean) && ids.join('|') !== before.join('|')) { setTriggerValue('order', ids); }
  };
  document.addEventListener('pointerdown', down);
  document.addEventListener('pointermove', move, { passive: false });
  document.addEventListener('pointerup', up);
  document.addEventListener('pointercancel', up);
  return () => {
    document.removeEventListener('pointerdown', down);
    document.removeEventListener('pointermove', move);
    document.removeEventListener('pointerup', up);
    document.removeEventListener('pointercancel', up);
    clear();
  };
}
"""
edit_sorter = st.components.v2.component("ck_edit_sorter", js=SORT_JS)


def _ed_noop():
    return None


def _ed_apply_order(sid, order):
    """드래그로 받은 id 순서를 초안에 반영 (현재 STEP 의 항목과 정확히 일치할 때만)."""
    step = _draft_step(sid)
    by_id = {i["id"]: i for i in step["items"]}
    order = [str(x) for x in (order or [])]
    if order and len(order) == len(by_id) and set(order) == set(by_id):
        step["items"] = [by_id[x] for x in order]


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

    # 드래그 정렬 컴포넌트 (화면에는 보이지 않음): 행을 그리기 전에 새 순서를 먼저 반영한다
    with st.container(key="edsort"):
        moved = edit_sorter(key="ed_sort_" + sid, on_order_change=_ed_noop)
    _ed_apply_order(sid, moved.get("order"))

    types = list(ITEM_TYPES)
    if step["items"]:
        st.caption("왼쪽 손잡이를 끌어서 순서를 바꿀 수 있어요.")
    for item in step["items"]:
        iid = item["id"]
        kind = ss.get("ed_type_" + iid, item_type(item))
        meta = ITEM_TYPES.get(kind, ITEM_TYPES["learn"])
        with st.container(key="edrow_" + iid):
            c = st.columns([0.4, 0.4, 1.9, 3.9, 0.9, 0.5], vertical_alignment="center", gap="small")
            c[0].html('<div class="ck-grip" data-iid="' + esc(iid, quote=True) + '" title="끌어서 순서 바꾸기">'
                      + ICON_GRIP + "</div>")
            with c[1]:
                with st.container(key="edic_" + meta["tag"] + "_" + iid):
                    st.markdown(":material/" + meta["icon"] + ":")
            item["type"] = c[2].selectbox(
                "유형", types, index=types.index(item_type(item)), key="ed_type_" + iid,
                format_func=lambda t: ITEM_TYPES[t]["label"], label_visibility="collapsed")
            item["name"] = c[3].text_input("이름", value=item["name"], key="ed_name_" + iid,
                                           label_visibility="collapsed")
            c[4].checkbox("지금", value=bool(item.get("current")), key="ed_cur_" + iid,
                          on_change=_ed_current, args=(iid,))
            c[5].button("×", key="ed_del_" + iid, on_click=_ed_del_item, args=(sid, iid), width="stretch",
                        help="이 항목 삭제")
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


# ================================================================ 포트폴리오 만들기
def _pf_rooms():
    """대화가 있는 학습방을 커리큘럼 순서로: [{id, name, kind, label, qa:[(질문, 답변)]}]."""
    ss = st.session_state
    out = []
    for s in ss.curriculum["steps"]:
        for it in s["items"]:
            qa = []
            for m in ss.rooms.get(it["id"], {}).get("messages") or []:
                if m["role"] == "user":
                    q = m.get("ask", m["text"])
                    if not q.startswith("/"):
                        qa.append([q, ""])
                elif m.get("answer") and qa and not qa[-1][1]:
                    qa[-1][1] = m["answer"]
            if qa:
                kind = item_type(it)
                out.append({"id": it["id"], "name": it["name"], "kind": kind, "label": ITEM_TYPES[kind]["label"],
                            "qa": [tuple(x) for x in qa]})
    return out


def _pf_clear_keys():
    for k in list(st.session_state.keys()):
        if isinstance(k, str) and k.startswith("pfe_"):
            del st.session_state[k]


def _pf_load_example():
    _pf_clear_keys()
    st.session_state.pf_draft = pf_example()


def _pf_reset():
    _pf_clear_keys()
    st.session_state.pf_draft = None


def open_portfolio():
    st.session_state.open_portfolio = True


def _pf_field(label, obj, field, key, area=False, height=96, hide_label=False, help=None):
    """초안의 한 칸: 값은 draft(dict)에 바로 되돌려 쓴다. '[숫자 입력 필요]' 가 남아 있으면 노랗게 표시."""
    current = st.session_state.get("pfe_" + key, obj.get(field, ""))
    prefix = "pfok_"
    if PF_NEED in str(current):
        prefix = "pfneed_"
    vis = "visible"
    if hide_label:
        vis = "collapsed"
    with st.container(key=prefix + key):
        if area:
            obj[field] = st.text_area(label, value=obj.get(field, ""), key="pfe_" + key, height=height,
                                      label_visibility=vis, help=help)
        else:
            obj[field] = st.text_input(label, value=obj.get(field, ""), key="pfe_" + key, label_visibility=vis, help=help)
        if PF_NEED in obj[field]:
            st.html('<div class="ck-need">숫자를 직접 입력해 주세요</div>')


def _pf_sec(letter, name):
    st.html('<div class="ck-pf-sec"><i>' + letter + "</i>" + name + "</div>")


def _pf_checklist_html(d):
    rows = ""
    for label, ok, ask in pf_checklist(d):
        cls, mark, extra = "", "O", ""
        if not ok:
            cls, mark = " x", "X"
            extra = "<small>채울 질문: " + esc(ask) + "</small>"
        rows += '<li class="ck-pfc-row' + cls + '"><span>' + mark + "</span><div>" + esc(label) + extra + "</div></li>"
    return '<ul class="ck-pfc">' + rows + "</ul>"


def _pf_setup():
    ss = st.session_state
    rooms = _pf_rooms()
    st.caption("학습방에서 나눈 대화를 바탕으로 10초 요약 1쪽과 프로젝트별 SPARK 1쪽 초안을 만들어요. "
               "숫자는 지어내지 않고, 모르는 값은 " + PF_NEED + " 로 남겨요.")
    sel, info = [], {"metrics": {}}
    if rooms:
        by_id = {r["id"]: r for r in rooms}
        picked = st.multiselect("포트폴리오에 담을 학습방", list(by_id), default=list(by_id), key="pfs_rooms",
                                format_func=lambda i: by_id[i]["name"] + " (" + by_id[i]["label"] + ")")
        sel = [by_id[i] for i in by_id if i in picked]
        c1, c2, c3 = st.columns(3)
        info["name"] = c1.text_input("이름 (선택)", key="pfs_name")
        info["job"] = c2.text_input("희망 직무 (선택)", key="pfs_job", placeholder="예: AI 서비스 기획")
        info["team"] = c3.text_input("팀 규모 (선택)", key="pfs_team", placeholder="예: 4명")
        for r in pf_page_rooms(sel):
            st.html('<div class="ck-label">' + esc(r["name"]) + " 의 성과 수치 (선택)</div>")
            m1, m2, m3, m4 = st.columns(4)
            info["metrics"][r["name"]] = {
                "label": m1.text_input("지표 이름", key="pfs_ml_" + r["id"], placeholder="예: 첫 답변 대기 시간").strip(),
                "before": m2.text_input("시작값", key="pfs_mb_" + r["id"], placeholder="예: 2분").strip(),
                "after": m3.text_input("결과값", key="pfs_ma_" + r["id"], placeholder="예: 3초").strip(),
                "contribution": m4.text_input("기여도 %", key="pfs_mc_" + r["id"], placeholder="예: 40%").strip(),
            }
    else:
        st.html('<div class="ck-box note"><b>아직 학습방 대화가 없어요</b>학습방에서 질문을 나눈 뒤 다시 열어 주세요. '
                "어떤 결과물이 나오는지는 예시로 먼저 볼 수 있어요.</div>")
    status = st.container()
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        st.button("예시 포트폴리오 보기", key="pfs_example", icon=":material/visibility:", on_click=_pf_load_example)
        go = st.button("초안 만들기", key="pfs_go", type="primary", disabled=not sel)
    if go:
        with status:
            if not ready():
                st.html('<div class="ck-box note"><b>' + esc(NO_KEY[0]) + "</b>초안은 API 키가 있어야 만들 수 있어요. "
                        "지금은 '예시 포트폴리오 보기' 로 결과물을 확인해 보세요.</div>")
                return
            try:
                with st.spinner("대화를 읽고 초안을 쓰는 중이에요"):
                    draft = pf_generate(sel, info)
            except Exception as err:
                st.html('<div class="ck-box note"><b>초안을 만들다가 문제가 생겼어요</b>' + esc(str(err)[:200]) + "</div>")
                return
        _pf_clear_keys()
        ss.pf_draft = draft
        st.rerun(scope="fragment")


def _pf_edit(d):
    if d.get("example"):
        st.html('<div class="ck-pf-ex"><span>예시</span>손으로 쓴 예시 포트폴리오예요. 숫자는 설명을 위한 값이니 내 것으로 고쳐 쓰세요.</div>')
    summary = st.container()
    names = ["10초 요약"] + ["프로젝트 " + str(n) + " " + p.get("room", "") for n, p in enumerate(d["projects"], 1)]
    tabs = st.tabs(names)
    with tabs[0]:
        c1, c2 = st.columns(2)
        with c1:
            _pf_field("이름", d, "name", "name")
        with c2:
            _pf_field("희망 직무", d, "job", "job")
        _pf_field("일하는 방식 한 줄", d, "slogan", "slogan", help="[문제]를 [방법]으로 해결하는 [정체성]")
        st.html('<div class="ck-label">대표 수치 (Before → After)</div>')
        for n, m in enumerate(d["metrics"]):
            a, b, c = st.columns([2, 1, 1])
            with a:
                _pf_field("지표 이름", m, "label", "m" + str(n) + "l", hide_label=n > 0)
            with b:
                _pf_field("시작값", m, "before", "m" + str(n) + "b", hide_label=n > 0)
            with c:
                _pf_field("결과값", m, "after", "m" + str(n) + "a", hide_label=n > 0)
        st.html('<div class="ck-label">핵심 강점 3개와 한 줄 근거</div>')
        for n, s in enumerate(d["strengths"]):
            a, b = st.columns([1, 2])
            with a:
                _pf_field("강점", s, "title", "s" + str(n) + "t", hide_label=n > 0)
            with b:
                _pf_field("근거 (어느 학습방, 프로젝트인지)", s, "evidence", "s" + str(n) + "e", hide_label=n > 0)
        hint = "한 줄에 하나씩 '기술: 연결 프로젝트' 로 적어요. 숙련도 % 는 쓰지 않아요."
        a, b = st.columns(2)
        with a:
            _pf_field("기술 스택: 주력", d, "stack_main", "stackm", area=True, help=hint)
        with b:
            _pf_field("기술 스택: 경험", d, "stack_exp", "stacke", area=True, help=hint)
    for n, p in enumerate(d["projects"]):
        k = "p" + str(n)
        with tabs[n + 1]:
            _pf_sec("S", "문제 정의")
            _pf_field("프로젝트 제목", p, "title", k + "title")
            _pf_field("누가 어떤 불편을 겪었나요", p, "who_pain", k + "who", area=True, height=80)
            _pf_field("3줄 요약 (한 줄에 하나씩)", p, "summary", k + "sum", area=True)
            _pf_sec("P", "선택 이유")
            _pf_field("기존 방식의 한계", p, "limits", k + "lim", area=True, height=80)
            st.html('<div class="ck-label">대안 비교 (마지막 칸은 선택 또는 제외)</div>')
            for i, alt in enumerate(p["alts"]):
                c1, c2, c3, c4 = st.columns([3, 4, 4, 2])
                with c1:
                    _pf_field("대안", alt, "option", k + "a" + str(i) + "o", hide_label=i > 0)
                with c2:
                    _pf_field("장점", alt, "pros", k + "a" + str(i) + "p", hide_label=i > 0)
                with c3:
                    _pf_field("한계", alt, "cons", k + "a" + str(i) + "c", hide_label=i > 0)
                with c4:
                    _pf_field("판단", alt, "decision", k + "a" + str(i) + "d", hide_label=i > 0)
            _pf_field("제약 조건 (기간, 인원, 환경)", p, "constraints", k + "con")
            _pf_sec("A", "실행과 성과")
            c1, c2 = st.columns([3, 1])
            with c1:
                _pf_field("내 역할", p, "role", k + "role")
            with c2:
                _pf_field("기여도 %", p, "contribution", k + "contrib")
            c1, c2, c3 = st.columns([2, 1, 1])
            with c1:
                _pf_field("지표 이름", p, "metric_label", k + "ml")
            with c2:
                _pf_field("시작값", p, "before", k + "mb")
            with c3:
                _pf_field("결과값", p, "after", k + "ma")
            _pf_field("방법별 기여 (한 줄에 '방법: 결과에 준 영향')", p, "methods", k + "meth", area=True)
            _pf_sec("R", "회고와 검증")
            _pf_field("막힌 지점과 해결", p, "stuck", k + "stuck", area=True, height=110)
            _pf_field("AI 검증 기록", p, "ai_check", k + "ai", area=True, height=80)
            _pf_field("한계와 다음 단계", p, "limitations", k + "limit", area=True, height=80)
            _pf_sec("K", "직무 키워드")
            _pf_field("희망 직무 키워드 (한 줄에 '키워드: 이 프로젝트에서의 근거')", p, "keywords", k + "kw", area=True)
    checks = pf_checklist(d)
    done = len([1 for _, ok, _ in checks if ok])
    with summary:
        note_need = ""
        if pf_has_need(d):
            note_need = '<span class="need">' + PF_NEED + " 가 남아 있어요</span>"
        st.html('<div class="ck-pf-sum"><b>점검표 ' + str(done) + " / " + str(len(checks)) + "</b>"
                "<span>칸을 고치면 아래 점검표가 바로 바뀌어요</span>" + note_need + "</div>")
    st.html('<div class="ck-label">점검표 (X 인 항목의 질문은 면접에서도 자주 나와요)</div>' + _pf_checklist_html(d))
    stem = "portfolio"
    if d.get("example"):
        stem = "portfolio_example"
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        st.button("처음으로", key="pfx_reset", icon=":material/restart_alt:", on_click=_pf_reset)
        st.download_button("마크다운 저장", data=pf_markdown(d), file_name=stem + ".md", mime="text/markdown",
                           key="pfx_md", on_click="ignore")
        st.download_button("HTML로 저장", data=pf_html(d), file_name=stem + ".html", mime="text/html",
                           type="primary", key="pfx_html", on_click="ignore")
    st.caption("HTML 파일을 브라우저에서 열면 글자를 눌러 바로 고칠 수 있고, Ctrl+P 로 PDF 로 저장할 수 있어요.")


@st.dialog("포트폴리오 만들기", width="large")
def portfolio_dialog():
    d = st.session_state.get("pf_draft")
    if d:
        _pf_edit(d)
    else:
        _pf_setup()


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
                            meta = ITEM_TYPES[item_type(item)]
                            label = item["name"]
                            if item.get("current"):
                                label += " :orange[지금]"
                            current = ss.view == "room" and ss.current_room == item["id"]
                            st.button(label, key="room" + meta["tag"] + "_" + item["id"],
                                      icon=":material/" + meta["icon"] + ":",
                                      type="primary" if current else "secondary", width="stretch",
                                      on_click=open_room, args=(item["id"],))

        with st.container(key="sbdoc"):
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


def curriculum_html():
    """/커리큘럼 카드: STEP 마다 한 줄짜리 타임라인 (지난 항목 진한 선, 지금 강조, 이후 연하게)."""
    cur = st.session_state.curriculum
    flat = [it for step in cur["steps"] for it in step["items"]]
    pos = next((i for i, it in enumerate(flat) if it.get("current")), -1)
    parts = ['<div class="ck-tl">']
    if cur.get("cohort"):
        parts.append('<div class="ck-label">' + esc(cur["cohort"]) + "</div>")
    idx = 0
    for n, step in enumerate(cur["steps"], 1):
        parts.append('<div class="ck-tl-step"><b>STEP ' + str(n) + "</b>" + esc(step["name"]) + "</div>")
        row_cls = "ck-tl-row"
        if idx <= pos < idx + len(step["items"]):
            row_cls += " now"
        parts.append('<div class="' + row_cls + '" style="--n:' + str(max(len(step["items"]), 1)) + '">')
        for it in step["items"]:
            cls = "ck-tl-it t-" + ITEM_TYPES[item_type(it)]["tag"]
            now = ""
            if idx == pos:
                cls += " cur"
                now = '<b class="ck-tl-now">지금</b>'
            elif idx < pos:
                cls += " done"
            else:
                cls += " todo"
            parts.append('<div class="' + cls + '"><i class="ck-tl-nd"></i><span class="ck-tl-nm">'
                         + esc(it["name"]) + "</span>" + now + "</div>")
            idx += 1
        parts.append("</div>")
    legend = "".join('<span class="t-' + m["tag"] + '"><i class="ck-tl-nd"></i>' + esc(m["label"]) + "</span>"
                     for m in ITEM_TYPES.values())
    parts.append('<div class="ck-tl-legend">' + legend + "</div></div>")
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
        elif card == "unlock":
            st.markdown("**「" + md(m["name"]) + "」은 비밀번호가 걸린 PDF예요.** " + md(m.get("msg", "")))
            pending = st.session_state.get("locked_pdf")
            if is_last and pending and pending["name"] == m["name"]:
                pw = st.text_input("PDF 비밀번호", type="password", key="pdfpw_" + key)
                with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
                    if st.button("열기", type="primary", key="pdfopen_" + key, disabled=not pw):
                        ingest(pending["name"], pending["data"], current_messages(), pw)
                        st.rerun()
        elif card == "docs":
            site = doc_site(m.get("site"))
            if site:
                st.markdown("**" + md(site[0]) + " 공식 문서**")
                st.caption(site[1])
                with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
                    st.link_button("열기", site[1], type="primary", icon=":material/open_in_new:")
            else:
                st.markdown("**공식 문서** 바로 가기예요. 누르면 새 탭에서 열려요.")
                with st.container(horizontal=True, gap="small"):
                    for name, _, url, _ in DOC_SITES:
                        st.link_button(name, url, icon=":material/open_in_new:")
        elif card == "recommend":
            st.markdown("지금 이런 걸 물어보면 좋아요.")
            for n, q in enumerate(m.get("qs", [])):
                st.button(q, key="cmd_" + key + "_r" + str(n), icon=":material/lightbulb:", width="stretch",
                          on_click=send, args=(q,))
        elif m.get("note"):
            st.html('<div class="ck-box note"><b>' + esc(m.get("note_title", "안내")) + "</b>" + esc(m["note"]) + "</div>")
        else:
            if m.get("ref"):
                st.html('<div class="ck-ref">' + esc(m["ref"]) + "</div>")
            st.markdown(md(_tidy_answer(m.get("answer", ""))))
            rows = []
            study = m.get("is_study", True)  # 공부/학습 질문일 때만 선배 한마디, 오늘 해 볼 것을 보여 준다
            if study and m.get("quote"):
                rows.append('<div class="ck-row"><span class="ck-ic q">' + ICON_QUOTE + '</span><div><b>선배 한마디</b><p>'
                            + esc(m["quote"]) + "</p></div></div>")
            if study and m.get("challenge"):
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
        '<div class="ck-hero-art">' + mascot_img(170) + "</div></div>"
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
    kind = item_type(item)
    if kind == "project":
        return [name + " 는 어떻게 진행되나요?", "팀 역할은 어떻게 나누면 좋을까요?", "발표 준비는 어떻게 하면 좋을까요?"]
    if kind == "activity":
        return [name + " 는 어떻게 진행되나요?", name + " 전에 무엇을 준비하면 좋을까요?",
                name + " 에서 무엇을 얻어 갈 수 있나요?"]
    return [name + " 는 무엇부터 공부하면 좋을까요?", name + " 에서 자주 막히는 부분은 어디인가요?",
            name + " 복습은 어떻게 하면 좋을까요?"]


ROOM_DESC = {
    "learn": "이 과목을 배우는 동안 궁금한 것을 백서, 교안, 웹에서 함께 찾아봐요.",
    "project": "팀 프로젝트를 하면서 막히는 것을 백서, 교안, 웹에서 함께 찾아봐요.",
    "activity": "이 활동을 준비하면서 궁금한 것을 백서, 교안, 웹에서 함께 찾아봐요.",
}


def lecture_box(rid, r):
    """학습방 교안 박스: 연결된 교안 표시 + PDF 올리기/바꾸기 (입력창 첨부와 같은 attach 경로)."""
    up = st.session_state.get("lec_up_" + rid)
    if up is not None:
        token = getattr(up, "file_id", None) or up.name
        if token != r.get("doc_tried"):
            r["doc_tried"] = token  # 같은 파일을 rerun 마다 다시 처리하지 않는다
            attach(up)
    with st.container(key="roomdoc"):
        if r["doc_name"]:
            st.html(
                '<div class="ck-lec"><span class="ck-lec-ic on">' + ICON_FILE + '</span>'
                '<div class="ck-lec-txt"><b>교안</b><span class="ck-lec-name">' + esc(r["doc_name"]) + "</span></div>"
                '<span class="ck-chip"><i></i>연결됨</span></div>'
            )
            hint = "다른 PDF 를 올리면 이 방의 교안이 바뀌어요."
        else:
            st.html(
                '<div class="ck-lec"><span class="ck-lec-ic">' + ICON_FILE_OFF + '</span>'
                '<div class="ck-lec-txt"><b>교안</b><span>아직 교안이 없어요</span></div></div>'
            )
            hint = "교안 PDF 를 아래에 올리거나 입력창에 첨부하면 이 방의 교안으로 연결돼요."
        st.caption(hint)
        st.file_uploader("교안 PDF 올리기", type=["pdf"], key="lec_up_" + rid, label_visibility="collapsed")


def render_room():
    ss = st.session_state
    found = find_item(ss.current_room)
    if not found:
        go_home()
        st.rerun()
    step, step_no, item = found
    rid = item["id"]
    r = room(rid)
    kind = item_type(item)
    meta = ITEM_TYPES[kind]
    now = ""
    if item.get("current"):
        now = '<span class="ck-now">지금</span>'
    with st.container(key="card_roomhead"):
        with st.container(key="roomkind_" + meta["tag"]):
            st.markdown(":material/" + meta["icon"] + ": **" + meta["label"] + "** STEP " + str(step_no) + " "
                        + md(step["name"]))
        st.html(
            '<div class="ck-room-title"><span class="ck-title">' + esc(item["name"]) + "</span>" + now + "</div>"
            '<div class="ck-desc">' + ROOM_DESC[kind] + "</div>"
        )
        with st.container(horizontal=True, vertical_alignment="center", gap="small", key="roomsrc"):
            st.markdown("답변 자료", width="content")
            st.pills("답변 자료", SOURCE_OPTIONS, selection_mode="multi", default=SOURCE_OPTIONS, key="src_" + rid,
                     label_visibility="collapsed")
            st.button("포트폴리오 만들기", key="pf_open", icon=":material/work:", on_click=open_portfolio)
    lecture_box(rid, r)
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
    ss = st.session_state
    want_portfolio = ss.pop("open_portfolio", False)
    if ss.pop("open_fortune", False):
        fortune_dialog()
    elif want_portfolio:
        portfolio_dialog()



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

# 데모 전용: ?demo=1&dlg=fortune|edit|portfolio 로 다이얼로그를 바로 연다 (발표/화면 점검용)
dlg = st.query_params.get("dlg")
if st.query_params.get("demo") == "1" and dlg and not st.session_state.get("_dlg_done"):
    st.session_state._dlg_done = True
    if dlg == "edit":
        open_curriculum_dialog()
    elif dlg == "portfolio":
        st.session_state.open_portfolio = True
    else:
        st.session_state.open_fortune = True
finish()
