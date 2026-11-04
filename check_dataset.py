import pandas as pd

movies = pd.read_csv("data/raw/tmdb_5000_movies.csv")
credits = pd.read_csv("data/raw/tmdb_5000_credits.csv")

print("Movies shape:", movies.shape)
print("Credits shape:", credits.shape)

print("\nMovies columns:")
print(movies.columns.tolist())

print("\nCredits columns:")
print(credits.columns.tolist())

print("\nFirst 5 movies:")
print(movies[["title", "genres", "overview"]].head())