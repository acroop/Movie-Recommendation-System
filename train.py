import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "movies_cleaned.csv"
)

ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


def train_model():

    os.makedirs(ARTIFACT_DIR, exist_ok=True)

    print("Loading processed dataset...")

    movies = pd.read_csv(DATA_PATH)

    movies["tags"] = movies["tags"].fillna("")

    print("Dataset shape:", movies.shape)

    print("Training CountVectorizer...")

    cv = CountVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = cv.fit_transform(movies["tags"])

    print("Vector shape:", vectors.shape)

    print("Saving artifacts...")

    joblib.dump(
        movies,
        os.path.join(ARTIFACT_DIR, "movies.pkl")
    )

    joblib.dump(
        cv,
        os.path.join(ARTIFACT_DIR, "vectorizer.pkl")
    )

    joblib.dump(
        vectors,
        os.path.join(ARTIFACT_DIR, "vectors.pkl")
    )

    print("Model training completed successfully!")


if __name__ == "__main__":
    train_model()