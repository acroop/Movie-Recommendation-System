from fastapi import APIRouter, HTTPException

from app.services.recommendation_service import (
    RecommendationService
)

from app.services.tmdb_service import (
    TMDBService
)


router = APIRouter(
    prefix="/recommend",
    tags=["Recommendations"]
)


recommender = RecommendationService()
tmdb = TMDBService()


@router.get("/{movie_name}")
def recommend(movie_name: str):

    results = recommender.recommend(
        movie_name,
        top_n=10
    )

    if not results:

        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )


    enriched_results = []


    for movie in results:

        tmdb_movie = tmdb.get_movie_details(
            movie["movie_id"]
        )

        if tmdb_movie:

            movie_data = tmdb.format_movie(
                tmdb_movie
            )

            movie_data["similarity"] = (
                movie["similarity"]
            )

            movie_data["movie_id"] = (
                movie["movie_id"]
            )

            enriched_results.append(
                movie_data
            )

        else:

            enriched_results.append(movie)


    return {

        "movie": movie_name,

        "recommendations":
            enriched_results
    }