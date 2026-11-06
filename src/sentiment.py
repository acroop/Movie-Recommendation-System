import os
import re
import joblib

from bs4 import BeautifulSoup


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


def clean_text(text):

    text = BeautifulSoup(
        str(text),
        "html.parser"
    ).get_text()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


class SentimentAnalyzer:

    def __init__(self):

        self.vectorizer = joblib.load(
            os.path.join(
                ARTIFACT_DIR,
                "sentiment_vectorizer.pkl"
            )
        )

        self.model = joblib.load(
            os.path.join(
                ARTIFACT_DIR,
                "sentiment_model.pkl"
            )
        )

    def predict(self, review):

        if not isinstance(review, str) or not review.strip():
            raise ValueError("Review cannot be empty.")

        cleaned_review = clean_text(review)

        review_vector = self.vectorizer.transform(
            [cleaned_review]
        )

        prediction = self.model.predict(
            review_vector
        )[0]

        probabilities = self.model.predict_proba(
            review_vector
        )[0]

        sentiment = (
            "Positive" if prediction == 1 else "Negative"
        )

        confidence = float(probabilities[int(prediction)])

        return {
            "sentiment": sentiment,
            "confidence": round(confidence * 100, 2)
        }