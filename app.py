
import os
import base64
import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 생성
client = OpenAI()

# 페이지 설정
st.set_page_config(page_title="텍스트 → 음성 변환기", page_icon="🔊")
st.title("🔊 텍스트 → 음성 변환기")
st.write("입력한 텍스트를 자연스러운 음성으로 읽어줍니다.")

# 텍스트 입력
text = st.text_area(
    "읽을 텍스트를 입력하세요",
    "안녕하세요. OpenAI 텍스트 음성 변환 실습입니다.",
    height=150
)

# 버튼
if st.button("음성 생성하기"):
    if text.strip() == "":
        st.warning("읽을 텍스트를 입력하세요.")
    else:
        with st.spinner("음성을 생성 중입니다..."):

            # TTS 생성
            speech = client.audio.speech.create(
                model="gpt-4o-mini-tts",
                voice="alloy",
                input=text
            )
            audio_bytes = speech.content

        # 음성 출력
        st.markdown("### 🔊 음성 재생")
        st.audio(audio_bytes, format="audio/mp3")
