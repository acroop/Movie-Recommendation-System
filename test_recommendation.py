from src.model_loader import load_recommender


recommender = load_recommender()

result = recommender.recommend(
    "The Dark Knight",
    top_n=10
)

for movie in result:
    print(
        movie["title"],
        movie["similarity"]
    )

   
import time

start = time.perf_counter()

result = recommender.recommend(
    "Interstellar",
    top_n=10
)

end = time.perf_counter()

print("Execution time:", round((end - start) * 1000, 2), "ms")