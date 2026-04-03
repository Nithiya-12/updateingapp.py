import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter message")

if st.button("Check"):
    if "offer" in msg or "win" in msg:
        st.error("🚨 Spam Message")

        # 🔊 Sound alert
        st.audio("https://www.soundjay.com/buttons/sounds/beep-07.mp3")
        
    else:
        st.success("✅ Not Spam")

        # optional sound
        st.audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
