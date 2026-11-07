from app.services.tmdb_service import TMDBService


tmdb = TMDBService()


movie = tmdb.search_movie(
    "The Dark Knight"
)


if movie:

    print("TMDB ID:", movie["id"])
    print("Title:", movie["title"])
    print("Release:", movie["release_date"])
    print("Rating:", movie["vote_average"])
    print("Poster:", movie["poster_path"])

else:

    print("Movie not found")