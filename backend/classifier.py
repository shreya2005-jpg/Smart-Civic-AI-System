
from transformers import pipeline

# AI model for text classification
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "garbage issue",
    "pothole",
    "water problem",
    "electricity issue",
    "drainage issue"
]

def classify(text):
    result = classifier(text, labels)
    return result["labels"][0]
