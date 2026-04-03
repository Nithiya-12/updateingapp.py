import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset (you can expand)
data = {
    "message": [
        "Win money now", "Limited offer click now",
        "Hello how are you", "Let's meet tomorrow",
        "Free gift claim now", "Call me later"
    ],
    "label": [1,1,0,0,1,0]  # 1 = spam, 0 = not spam
}

df = pd.DataFrame(data)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Streamlit UI
st.title("📩 Spam Detection App (ML Based)")

msg = st.text_input("Enter your message")

if st.button("Check"):
    if msg:
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)

        if pred[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
    else:
        st.warning("Please enter a message")