import os
import requests

from dotenv import load_dotenv


load_dotenv()


class TMDBService:

    BASE_URL = "https://api.themoviedb.org/3"

    IMAGE_BASE_URL = (
        "https://image.tmdb.org/t/p/w500"
    )

    def __init__(self):

        self.api_key = os.getenv(
            "TMDB_API_KEY"
        )

        if not self.api_key:
            raise ValueError(
                "TMDB_API_KEY is not configured."
            )


    def search_movie(self, movie_title):

        url = f"{self.BASE_URL}/search/movie"

        params = {
            "api_key": self.api_key,
            "query": movie_title,
            "include_adult": False
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        results = data.get(
            "results",
            []
        )

        if not results:
            return None

        return results[0]


    def get_movie_details(self, movie_id):
        url = f"{self.BASE_URL}/movie/{movie_id}"
        params = {"api_key": self.api_key}

        try:
            response = requests.get(
                url,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"TMDB request failed for movie ID {movie_id}: {e}")
            return None


    def format_movie(self, movie):

        poster_path = movie.get(
            "poster_path"
        )

        return {

            "tmdb_id":
                movie.get("id"),

            "title":
                movie.get("title"),

            "overview":
                movie.get("overview"),

            "release_date":
                movie.get("release_date"),

            "rating":
                movie.get("vote_average"),

            "poster_url":
                (
                    f"{self.IMAGE_BASE_URL}"
                    f"{poster_path}"
                    if poster_path
                    else None
                ),

            "genres":
                [
                    genre["name"]
                    for genre
                    in movie.get("genres", [])
                ]
        }