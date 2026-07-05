import streamlit as st
import pickle
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Load Model
model = pickle.load(open("logistic_sentiment_model.pkl", "rb"))

# Load TF-IDF Vectorizer
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text Preprocessing
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):

    text = text.lower()

    text = re.sub(r'<.*?>', '', text)

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)


# Streamlit UI
st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Analysis")

st.write("Predict whether a movie review is Positive or Negative.")

review = st.text_area(
    "Enter Movie Review",
    height=200
)

if st.button("Predict"):

    if review.strip() == "":

        st.warning("Please enter a movie review.")

    else:

        cleaned_review = clean_text(review)

        vector = tfidf.transform([cleaned_review])

        prediction = model.predict(vector)

        if prediction[0] == 1:

            st.success("😊 Positive Review")

        else:

            st.error("😞 Negative Review")