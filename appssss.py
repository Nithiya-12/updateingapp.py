import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter your message")

if st.button("Check"):
    if msg == "":
        st.warning("Please enter a message")
    else:
        spam_words = ["win", "offer", "free", "money", "prize"]

        found = False
        for word in spam_words:
            if word.lower() in msg.lower():
                found = True
                break

        if found:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
