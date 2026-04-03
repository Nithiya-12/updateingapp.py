import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter your message")

if st.button("Check"):
    if msg.strip() == "":
        st.warning("⚠️ Enter message")
    else:
        msg = msg.lower()
        spam_words = ["offer", "win", "free", "money", "click"]

        if any(word in msg for word in spam_words):
            st.error("🚨 Spam Message")

            try:
                with open("spam.mp3", "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
            except:
                st.warning("🔇 spam.mp3 missing")

        else:
            st.success("✅ Not Spam")

            try:
                with open("notspam.mp3", "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
            except:
                st.warning("🔇 notspam.mp3 missing")
