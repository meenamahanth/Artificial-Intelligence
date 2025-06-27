import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analyzer")

text = st.text_area("Enter text:")
if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    st.write("Sentiment:", "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral")
