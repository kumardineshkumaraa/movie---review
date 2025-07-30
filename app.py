import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load the model
model = keras.models.load_model('sentiment_rnn_model.keras')

# Word index from IMDb
word_index = keras.datasets.imdb.get_word_index()
word_index = {k: (v + 3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

# Text preprocessing
def encode_review(text):
    tokens = text.lower().split()
    encoded = [1]  # <START>
    for word in tokens:
        encoded.append(word_index.get(word, 2))  # 2 is <UNK>
    padded = keras.preprocessing.sequence.pad_sequences([encoded], maxlen=200)
    return padded

# Streamlit UI
st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict whether it's positive or negative.")

review = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        padded = encode_review(review)
        prediction = model.predict(padded)[0][0]
        label = "😊 Positive" if prediction > 0.5 else "😞 Negative"
        st.write(f"**Prediction:** {label} (score: {prediction:.4f})")
