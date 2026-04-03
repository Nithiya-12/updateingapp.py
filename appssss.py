import streamlit as st
from gtts import gTTS
import os

st.title("🔊 Spam Detection App")

msg = st.text_input("Enter message")

if st.button("Check"):
    if "offer" in msg or "win" in msg:
        result = "Spam Message"
        st.error("🚨 Spam Message")
    else:
        result = "Not Spam"
        st.success("✅ Not Spam")

    # Convert text to speech
    tts = gTTS(result)
    tts.save("output.mp3")

    # Play audio
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
