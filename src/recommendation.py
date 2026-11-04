import os
import joblib

from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


class MovieRecommender:

    def __init__(self):

        self.movies = joblib.load(
            os.path.join(ARTIFACT_DIR, "movies.pkl")
        )

        self.vectorizer = joblib.load(
            os.path.join(ARTIFACT_DIR, "vectorizer.pkl")
        )

        self.vectors = joblib.load(
            os.path.join(ARTIFACT_DIR, "vectors.pkl")
        )

    def recommend(self, movie_name, top_n=10):

        indices = self.movies[
            self.movies["title"].str.casefold()
            == movie_name.casefold()
        ].index

        if len(indices) == 0:
            return []

        movie_index = indices[0]

        scores = cosine_similarity(
            self.vectors[movie_index],
            self.vectors
        ).flatten()

        similar_movies = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for index, score in similar_movies:

            if index == movie_index:
                continue

            recommendations.append({
                "movie_id": int(
                    self.movies.iloc[index]["movie_id"]
                ),
                "title": self.movies.iloc[index]["title"],
                "similarity": round(float(score), 4)
            })

            if len(recommendations) == top_n:
                break

        return recommendations