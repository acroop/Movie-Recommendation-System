from src.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()

reviews = [
    "This movie was absolutely brilliant. I loved every moment!",
    "Terrible movie. Poor acting and boring storyline.",
    "The movie was not bad, but it could have been better."
]

for review in reviews:

    result = analyzer.predict(review)

    print("\nReview:", review)
    print("Prediction:", result["sentiment"])
    print("Confidence:", result["confidence"], "%")