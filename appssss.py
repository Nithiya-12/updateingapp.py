import streamlit as st
import tensorflow as tf
import pickle
import re
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ----------------------------
# Load model & tokenizer
# ----------------------------
model = tf.keras.models.load_model("spam_model.h5")
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
max_len = 50

# ----------------------------
# Text cleaning
# ----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

# ----------------------------
# Prediction function
# ----------------------------
def predict_spam(text):
    text = clean_text(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')

    score = model.predict(padded)[0][0]
    return score

# ----------------------------
# UI
# ----------------------------
st.set_page_config(page_title="Spam Detector", layout="centered")

st.title("📩 AI Spam Detection System")
st.markdown("### 🔍 Detect Spam using NLP + Deep Learning")

msg = st.text_area("✉ Enter Email Message")

# Store history
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Check Message"):
    if msg.strip() == "":
        st.warning("⚠ Please enter a message")
    else:
        score = predict_spam(msg)

        if score > 0.5:
            result = "🚨 Spam"
            st.error(result)
        else:
            result = "✅ Not Spam"
            st.success(result)

        # Show probability
        st.progress(float(score))
        st.write(f"Spam Probability: **{score:.2f}**")

        # Save history
        st.session_state.history.append({
            "Message": msg,
            "Result": result,
            "Score": round(score, 2)
        })

# ----------------------------
# Show history
# ----------------------------
if st.session_state.history:
    st.markdown("### 📜 History")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)
