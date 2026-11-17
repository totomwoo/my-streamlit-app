
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


# 답변 카드 / 편집 행에서 쓰는 아이콘 (색은 ui_css 의 :root 토큰 값과 같게 유지)
ICON_QUOTE = line_icon(
    '<path d="M3 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/>'
    '<path d="M15 21c3 0 7-1 7-8V5c0-1.25-.76-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h2c0 4-2 6-3 6"/>',
    "#B45309")  # --cookie-deep
ICON_FLAG = line_icon(
    '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><path d="M4 22v-7"/>',
    "#5B4BE0")  # --primary
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
  --primary-pale:#DCD6FF; --ring:#D5D2E8; --need-line:#E0A23A; --need-bg:#FFF7E6; --need-border:#F1D9AE;
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
/* st-key-fu_*: 이어서 물어보기 버튼 (왼쪽 정렬) / st-key-cmd_*: 명령어 버튼 */
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
/* 포트폴리오 만들기 (1단계 학습방 고르기, 2단계 미리보기) */
/* ck-pf-steps: 단계 표시 (1 학습방 고르기 / 2 미리보기) */
.ck-pf-steps{display:flex;gap:6px;font-size:12px;font-weight:700;margin-bottom:6px;}
.ck-pf-steps span{color:var(--text-sub);background:var(--bg);border-radius:999px;padding:3px 10px;}
.ck-pf-steps span.on{color:var(--surface);background:var(--primary);}
.st-key-pf_top .ck-pf-steps{margin-bottom:0;}
/* st-key-pfr_*: 넣을 학습방 토글 칩 (on: 고름, off: 안 고름, x: 대화 없음) */
[class*="st-key-pfr_"] button{min-height:40px;padding:0 14px;border-radius:999px;font-weight:600;}
[class*="st-key-pfr_on_"] button{border:1.5px solid var(--primary);background:var(--primary-soft);color:var(--primary-hover);}
[class*="st-key-pfr_on_"] button p{font-weight:700;}
[class*="st-key-pfr_x_"] button{min-height:30px;padding:0 11px;border:1px dashed var(--border);background:var(--surface);
  color:var(--muted);}
[class*="st-key-pfr_x_"] button p{font-size:12.5px;}
/* st-key-pf_needbox: 비어 있는 숫자 입력 상자 (호박색 바탕) */
.st-key-pf_needbox{background:var(--need-bg);border-radius:12px;padding:10px 12px;gap:8px;}
/* st-key-pfn_* 의 stTextInput (DOM 확인: label + 입력 div): 라벨은 왼쪽, 작은 입력칸은 오른쪽 한 줄 */
[class*="st-key-pfn_"] [data-testid="stTextInput"]{display:flex;flex-direction:row;align-items:center;gap:8px;}
[class*="st-key-pfn_"] [data-testid="stTextInput"] > label{flex:1;min-width:0;margin:0;}
[class*="st-key-pfn_"] [data-testid="stTextInput"] > label p{font-size:13.5px;font-weight:600;color:var(--text);}
[class*="st-key-pfn_"] [data-testid="stTextInput"] > div{flex:0 0 104px;width:104px;border-color:var(--need-border);}
[class*="st-key-pfn_"] [data-testid="stTextInput"] > div, [class*="st-key-pfn_"] input{background:var(--surface);}
/* ck-pf-cap: 저장 버튼 아래 한 줄 안내 */
.ck-pf-cap{font-size:12px;color:var(--text-sub);text-align:center;}

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
    st.html("<style>" + CSS.replace("__MASCOT__", MASCOT_URI) + PF_SLIDE_CSS + "</style>")



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
    "없으면 AIVLE-EDU 공지사항을 확인하도록 안내하세요. 개념 설명은 [{web_label}]을 활용하세요.\n"
    "말투는 따뜻한 해요체, 결론 먼저, 번호 목록으로 짧게, 바로 해 볼 행동을 권하세요.\n"
    + ANSWER_RULES
    + "\n[이전 대화]\n{history}\n\n[백서]\n{wp}\n\n[{web_label}]\n{web}"
)


def room_answer(question, topic, sources, wp_retriever=None, history=""):
    """학습방 답변: 켜진 자료(백서/웹 검색)를 종합한다."""
    srcs, wp_docs = [], []
    search_q = rewrite_query(question, history)  # 앞 대화를 받아 묻는 질문도 검색되게
    query = topic + " " + search_q
    if "백서" in sources and wp_retriever is not None:
        wp_docs = wp_retriever.invoke(query)[:3]
        srcs += [doc_source(d, "백서") for d in wp_docs]

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
            "web": web_text,
            "input": question,
        }
    )
    msg = to_message({"answer": ans, "docs": []})
    msg["sources"] = srcs
    return msg



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
        ("적용했더니 재시작해도 첫 답변이 바로 나와요. 그런데 두 명이 동시에 PDF를 올리면 서로의 업로드가 지워져요.",
         "모두가 같은 컬렉션 이름을 쓰고 있어서 그래요. **세션마다 컬렉션을 나누면** 해결돼요.\n\n"
         "1. 세션 ID를 만들어 컬렉션 이름 뒤에 붙여요. 예: `upload_ab12cd34`\n"
         "2. 공용 백서 컬렉션은 읽기 전용으로 두고, 업로드 문서만 세션 컬렉션에 넣어요.\n"
         "3. 두 브라우저에서 동시에 올려 보고 서로의 문서가 남아 있는지 확인해요."),
        ("비밀번호가 걸린 PDF는 로더에서 오류가 나요. 어떻게 처리하면 좋을까요?",
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
         "기본값인 **k=4 에서 시작**해 검색 결과를 보며 조정해요.\n\n"
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
                          "1. 기본 설정은 `chunk_size=500`, `chunk_overlap=100` 이에요.\n"
                          "2. 답이 문단 중간에서 잘리면 overlap 을 늘려요.\n"
                          "3. 엉뚱한 문단이 섞이면 chunk 를 줄이고 k 값을 조정해요.",
                "is_study": True,
                "quote": "",
                "challenge": "같은 질문을 chunk_size 300 / 500 / 800 으로 돌려 보고 검색된 문단을 비교해 보세요.",
                "followups": ["k 값은 몇으로 두면 좋나요?", "Chroma 컬렉션은 왜 나누나요?", "발표 때 무엇을 보여 주면 좋나요?"],
                "sources": [
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
# 포트폴리오 만들기: 학습방 대화 → 16:9 슬라이드 5장 (초안 스키마, 프롬프트, 숫자 가드, 예시, 슬라이드 HTML).
import copy
import datetime
import html
import json
import re
from typing import List

from pydantic import BaseModel, Field


PF_NEED = "[숫자 입력 필요]"
PF_FOOTER = "AIVLE School 학습 도우미 쿠키 선배로 만든 초안"
PF_SLIDE_NAMES = ["표지", "한눈에", "만든 구조", "선택 이유", "성과와 회고"]
PF_ED = "\x00"  # 내보내기 HTML 에서만 contenteditable 속성으로 바뀌는 자리 표시


# ---------------------------------------------------------------- 구조화 출력 스키마 (슬라이드 칸과 1:1)
class PortfolioMetric(BaseModel):
    """대표 수치 하나 (표지 KPI 카드, 5번 슬라이드 막대)"""

    label: str = Field(description="지표 이름. 12자 이내의 명사구. 예: 첫 답변 대기")
    before: str = Field(description="시작값. 숫자와 단위. 예: 2분. 대화에 없으면 '" + PF_NEED + "'")
    after: str = Field(description="결과값. 숫자와 단위. 예: 3초. 대화에 없으면 '" + PF_NEED + "'")
    unit: str = Field(description="막대 그래프에 쓸 단위. 예: 초, %, 건")


class PortfolioStep(BaseModel):
    """만든 구조의 단계 하나"""

    name: str = Field(description="단계 이름. 8자 이내. 예: 임베딩, 저장")
    detail: str = Field(description="한 줄 설명. 12자 이내. 예: 상위 4개 문단")
    mine: bool = Field(description="내가 맡은 단계면 true")


class PortfolioHighlight(BaseModel):
    """만든 구조에서 내세울 점 하나"""

    title: str = Field(description="제목. 10자 이내. 예: 저장소 재사용")
    line: str = Field(description="한 줄. 28자 이내. 예: 서버를 켤 때마다 다시 벡터화하지 않음")


class PortfolioOption(BaseModel):
    """비교한 대안 하나"""

    name: str = Field(description="대안 이름. 14자 이내. 예: 일반 LLM 챗봇")
    scores: List[int] = Field(description="기준 4개에 대한 점수. 기준과 같은 순서로 정확히 4개. 2=충족, 1=보통, 0=미흡")
    chosen: bool = Field(description="실제로 고른 대안이면 true. 셋 중 하나만 true")


class PortfolioStuck(BaseModel):
    """막힌 점과 해결 한 쌍"""

    issue: str = Field(description="막힌 점. 12자 이내. 예: 동시 업로드 충돌")
    fix: str = Field(description="해결. 12자 이내. 예: 사용자별 저장")


class PortfolioDraft(BaseModel):
    """포트폴리오 슬라이드 5장 초안"""

    name: str = Field(description="이름. 사용자가 알려 준 경우만, 아니면 빈 문자열")
    slogan_lines: List[str] = Field(description="1번 표지 슬로건. '[문제]를 [방법]으로 해결하는 [정체성]' 을 2~3줄로 나눈 것. 한 줄 12자 이내")
    keywords: List[str] = Field(description="1번 표지 직무 키워드. 정확히 3개. 각 10자 이내")
    metrics: List[PortfolioMetric] = Field(description="대표 수치. 정확히 2개. 대표 프로젝트의 전후 비교")
    contribution: str = Field(description="내 기여도 %. 예: 40%. 대화에 없으면 '" + PF_NEED + "'")
    project_title: str = Field(description="2번 프로젝트 제목. 24자 이내")
    period: str = Field(description="프로젝트 기간. 예: 2일. 대화에 없으면 '" + PF_NEED + "'")
    team: str = Field(description="팀 인원. 예: 4명. 대화에 없으면 '" + PF_NEED + "'")
    role: str = Field(description="내 역할. 10자 이내. 예: RAG 파이프라인")
    tools: str = Field(description="쓴 도구 1~3개를 쉼표로. 20자 이내. 예: LangChain, Streamlit")
    problem_lines: List[str] = Field(description="문제. 누가 어떤 불편을 겪었는지 2~3줄. 한 줄 11자 이내")
    solution_lines: List[str] = Field(description="해결. 무엇을 어떻게 만들었는지 2~3줄. 한 줄 11자 이내")
    pipeline_title: str = Field(description="3번 슬라이드 제목. 16자 이내. 예: 어떻게 만들었나")
    steps: List[PortfolioStep] = Field(description="만든 구조의 단계. 처리 순서대로 4~6개")
    highlights: List[PortfolioHighlight] = Field(description="구조에서 내세울 점. 정확히 3개")
    choice_title: str = Field(description="4번 슬라이드 제목. 16자 이내. 예: 왜 RAG를 골랐나")
    criteria: List[str] = Field(description="대안을 비교한 기준. 정확히 4개. 각 8자 이내. 예: 근거 확인")
    options: List[PortfolioOption] = Field(description="비교한 대안. 정확히 3개. 고른 대안을 마지막에")
    constraints: str = Field(description="제약 조건 한 줄. 쉼표로 나열. 40자 이내. 대화에 없는 숫자는 쓰지 않음")
    result_title: str = Field(description="5번 슬라이드 제목. 16자 이내. 예: 무엇이 달라졌나")
    stuck: List[PortfolioStuck] = Field(description="막힌 점과 해결. 정확히 3쌍")
    ai_check: str = Field(description="AI 결과를 어떻게 검증했는지 한 줄. 44자 이내. 대화에 없으면 빈 문자열")


PF_SYSTEM = (
    "당신은 KT AIVLE School 교육생의 취업 포트폴리오를 발표용 슬라이드 5장으로 정리해 주는 선배 '쿠키 선배'입니다.\n"
    "아래 학습방 대화만 근거로 씁니다.\n\n"
    "[슬라이드]\n"
    "1. 표지(10초 요약): 슬로건 '[문제]를 [방법]으로 해결하는 [정체성]', 직무 키워드 3개, 대표 수치 2개(시작값 → 결과값), 내 기여도.\n"
    "2. 프로젝트 한눈에: 제목, 기간, 팀, 내 역할, 도구, 문제 → 해결 → 결과.\n"
    "3. 만든 구조: 처리 단계 4~6개(내가 맡은 단계 표시), 내세울 점 3개.\n"
    "4. 선택 이유: 대안 3개를 기준 4개로 비교(2=충족, 1=보통, 0=미흡), 고른 대안, 제약 조건.\n"
    "5. 성과와 회고: 대표 수치의 전후 비교, 막힌 점과 해결 3쌍, AI 검증 한 줄.\n\n"
    "[대표 프로젝트]\n"
    "- 슬라이드 2~5는 '대표 프로젝트' 학습방 하나만 다룹니다. 다른 학습방은 키워드와 슬로건의 근거로만 씁니다.\n\n"
    "[숫자 규칙: 가장 중요]\n"
    "- 숫자는 대화에 실제로 나온 값만 씁니다.\n"
    "- 그 밖의 수치, 시작값, 결과값, 기여도, 기간, 인원은 절대 지어내지 말고 정확히 '" + PF_NEED + "' 라고 씁니다.\n\n"
    "[글 규칙]\n"
    "- 슬라이드에 들어갈 글이라 아주 짧게 씁니다. 문장이 아니라 짧은 구로 쓰고, 각 항목의 글자 수 제한을 꼭 지킵니다.\n"
    "- 과장하는 형용사 대신 한 일과 결과를 씁니다.\n"
    "- 대화에 없는 경험을 만들어 내지 않습니다. 근거가 없으면 빈 문자열로 둡니다.\n"
    "- 가운뎃점 문자는 쓰지 않고 쉼표를 씁니다."
)
PF_REVISE = (
    "\n\n[고치기]\n"
    "- 현재 초안(JSON)과 수정 요청을 받습니다. 같은 구조로 초안 전체를 다시 냅니다.\n"
    "- 요청과 관계없는 항목은 글자 하나 바꾸지 않고 그대로 둡니다.\n"
    "- 새 숫자는 수정 요청이나 대화에 있는 값만 씁니다. '" + PF_NEED + "' 는 요청에 값이 없으면 그대로 둡니다."
)
PF_MODEL_KEYS = list(PortfolioDraft.model_fields)


def pf_primary(convos):
    """대표 프로젝트 학습방: 고른 미니프로젝트 방 중 대화가 가장 많은 곳 (없으면 대화가 가장 많은 방)."""
    if not convos:
        return None
    projects = [c for c in convos if c["kind"] == "project"]
    return max(projects or convos, key=lambda c: len(c["qa"]))


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


def pf_build_prompt(convos, job):
    """새 초안용 (system, human) 프롬프트 문자열."""
    main = pf_primary(convos)
    lines = ["[희망 직무] " + (job or "(미입력)"),
             "[대표 프로젝트 학습방] " + (main["name"] if main else "(없음)"),
             "", "[학습방 대화]", pf_convo_text(convos)]
    return PF_SYSTEM, "\n".join(lines)


def pf_revise_prompt(d, instruction, convos):
    """말로 고치기용 (system, human) 프롬프트 문자열: 현재 초안 + 수정 요청 + 대화."""
    current = {k: d.get(k) for k in PF_MODEL_KEYS}
    lines = ["[희망 직무] " + (d.get("job") or "(미입력)"),
             "[대표 프로젝트 학습방] " + (d.get("room") or "(없음)"),
             "", "[현재 초안]", json.dumps(current, ensure_ascii=False),
             "", "[수정 요청]", instruction.strip()[:400],
             "", "[학습방 대화]", pf_convo_text(convos) or "(없음)"]
    return PF_SYSTEM + PF_REVISE, "\n".join(lines)


def _pf_guard(value, corpus):
    """대화/입력에 없는 숫자가 섞여 있으면 통째로 '[숫자 입력 필요]' 로 바꾼다 (모델이 지어낸 숫자 차단)."""
    value = (value or "").strip()
    if not value or PF_NEED in value:
        return PF_NEED
    nums = re.findall(r"\d+(?:[.,]\d+)?", value)
    if not nums or any(n not in corpus for n in nums):
        return PF_NEED
    return value


def _pf_known(text, corpus):
    """설명 글에 근거 없는 숫자가 있으면 그 글을 비운다 (없어도 되는 칸에만 쓴다)."""
    text = (text or "").strip()
    if any(n not in corpus for n in re.findall(r"\d+(?:[.,]\d+)?", text)):
        return ""
    return text


def _pf_suffix(value, suffix):
    """숫자만 있는 값에 단위를 붙인다 ('40' → '40%')."""
    value = str(value or "").strip()
    if suffix and re.fullmatch(r"\d+(?:[.,]\d+)?", value):
        return value + suffix
    return value


def _pf_strs(items, n):
    return [str(x or "").strip() for x in list(items or [])[:n] if str(x or "").strip()]


def pf_from_model(result, corpus, base):
    """구조화 출력(PortfolioDraft) → 슬라이드용 dict. 근거 없는 숫자는 '[숫자 입력 필요]' 로 바꾼다.

    corpus: 숫자의 근거가 되는 글 (프롬프트 전체), base: example/job/year/room/rooms 를 담은 dict.
    """
    d = {k: base.get(k) for k in ("example", "job", "year", "room", "rooms")}
    d["name"] = (result.name or "").strip()
    d["slogan_lines"] = _pf_strs(result.slogan_lines, 3)
    d["keywords"] = _pf_strs(result.keywords, 3)
    d["metrics"] = []
    for m in list(result.metrics)[:2]:
        unit = (m.unit or "").strip()
        d["metrics"].append({"label": m.label.strip(), "unit": unit,
                             "before": _pf_suffix(_pf_guard(m.before, corpus), unit),
                             "after": _pf_suffix(_pf_guard(m.after, corpus), unit)})
    d["contribution"] = _pf_suffix(_pf_guard(result.contribution, corpus), "%")
    d["project_title"] = result.project_title.strip()
    d["period"] = _pf_guard(result.period, corpus)
    d["team"] = _pf_suffix(_pf_guard(result.team, corpus), "명")
    d["role"] = result.role.strip()
    d["tools"] = result.tools.strip()
    d["problem_lines"] = _pf_strs(result.problem_lines, 3)
    d["solution_lines"] = _pf_strs(result.solution_lines, 3)
    d["pipeline_title"] = result.pipeline_title.strip() or "어떻게 만들었나"
    d["steps"] = [{"name": s.name.strip(), "detail": _pf_known(s.detail, corpus), "mine": bool(s.mine)}
                  for s in list(result.steps)[:6] if s.name.strip()]
    d["highlights"] = [{"title": h.title.strip(), "line": h.line.strip()} for h in list(result.highlights)[:3]]
    d["choice_title"] = result.choice_title.strip() or "왜 이 방법을 골랐나"
    d["criteria"] = (_pf_strs(result.criteria, 4) + ["", "", "", ""])[:4]
    d["options"] = []
    for o in list(result.options)[:3]:
        scores = [min(2, max(0, int(x))) for x in list(o.scores)[:4]]
        d["options"].append({"name": o.name.strip(), "scores": (scores + [0, 0, 0, 0])[:4], "chosen": bool(o.chosen)})
    picked = [o for o in d["options"] if o["chosen"]]
    if d["options"] and len(picked) != 1:
        best = max(picked or d["options"], key=lambda o: sum(o["scores"]))
        for o in d["options"]:
            o["chosen"] = o is best
    d["constraints"] = result.constraints.strip()
    d["result_title"] = result.result_title.strip() or "무엇이 달라졌나"
    d["stuck"] = [{"issue": s.issue.strip(), "fix": s.fix.strip()} for s in list(result.stuck)[:3]]
    d["ai_check"] = result.ai_check.strip()
    return d


def pf_generate(convos, job):
    """LLM 한 번 호출로 초안을 만든다 (구조화 출력)."""
    system, human = pf_build_prompt(convos, job)
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0).with_structured_output(PortfolioDraft)
    result = llm.invoke([("system", system), ("human", human)])
    main = pf_primary(convos)
    base = {"example": False, "job": (job or "").strip(), "year": str(datetime.date.today().year),
            "room": main["name"] if main else "", "rooms": [c["id"] for c in convos]}
    return pf_from_model(result, human, base)


def pf_revise(d, instruction, convos):
    """말로 고치기: 현재 초안 + 수정 요청으로 LLM 을 한 번 불러 같은 구조의 초안을 받는다."""
    system, human = pf_revise_prompt(d, instruction, convos)
    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0).with_structured_output(PortfolioDraft)
    result = llm.invoke([("system", system), ("human", human)])
    return pf_from_model(result, human, d)


# ---------------------------------------------------------------- 비어 있는 숫자 (입력칸 목록과 채우기)
def pf_need_slots(d):
    """'[숫자 입력 필요]' 로 남은 칸: [(키, 라벨, 입력 예시)]."""
    out = []
    for n, m in enumerate(d.get("metrics", [])[:2]):
        label = m.get("label") or ("지표 " + str(n + 1))
        if PF_NEED in str(m.get("before")):
            out.append(("m" + str(n) + "b", label + " (전)", "예: 2분"))
        if PF_NEED in str(m.get("after")):
            out.append(("m" + str(n) + "a", label + " (결과)", "예: 95%"))
    for key, label, hint in (("contribution", "내 기여도", "예: 40%"), ("period", "프로젝트 기간", "예: 2일"),
                             ("team", "팀 인원", "예: 4명")):
        if PF_NEED in str(d.get(key)):
            out.append((key, label, hint))
    return out


def pf_fill(d, key, value):
    """비어 있는 숫자 칸 하나를 사용자가 넣은 값으로 채운다."""
    value = " ".join(str(value or "").split())[:12]
    if not value:
        return
    if key in ("contribution", "period", "team"):
        d[key] = _pf_suffix(value, {"contribution": "%", "team": "명"}.get(key, ""))
    else:
        m = d["metrics"][int(key[1])]
        m["before" if key[2] == "b" else "after"] = _pf_suffix(value, m.get("unit", ""))


# ---------------------------------------------------------------- 예시 (API 호출 없이 보여 주는 보기)
PF_EXAMPLE = {
    "example": True, "year": "2026", "name": "김에이블", "job": "DX 컨설턴트", "room": "미니프로젝트 4차", "rooms": [],
    "slogan_lines": ["흩어진 학습 정보를", "근거가 보이는 서비스로", "바꾸는 기획자"],
    "keywords": ["RAG 서비스 기획", "AI 결과 검증", "Streamlit 배포"],
    "metrics": [
        {"label": "첫 답변 대기", "before": "2분", "after": "3초", "unit": "초"},
        {"label": "근거 페이지가 붙은 답변", "before": "0%", "after": "100%", "unit": "%"},
    ],
    "contribution": "40%",
    "project_title": "근거가 보이는 AIVLE School 학습 도우미",
    "period": "2일", "team": "4명", "role": "RAG 파이프라인", "tools": "LangChain, Streamlit",
    "problem_lines": ["수십 쪽 백서를", "직접 뒤져야 했고", "맞는지 확인이 어려움"],
    "solution_lines": ["백서 기반 RAG로", "답마다", "근거 페이지 표시"],
    "pipeline_title": "어떻게 만들었나",
    "steps": [
        {"name": "백서 PDF", "detail": "업로드", "mine": False},
        {"name": "분할", "detail": "500자, 겹침 100", "mine": True},
        {"name": "임베딩, 저장", "detail": "Chroma", "mine": True},
        {"name": "검색", "detail": "상위 4개 문단", "mine": True},
        {"name": "답변", "detail": "근거 페이지 표시", "mine": False},
    ],
    "highlights": [
        {"title": "저장소 재사용", "line": "서버를 켤 때마다 다시 벡터화하지 않음"},
        {"title": "사용자별 저장", "line": "여러 명이 동시에 올려도 서로 지우지 않음"},
        {"title": "잠긴 PDF 해제", "line": "비밀번호가 걸린 PDF도 바로 읽음"},
    ],
    "choice_title": "왜 RAG를 골랐나",
    "criteria": ["근거 확인", "지어내지 않음", "질문 이해", "개발 부담 낮음"],
    "options": [
        {"name": "PDF 직접 검색", "scores": [2, 2, 0, 2], "chosen": False},
        {"name": "일반 LLM 챗봇", "scores": [0, 0, 2, 2], "chosen": False},
        {"name": "RAG (백서 검색 + 근거)", "scores": [2, 2, 2, 1], "chosen": True},
    ],
    "constraints": "2일, 4명, 무료 배포, 올린 문서는 외부 공유 불가",
    "result_title": "무엇이 달라졌나",
    "stuck": [
        {"issue": "첫 답변 2분", "fix": "저장소 재사용"},
        {"issue": "잠긴 PDF", "fix": "읽기 전 잠금 해제"},
        {"issue": "동시 업로드 충돌", "fix": "사용자별 저장"},
    ],
    "ai_check": "질문 20개로 근거 페이지를 백서 원문과 대조, 어긋난 3건은 설정을 고쳐 재확인",
}


def pf_example():
    return copy.deepcopy(PF_EXAMPLE)


# ---------------------------------------------------------------- 슬라이드 HTML (미리보기와 내보내기가 같은 마크업)
# 크기는 시안의 1000 x 562.5 기준 px 로 적고, 아래에서 cqw(틀 너비의 1/100)로 바꾼다. 대문자 PX 는 바꾸지 않는 실선 두께.
_PF_SLIDE_CSS_PX = """
/* pfs-frame: 슬라이드 틀. 안쪽 크기가 모두 틀 너비에 비례한다 */
.pfs-frame{container-type:inline-size;width:100%;}
/* pfs: 16:9 슬라이드 한 장 (공통) */
.pfs{position:relative;box-sizing:border-box;width:1000px;height:562.5px;overflow:hidden;background:var(--surface);
  border:1PX solid var(--border);border-radius:12px;padding:44px 52px;display:flex;flex-direction:column;gap:24px;
  font-family:var(--font);font-size:15px;line-height:1.5;color:var(--text);text-align:left;}
.pfs *{box-sizing:border-box;margin:0;}
.pfs-badge{position:absolute;top:22px;right:26px;font-size:12px;font-weight:700;color:var(--cookie-deep);
  background:var(--cookie-soft);border-radius:999px;padding:3px 10px;}
.pfs-h{font-size:30px;line-height:1.3;font-weight:800;letter-spacing:-.02em;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;}
/* pfs-need: 비어 있는 숫자 자리 (점선 호박색 칩) */
.pfs-need{flex:none;display:inline-flex;align-items:center;align-self:center;height:34px;padding:0 14px;
  border:1.5PX dashed var(--need-line);border-radius:10px;background:var(--need-bg);color:var(--cookie-deep);
  font-size:15px;line-height:1;font-weight:700;letter-spacing:0;white-space:nowrap;}
.pfs-need.sm{height:24px;padding:0 9px;border-radius:7px;font-size:12px;}
/* pfs-line: 아래쪽 한 줄 상자 (제약 조건, AI 검증) */
.pfs-line{display:flex;align-items:center;gap:14px;background:var(--bg);border-radius:14px;padding:16px 20px;
  white-space:nowrap;overflow:hidden;}
.pfs-line.end{margin-top:auto;}
.pfs-line.sm{padding:14px 20px;}
.pfs-line b{flex:none;font-size:14px;color:var(--text-sub);}
.pfs-line span{min-width:0;font-size:16px;font-weight:600;overflow:hidden;text-overflow:ellipsis;}
.pfs-line.sm span{font-size:15px;}
/* s1: 표지 (왼쪽 슬로건, 오른쪽 KPI 카드 3개) */
.pfs.s1{padding:52px 56px;flex-direction:row;gap:44px;}
.pfs-l{flex:1.25;min-width:0;display:flex;flex-direction:column;justify-content:space-between;}
.pfs-l-top{display:flex;flex-direction:column;gap:14px;}
.pfs-eye{font-size:13px;font-weight:800;letter-spacing:.14em;color:var(--primary);}
.pfs-who{font-size:18px;font-weight:700;white-space:nowrap;overflow:hidden;}
.pfs-who span{font-weight:500;color:var(--text-sub);}
.pfs-slogan{font-size:40px;line-height:1.28;font-weight:800;letter-spacing:-.025em;white-space:nowrap;overflow:hidden;}
.pfs-slogan.m{font-size:34px;}
.pfs-slogan.s{font-size:29px;}
.pfs-chips{display:flex;flex-wrap:wrap;gap:8px;}
.pfs-chips span{font-size:13px;font-weight:700;color:var(--primary-hover);background:var(--primary-soft);
  border-radius:999px;padding:5px 12px;white-space:nowrap;}
.pfs-r{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:14px;}
.pfs-kpi{background:var(--bg);border-radius:16px;padding:18px 22px;white-space:nowrap;overflow:hidden;}
.pfs-kpi b{display:block;font-size:14px;font-weight:700;color:var(--text-sub);overflow:hidden;text-overflow:ellipsis;}
.pfs-kpi div{margin-top:4px;display:flex;align-items:baseline;gap:8px;font-size:18px;color:var(--text-sub);}
.pfs-kpi strong{font-size:44px;line-height:1.25;font-weight:800;color:var(--primary);letter-spacing:-.02em;}
/* s2: 프로젝트 한눈에 (정보 상자 4개, 문제 → 해결 → 결과) */
.pfs.s2{gap:26px;}
.pfs-head{display:flex;flex-direction:column;gap:6px;}
.pfs-head > span{font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--primary);white-space:nowrap;overflow:hidden;}
.pfs-meta{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;}
.pfs-meta div{border:1PX solid var(--border);border-radius:12px;padding:12px 16px;overflow:hidden;}
.pfs-meta small{display:block;font-size:12px;font-weight:700;color:var(--text-sub);}
.pfs-meta b{display:block;margin-top:2px;font-size:18px;line-height:1.35;font-weight:800;}
.pfs-flow{flex:1;min-height:0;display:flex;align-items:stretch;gap:14px;}
.pfs-box{flex:1;min-width:0;background:var(--bg);border-radius:16px;padding:22px;display:flex;flex-direction:column;
  gap:10px;overflow:hidden;}
.pfs-flow > i{align-self:center;font-style:normal;font-size:26px;color:var(--muted);}
.pfs-box small{font-size:13px;font-weight:800;color:var(--text-sub);}
.pfs-box b{font-size:20px;line-height:1.45;font-weight:700;}
.pfs-box.res{background:var(--primary);color:var(--surface);}
.pfs-box.res small{color:var(--primary-pale);}
.pfs-box.res strong{font-size:44px;line-height:1.1;font-weight:800;white-space:nowrap;}
.pfs-box.res > span{font-size:15px;font-weight:600;color:var(--primary-soft);}
.pfs-box.res .pfs-need{align-self:flex-start;color:var(--cookie-deep);font-weight:700;}
/* s3: 만든 구조 (단계 상자와 화살표, 내 담당 묶음, 내세울 점 3개) */
.pfs.s3{gap:30px;}
.pfs-pipe{display:flex;align-items:flex-end;gap:8px;}
.pfs-pipe i{flex:none;height:92px;display:flex;align-items:center;font-style:normal;font-size:18px;color:var(--muted);}
.pfs-step{height:92px;min-width:0;border:1PX solid var(--border);border-radius:12px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:2px;padding:0 6px;text-align:center;overflow:hidden;}
.pfs-step b{font-size:15px;line-height:1.3;}
.pfs-step span{font-size:12px;line-height:1.3;color:var(--text-sub);}
.pfs-step.me{border:2px solid var(--primary);background:var(--primary-soft);}
.pfs-step.me span{color:var(--primary-hover);}
.pfs-mine{flex:none;display:flex;flex-direction:column;gap:8px;}
.pfs-mine > u{text-decoration:none;text-align:center;font-size:12px;font-weight:800;color:var(--primary);
  border-bottom:2px solid var(--primary);padding-bottom:4px;}
.pfs-mine > div{display:flex;align-items:center;gap:8px;}
.pfs-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;}
.pfs-cards div{background:var(--bg);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;gap:6px;
  overflow:hidden;}
.pfs-cards b{font-size:16px;}
.pfs-cards span{font-size:14px;color:var(--text-sub);}
/* s4: 선택 이유 (대안 3 x 기준 4 비교표, 범례, 제약 조건) */
.pfs.s4{gap:22px;}
.pfs-tbl{display:grid;grid-template-columns:1.7fr repeat(4,minmax(0,1fr)) .7fr;font-size:15px;}
.pfs-tbl > span{min-width:0;min-height:54px;padding:0 10px;border-top:1PX solid var(--border);display:flex;
  align-items:center;justify-content:center;white-space:nowrap;overflow:hidden;}
.pfs-tbl > span.th{min-height:40px;border-top:0;font-size:13px;font-weight:700;color:var(--text-sub);}
.pfs-tbl > span.n{justify-content:flex-start;padding-left:14px;font-weight:700;}
.pfs-tbl > span.v{color:var(--text-sub);}
.pfs-tbl > span.on{background:var(--primary-soft);}
.pfs-tbl > span.on.n, .pfs-tbl > span.on.v{font-weight:800;color:var(--primary-hover);}
.pfs-dot{flex:none;display:inline-block;width:16px;height:16px;border-radius:999px;}
.pfs-dot.d2{background:var(--primary);}
.pfs-dot.d1{border:3px solid var(--primary);}
.pfs-dot.d0{border:2px solid var(--ring);}
.pfs-legend{display:flex;gap:18px;font-size:13px;color:var(--text-sub);}
.pfs-legend span{display:flex;align-items:center;gap:6px;}
.pfs-legend .pfs-dot{width:12px;height:12px;}
/* s5: 성과와 회고 (전후 막대, 기여도 도넛, 막힌 점과 해결 표, AI 검증) */
.pfs-g5{flex:1;min-height:0;display:grid;grid-template-columns:1.15fr .7fr 1.15fr;gap:26px;}
.pfs-bars{min-width:0;display:flex;flex-direction:column;gap:20px;}
.pfs-bar{display:flex;flex-direction:column;gap:8px;}
.pfs-cap{font-size:14px;font-weight:700;color:var(--text-sub);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.pfs-bar > div{display:flex;align-items:center;gap:10px;height:24px;}
.pfs-bar small{flex:none;width:44px;font-size:13px;color:var(--text-sub);}
.pfs-bar i{height:22px;border-radius:6px;background:var(--ring);}
.pfs-bar em{font-style:normal;font-size:14px;font-weight:700;white-space:nowrap;}
.pfs-bar .af i{background:var(--primary);}
.pfs-bar .af em{font-weight:800;color:var(--primary);}
.pfs-donut{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;}
.pfs-donut svg{width:150px;height:150px;}
.pfs-donut circle{fill:none;stroke-width:18;}
.pfs-donut circle.bg{stroke:var(--primary-soft);}
.pfs-donut circle.fg{stroke:var(--primary);stroke-linecap:round;}
.pfs-donut text{font-family:var(--font);font-size:26px;font-weight:800;fill:var(--text);}
.pfs-stuck{min-width:0;display:flex;flex-direction:column;gap:10px;}
.pfs-stuck > div{display:grid;grid-template-columns:1fr 1fr;border:1PX solid var(--border);border-radius:12px;
  overflow:hidden;font-size:13.5px;}
.pfs-stuck > div > span{min-width:0;padding:10px 12px;border-top:1PX solid var(--border);}
.pfs-stuck > div > span.th{border-top:0;background:var(--bg);font-weight:700;color:var(--text-sub);}
.pfs-stuck > div > span.fx{font-weight:600;}
"""
PF_SLIDE_CSS = re.sub(r"(\d*\.?\d+)px", lambda m: format(float(m.group(1)) / 10, "g") + "cqw", _PF_SLIDE_CSS_PX)
PF_NEED_CHIP = '<span class="pfs-need">숫자 넣기</span>'
PF_NEED_CHIP_SM = '<span class="pfs-need sm">숫자 넣기</span>'
_PF_TIME = {"초": 1, "분": 60, "시간": 3600}


def _pf_width(text):
    """글의 대략적인 너비 (한글 1, 영문/숫자 0.6, 공백 0.3)."""
    total = 0.0
    for ch in text:
        if ch == " ":
            total += 0.3
        elif ord(ch) > 0x2E7F:
            total += 1.0
        else:
            total += 0.6
    return total


def _pf_cut(text, limit):
    """슬라이드 밖으로 넘치지 않게 너비 기준으로 자른다 (가운뎃점은 쉼표로)."""
    text = " ".join(str(text or "").replace(PF_ED, "").replace(chr(183), ",").split())
    total = 0.0
    for n, ch in enumerate(text):
        total += _pf_width(ch)
        if total > limit:
            return text[:n].rstrip(" ,") + "…"
    return text


def _pf_t(text, limit):
    return html.escape(_pf_cut(text, limit))


def _pf_missing(value):
    return PF_NEED in str(value or "") or not str(value or "").strip()


def _pf_val(value, limit, small=False):
    """숫자 칸: 비어 있으면 '숫자 넣기' 칩, 아니면 글자."""
    if _pf_missing(value):
        return PF_NEED_CHIP_SM if small else PF_NEED_CHIP
    return "<span" + PF_ED + ">" + _pf_t(value, limit) + "</span>"


def _pf_badge(d):
    if d.get("example"):
        return '<span class="pfs-badge">예시</span>'
    return ""


def _pf_lines(lines, limit):
    return "<br>".join(_pf_t(x, limit) for x in list(lines or [])[:3])


def _pf_parse(value):
    """'2분' → (2.0, '분'). 숫자로 시작하지 않으면 None."""
    m = re.match(r"^\s*(\d[\d,]*(?:\.\d+)?)\s*(.*)$", str(value or ""))
    if not m or PF_NEED in str(value):
        return None
    return float(m.group(1).replace(",", "")), m.group(2).strip()


def _pf_slide1(d):
    name = _pf_t(d.get("name"), 10)
    job = _pf_t(d.get("job"), 16)
    if job:
        job += " 지원"
    lines = [_pf_cut(x, 16) for x in list(d.get("slogan_lines") or [])[:3]]
    widest = max([_pf_width(x) for x in lines] or [0])
    size = ""
    if widest > 13.5:
        size = " s"
    elif widest > 11.5:
        size = " m"
    chips = "".join("<span" + PF_ED + ">" + _pf_t(k, 10) + "</span>" for k in list(d.get("keywords") or [])[:3])
    cards = ""
    for m in list(d.get("metrics") or [])[:2]:
        cards += ('<div class="pfs-kpi"><b' + PF_ED + ">" + _pf_t(m.get("label"), 16) + "</b><div>"
                  + _pf_val(m.get("before"), 5, small=True) + "<span>→</span><strong>" + _pf_val(m.get("after"), 5)
                  + "</strong></div></div>")
    team = re.fullmatch(r"(\d+)\s*명", str(d.get("team") or "").strip())
    mine = "내 기여도"
    if team:
        mine += " (" + team.group(1) + "인 팀)"
    cards += ('<div class="pfs-kpi"><b>' + mine + "</b><div><strong>" + _pf_val(d.get("contribution"), 4)
              + "</strong></div></div>")
    return ('<div class="pfs s1">' + _pf_badge(d) + '<div class="pfs-l"><div class="pfs-l-top">'
            '<span class="pfs-eye">PORTFOLIO ' + html.escape(str(d.get("year") or "")) + "</span>"
            '<div class="pfs-who"><b' + PF_ED + ">" + name + "</b> <span" + PF_ED + ">" + job + "</span></div>"
            '<div class="pfs-slogan' + size + '"' + PF_ED + ">" + "<br>".join(html.escape(x) for x in lines) + "</div></div>"
            '<div class="pfs-chips">' + chips + '</div></div><div class="pfs-r">' + cards + "</div></div>")


def _pf_slide2(d):
    meta = ""
    for label, key, limit in (("기간", "period", 8), ("팀", "team", 8), ("내 역할", "role", 12), ("도구", "tools", 22)):
        if key in ("period", "team"):
            value = _pf_val(d.get(key), limit, small=True)
        else:
            value = "<span" + PF_ED + ">" + _pf_t(d.get(key), limit) + "</span>"
        meta += "<div><small>" + label + "</small><b>" + value + "</b></div>"
    result = ""
    metrics = list(d.get("metrics") or [])
    if metrics:
        m = metrics[0]
        caption = _pf_cut(m.get("label"), 16)
        if not _pf_missing(m.get("before")):
            caption += " (기존 " + _pf_cut(m.get("before"), 5) + ")"
        result = "<strong>" + _pf_val(m.get("after"), 5) + "</strong><span" + PF_ED + ">" + html.escape(caption) + "</span>"
    return ('<div class="pfs s2">' + _pf_badge(d) + '<div class="pfs-head"><span>PROJECT 01&nbsp;&nbsp;'
            + _pf_t(d.get("room"), 24) + '</span><div class="pfs-h"' + PF_ED + ">" + _pf_t(d.get("project_title"), 27)
            + '</div></div><div class="pfs-meta">' + meta + '</div><div class="pfs-flow">'
            '<div class="pfs-box"><small>문제</small><b' + PF_ED + ">" + _pf_lines(d.get("problem_lines"), 18) + "</b></div><i>→</i>"
            '<div class="pfs-box"><small>해결</small><b' + PF_ED + ">" + _pf_lines(d.get("solution_lines"), 18) + "</b></div><i>→</i>"
            '<div class="pfs-box res"><small>결과</small>' + result + "</div></div></div>")


def _pf_slide3(d):
    steps = list(d.get("steps") or [])[:6]
    count = max(1, len(steps))
    width = format((896 - 34 * (count - 1)) / count / 10 - 0.2, ".2f") + "cqw"
    name_limit, detail_limit = 8, 12
    if count >= 6:
        name_limit, detail_limit = 7, 9

    def box(s):
        cls = "pfs-step"
        if s.get("mine"):
            cls += " me"
        return ('<div class="' + cls + '" style="flex:0 0 ' + width + '"><b' + PF_ED + ">" + _pf_t(s.get("name"), name_limit)
                + "</b><span" + PF_ED + ">" + _pf_t(s.get("detail"), detail_limit) + "</span></div>")

    parts, n = [], 0
    while n < len(steps):
        if steps[n].get("mine"):
            run = []
            while n < len(steps) and steps[n].get("mine"):
                run.append(box(steps[n]))
                n += 1
            parts.append('<div class="pfs-mine"><u>내 담당</u><div>' + "<i>→</i>".join(run) + "</div></div>")
        else:
            parts.append(box(steps[n]))
            n += 1
    cards = ""
    for h in list(d.get("highlights") or [])[:3]:
        cards += ("<div><b" + PF_ED + ">" + _pf_t(h.get("title"), 14) + "</b><span" + PF_ED + ">" + _pf_t(h.get("line"), 34)
                  + "</span></div>")
    return ('<div class="pfs s3">' + _pf_badge(d) + '<div class="pfs-h"' + PF_ED + ">" + _pf_t(d.get("pipeline_title"), 27)
            + '</div><div class="pfs-pipe">' + "<i>→</i>".join(parts) + '</div><div class="pfs-cards">' + cards
            + "</div></div>")


def _pf_slide4(d):
    criteria = (list(d.get("criteria") or []) + ["", "", "", ""])[:4]
    cells = '<span class="th n">방법</span>'
    for c in criteria:
        cells += '<span class="th"' + PF_ED + ">" + _pf_t(c, 8) + "</span>"
    cells += '<span class="th">판단</span>'
    for o in list(d.get("options") or [])[:3]:
        on, verdict = "", "제외"
        if o.get("chosen"):
            on, verdict = " on", "선택"
        cells += '<span class="n' + on + '"' + PF_ED + ">" + _pf_t(o.get("name"), 15) + "</span>"
        for s in (list(o.get("scores") or []) + [0, 0, 0, 0])[:4]:
            cells += '<span class="' + on.strip() + '"><span class="pfs-dot d' + str(min(2, max(0, int(s)))) + '"></span></span>'
        cells += '<span class="v' + on + '">' + verdict + "</span>"
    legend = ('<div class="pfs-legend"><span><span class="pfs-dot d2"></span>충족</span>'
              '<span><span class="pfs-dot d1"></span>보통</span><span><span class="pfs-dot d0"></span>미흡</span></div>')
    return ('<div class="pfs s4">' + _pf_badge(d) + '<div class="pfs-h"' + PF_ED + ">" + _pf_t(d.get("choice_title"), 27)
            + '</div><div class="pfs-tbl">' + cells + "</div>" + legend
            + '<div class="pfs-line end"><b>제약 조건</b><span' + PF_ED + ">" + _pf_t(d.get("constraints"), 44)
            + "</span></div></div>")


def _pf_num(value):
    """막대 옆 숫자: 천 단위 쉼표, 소수는 한 자리까지 ('120', '1,200', '2.5')."""
    text = format(value, ",.1f")
    if text.endswith(".0"):
        return text[:-2]
    return text


def _pf_bar(m):
    """지표 하나의 전/후 막대 두 줄. 값이 비어 있으면 막대 대신 '숫자 넣기' 칩."""
    raw = [m.get("before"), m.get("after")]
    parsed = [_pf_parse(v) for v in raw]
    unit = ""
    for p in parsed:
        if p and p[1]:
            unit = p[1]
    known = [p for p in parsed if p]
    if len(known) == 2 and known[0][1] != known[1][1] and all(p[1] in _PF_TIME for p in known):
        parsed = [(p[0] * _PF_TIME[p[1]], "초") for p in parsed]  # 분과 초가 섞이면 초로 맞춘다
        unit = "초"
    unit = unit or str(m.get("unit") or "")
    top = max([p[0] for p in parsed if p] + [0]) or 1
    rows = ""
    for tag, cls, value, p in (("전", "bf", raw[0], parsed[0]), ("후", "af", raw[1], parsed[1])):
        if _pf_missing(value):
            body = PF_NEED_CHIP_SM
        elif not p:
            body = "<em>" + _pf_t(value, 12) + "</em>"
        else:
            size = format(max(4, 210 * p[0] / top) / 10, ".2f") + "cqw"
            body = '<i style="flex:0 0 ' + size + '"></i><em>' + _pf_num(p[0]) + "</em>"
        rows += '<div class="' + cls + '"><small>' + tag + "</small>" + body + "</div>"
    caption = _pf_cut(m.get("label"), 16)
    if unit:
        caption += " (" + _pf_cut(unit, 4) + ")"
    return '<div class="pfs-bar"><span class="pfs-cap">' + html.escape(caption) + "</span>" + rows + "</div>"


def _pf_donut(value):
    """내 기여도 도넛 (SVG). 값이 비어 있으면 빈 고리와 '숫자 넣기' 칩."""
    p = _pf_parse(value)
    ring = '<circle class="bg" cx="70" cy="70" r="54"></circle>'
    if not p:
        return ('<div class="pfs-donut"><svg viewBox="0 0 140 140" role="img" aria-label="내 기여도 미입력">' + ring
                + "</svg>" + PF_NEED_CHIP_SM + '<span class="pfs-cap">내 기여도</span></div>')
    pct = min(100.0, max(0.0, p[0]))
    arc = 339.3 * pct / 100
    label = format(pct, "g") + "%"
    return ('<div class="pfs-donut"><svg viewBox="0 0 140 140" role="img" aria-label="내 기여도 ' + label + '">' + ring
            + '<circle class="fg" cx="70" cy="70" r="54" stroke-dasharray="' + format(arc, ".1f") + " "
            + format(339.3, ".1f") + '" transform="rotate(-90 70 70)"></circle>'
            '<text x="70" y="78" text-anchor="middle">' + label + '</text></svg><span class="pfs-cap">내 기여도</span></div>')


def _pf_slide5(d):
    bars = "".join(_pf_bar(m) for m in list(d.get("metrics") or [])[:2])
    rows = '<span class="th">막힌 점</span><span class="th">해결</span>'
    for s in list(d.get("stuck") or [])[:3]:
        rows += ("<span" + PF_ED + ">" + _pf_t(s.get("issue"), 16) + '</span><span class="fx"' + PF_ED + ">"
                 + _pf_t(s.get("fix"), 16) + "</span>")
    return ('<div class="pfs s5">' + _pf_badge(d) + '<div class="pfs-h"' + PF_ED + ">" + _pf_t(d.get("result_title"), 27)
            + '</div><div class="pfs-g5"><div class="pfs-bars">' + bars + "</div>" + _pf_donut(d.get("contribution"))
            + '<div class="pfs-stuck"><span class="pfs-cap">막힌 점과 해결</span><div>' + rows + "</div></div></div>"
            '<div class="pfs-line sm"><b>AI 검증</b><span' + PF_ED + ">" + _pf_t(d.get("ai_check"), 46) + "</span></div></div>")


PF_SLIDE_FUNCS = [_pf_slide1, _pf_slide2, _pf_slide3, _pf_slide4, _pf_slide5]


def pf_slide_html(d, index, editable=False):
    """슬라이드 한 장의 HTML (pfs-frame 안에 넣어 쓴다). editable 이면 글자를 눌러 고칠 수 있게 한다."""
    body = PF_SLIDE_FUNCS[index](d)
    if editable:
        return body.replace(PF_ED, ' contenteditable="true" spellcheck="false"')
    return body.replace(PF_ED, "")


# ---------------------------------------------------------------- 내보내기 (자체 완결 HTML, 16:9, 한 장에 한 쪽)
PF_HTML_CSS = """
/* 앱과 같은 디자인 토큰 */
:root{
  --primary:#5B4BE0; --primary-hover:#4B3CD0; --primary-soft:#EEEBFF; --primary-pale:#DCD6FF;
  --text:#1E1B3A; --text-sub:#5E6278; --muted:#94A3B8;
  --surface:#FFFFFF; --bg:#F6F5FF; --border:#E6E4F2; --ring:#D5D2E8;
  --cookie-deep:#B45309; --cookie-soft:#FFF1DE; --need-line:#E0A23A; --need-bg:#FFF7E6;
  --font:'Noto Sans KR',sans-serif;
}
/* 화면: 슬라이드를 세로로 쌓아 보여 준다 */
body{margin:0;background:var(--bg);font-family:var(--font);color:var(--text);
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}
.tip{max-width:1280px;margin:20px auto 0;padding:0 16px;font-size:14px;line-height:1.6;color:var(--text-sub);}
.deck{display:flex;flex-direction:column;align-items:center;gap:24px;padding:20px 16px 12px;}
.deck .pfs-frame{flex:none;width:min(1280px,100%);}
.foot{padding:4px 16px 28px;font-size:13px;color:var(--text-sub);text-align:center;}
[contenteditable]:focus{outline:2px solid var(--primary-soft);outline-offset:2px;border-radius:4px;}
/* 인쇄: 가로 16:9 한 장에 슬라이드 하나 */
@page{size:13.333in 7.5in;margin:0;}
@media print{
  body{background:var(--surface);}
  .tip,.foot{display:none;}
  .deck{display:block;padding:0;}
  .deck .pfs-frame{width:13.333in;height:7.5in;overflow:hidden;break-after:page;page-break-after:always;}
  .deck .pfs-frame:last-child{break-after:auto;page-break-after:auto;}
  .pfs{border:0;border-radius:0;}
}
"""


def pf_html(d):
    """슬라이드 5장을 담은 HTML 문서 (브라우저에서 열어 PDF 로 인쇄)."""
    title = "포트폴리오"
    foot = PF_FOOTER
    if d.get("example"):
        title = "포트폴리오 예시"
        foot = "예시: 숫자와 내용은 보기로 넣은 값입니다. " + PF_FOOTER
    if d.get("name"):
        title += " " + _pf_cut(d["name"], 10)
    slides = "".join('<div class="pfs-frame">' + pf_slide_html(d, n, editable=True) + "</div>"
                     for n in range(len(PF_SLIDE_FUNCS)))
    return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>' + html.escape(title) + "</title>\n"
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
            "<style>" + PF_HTML_CSS + PF_SLIDE_CSS + "</style>\n</head>\n<body>\n"
            '<p class="tip">글자를 누르면 오타를 바로 고칠 수 있어요 (고친 내용은 파일에 저장되지 않아요). '
            "Ctrl+P 로 인쇄하면 가로 16:9 PDF 5쪽으로 저장돼요.</p>\n"
            '<div class="deck">' + slides + "</div>\n"
            '<p class="foot">' + html.escape(foot) + "</p>\n</body>\n</html>\n")



# ======================================================================
# 화면 구성
# ======================================================================
# 화면 구성: 사이드바, 홈, 대화, 학습방, 다이얼로그, 슬래시 명령어.
import copy
import datetime
import hashlib
import html
import json
import tempfile

import streamlit as st


esc = html.escape
PLACEHOLDER = "질문을 입력하세요 (/ 로 명령어 보기)"
SOURCE_OPTIONS = ["백서", "웹 검색"]
COMMANDS = [
    ("/커리큘럼", "우리 기수 커리큘럼 한눈에 보기", "account_tree"),
    ("/쿠키", "포춘쿠키 하나 열기", "cookie"),
    ("/계획", "백서 학습 전략으로 개인 학습 계획 짜기", "event_note"),
    ("/포트폴리오", "학습방 대화로 포트폴리오 슬라이드 만들기", "work"),
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
        if ss.view == "room":
            rid = ss.current_room
            _, _, item = find_item(rid)
            sources = ss.get("src_" + rid) or []
            wp_ret = None
            if "백서" in sources:
                wp_ret = whitepaper()[1]
            with st.spinner("쿠키 선배가 자료를 찾아보는 중이에요."):
                msgs.append(room_answer(question, item["name"], sources, wp_ret, hist))
        else:
            chain, _ = whitepaper()
            with st.spinner("쿠키 선배가 백서를 찾아보는 중이에요."):
                result = chain.invoke({"input": question, "history": hist})
            msgs.append(to_message(result, "백서"))
        if last.get("ref") and msgs[-1].get("answer"):
            msgs[-1]["ref"] = last["ref"]


def attach(file):
    """첨부 PDF (일반 대화): 백서 대신 이 문서를 근거로 답한다."""
    ss = st.session_state
    msgs = current_messages(create_title=file.name)
    if not ready():
        msgs.append(not_ready_note())
        return
    if file.name == ss.doc_name:
        return  # 같은 문서는 다시 벡터화하지 않는다
    ingest(file.name, file.getvalue(), msgs)


def ingest(name, data, msgs, password=None):
    """PDF 바이트 → 임시 파일(잠겨 있으면 풀기) → rag_pipeline(경로). 잠긴 PDF는 비밀번호 입력 카드를 띄운다."""
    ss = st.session_state
    try:
        with st.spinner("문서를 읽고 벡터화하는 중이에요. 페이지가 많으면 몇 분 걸릴 수 있어요."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(data)
            path = unlock_pdf(tmp.name, password)
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
    elif cmd == "/커리큘럼":
        msgs.append({"role": "user", "text": cmd})
        msgs.append({"role": "assistant", "card": "curriculum"})
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
    '/쿠키': sv('<path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01"/><path d="M16 15.5v.01"/><path d="M12 12v.01"/><path d="M11 17v.01"/><path d="M7 14v.01"/>'),
    '/계획': sv('<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>'),
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
    if key == "input_room":
        # 학습방에서는 PDF 첨부를 받지 않는다 (문서 교체는 일반 대화에서만)
        handle_input(st.chat_input(placeholder=PLACEHOLDER, key=key))
    else:
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
    """학습방을 커리큘럼 순서로: [{id, name, kind, label, qa:[(질문, 답변)]}]. 대화가 없는 방은 qa 가 비어 있다."""
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
            kind = item_type(it)
            out.append({"id": it["id"], "name": it["name"], "kind": kind, "label": ITEM_TYPES[kind]["label"],
                        "qa": [tuple(x) for x in qa]})
    return out


def open_portfolio():
    st.session_state.open_portfolio = True


def _pf_switch(draft):
    """단계 전환: 초안을 바꾸고 앱 전체를 다시 그려 알맞은 크기의 다이얼로그로 다시 연다."""
    ss = st.session_state
    ss.pf_draft = draft
    ss.open_portfolio = True
    st.rerun()


def _pf_toggle(rid):
    picked = st.session_state.pf_sel
    picked[rid] = not picked.get(rid, True)


def _pf_job_default():
    """희망 직무 기본값: 커리큘럼의 '10기 DX 컨설턴트 트랙' 에서 기수와 '트랙' 을 뗀 것."""
    words = [w for w in str(st.session_state.curriculum.get("cohort") or "").split()
             if w != "트랙" and not (w.endswith("기") and w[:-1].isdigit())]
    return " ".join(words)


def _pf_steps_html(now):
    out = '<div class="ck-pf-steps">'
    for n, name in enumerate(["학습방 고르기", "미리보기"], 1):
        cls = ""
        if n == now:
            cls = ' class="on"'
        out += "<span" + cls + ">" + str(n) + " " + name + "</span>"
    return out + "</div>"


def _pf_no_key_note():
    st.html('<div class="ck-box note"><b>' + esc(NO_KEY[0]) + "</b>슬라이드 글은 API 키가 있어야 쓸 수 있어요. "
            "지금은 예시로 결과물을 확인해 보세요.</div>")


def _pf_pick():
    """1단계: 넣을 학습방과 희망 직무만 고른다."""
    ss = st.session_state
    rooms = _pf_rooms()
    picked = ss.setdefault("pf_sel", {})
    if "pf_job" not in ss:
        ss.pf_job = _pf_job_default()
    st.html(_pf_steps_html(1) + '<div class="ck-desc">학습방 대화로 발표용 슬라이드를 만들어요.</div>')
    st.html('<div class="ck-label">넣을 학습방</div>')
    with st.container(horizontal=True, gap="small", key="pf_roomchips"):
        for r in [x for x in rooms if x["qa"]]:  # 대화가 있는 방만 보여 준다
            if picked.get(r["id"], True):
                st.button(md(r["name"]) + " :gray[" + str(len(r["qa"])) + "]", key="pfr_on_" + r["id"],
                          icon=":material/check:", on_click=_pf_toggle, args=(r["id"],))
            else:
                st.button(md(r["name"]) + " :gray[" + str(len(r["qa"])) + "]", key="pfr_off_" + r["id"],
                          on_click=_pf_toggle, args=(r["id"],))
    st.caption("대화가 있는 학습방만 보여요. 숫자는 질문 수예요.")
    ss.pf_job = st.text_input("희망 직무 (선택)", value=ss.pf_job, key="pfs_job", placeholder="예: AI 서비스 기획").strip()
    sel = [r for r in rooms if r["qa"] and picked.get(r["id"], True)]
    status = st.container()
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        example = st.button("예시 보기", key="pfs_example")
        go = st.button("만들기", key="pfs_go", type="primary", disabled=not sel)
    if example:
        _pf_switch(pf_example())
    if go:
        with status:
            if not ready():
                _pf_no_key_note()
                return
            try:
                with st.spinner("대화를 읽고 슬라이드를 쓰는 중이에요"):
                    draft = pf_generate(sel, ss.pf_job)
            except Exception as err:
                st.html('<div class="ck-box note"><b>슬라이드를 만들다가 문제가 생겼어요</b>' + esc(str(err)[:200]) + "</div>")
                return
        _pf_switch(draft)


def _pf_view(d):
    """2단계: 슬라이드 미리보기 + 비어 있는 숫자 + 말로 고치기 + 저장."""
    ss = st.session_state
    # 비어 있는 숫자 칸에 넣은 값은 미리보기를 그리기 전에 초안에 반영한다
    for slot, _, _ in pf_need_slots(d):
        typed = ss.pop("pfn_" + slot, "")
        if typed and typed.strip():
            pf_fill(d, slot, typed)
    with st.container(horizontal=True, vertical_alignment="center", gap="small", key="pf_top"):
        st.html(_pf_steps_html(2), width="content")
        if st.button("처음으로", key="pfx_reset", type="tertiary", icon=":material/restart_alt:"):
            _pf_switch(None)
    left, right = st.columns([2.3, 1], gap="medium")
    with left:
        now = ss.get("pf_slide")
        if now not in range(len(PF_SLIDE_NAMES)):
            now = 0
        st.html('<div class="pfs-frame">' + pf_slide_html(d, now) + "</div>")
        st.segmented_control("슬라이드", list(range(len(PF_SLIDE_NAMES))), default=0, required=True, key="pf_slide",
                             format_func=lambda n: str(n + 1) + " " + PF_SLIDE_NAMES[n],
                             label_visibility="collapsed", width="stretch")
    with right:
        slots = pf_need_slots(d)
        if slots:
            with st.container(key="pf_needbox"):
                st.html('<div class="ck-label">비어 있는 숫자 ' + str(len(slots)) + "개</div>")
                for slot, label, hint in slots:
                    st.text_input(label, key="pfn_" + slot, placeholder=hint)
            st.caption("대화에 없는 숫자는 지어내지 않고 여기만 비워 둬요.")
        with st.container(horizontal=True, vertical_alignment="bottom", gap="small", key="pf_fixrow"):
            ask = st.text_input("말로 고치기", key="pf_fix", placeholder="예: 슬로건을 더 짧게 바꿔줘")
            fix = st.button("고치기", key="pf_fix_go")
        if fix and ask.strip():
            if not ready():
                _pf_no_key_note()
            else:
                try:
                    with st.spinner("고치는 중이에요"):
                        convos = [r for r in _pf_rooms() if r["qa"] and r["id"] in (d.get("rooms") or [])]
                        ss.pf_draft = pf_revise(d, ask, convos)
                    st.rerun(scope="fragment")
                except Exception as err:
                    st.html('<div class="ck-box note"><b>고치다가 문제가 생겼어요</b>' + esc(str(err)[:200]) + "</div>")
        stem = "portfolio_slides"
        if d.get("example"):
            stem = "portfolio_slides_example"
        st.download_button("슬라이드 저장", data=pf_html(d), file_name=stem + ".html", mime="text/html",
                           key="pfx_html", type="primary", on_click="ignore", width="stretch")
        st.html('<div class="ck-pf-cap">가로 16:9, 브라우저에서 PDF로 인쇄</div>')


@st.dialog("포트폴리오 만들기", width="small")
def _pf_pick_dialog():
    _pf_pick()


@st.dialog("포트폴리오 만들기", width="large")
def _pf_view_dialog():
    _pf_view(st.session_state.pf_draft)


def portfolio_dialog():
    """초안이 없으면 1단계(작은 창), 있으면 2단계(큰 창)를 연다."""
    if st.session_state.get("pf_draft"):
        _pf_view_dialog()
    else:
        _pf_pick_dialog()


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
    return {"백서": "k-wp", "웹": "k-web"}.get(kind, "")


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
    "learn": "이 과목을 배우는 동안 궁금한 것을 백서와 웹에서 함께 찾아봐요.",
    "project": "팀 프로젝트를 하면서 막히는 것을 백서와 웹에서 함께 찾아봐요.",
    "activity": "이 활동을 준비하면서 궁금한 것을 백서와 웹에서 함께 찾아봐요.",
}


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
