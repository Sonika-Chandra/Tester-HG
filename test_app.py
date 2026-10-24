from transformers import pipeline

# Downloads the model from Hugging Face the first time, then runs it on your laptop
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

# top_k=None means: give the scores for ALL labels, not just the top one
result = classifier("I love hackathons!", top_k=None)
print(result)