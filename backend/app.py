from fastapi import FastAPI
from classifier import classify
from location import extract_location
from complaint_generator import generate_complaint

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    text = data["text"]

    # Step 1: AI classification
    issue = classify(text)

    # Step 2: extract location
    location = extract_location(text)

    # Step 3: generate complaint
    complaint = generate_complaint(issue, location)

    return {
        "input_text": text,
        "issue": issue,
        "location": location,
        "complaint": complaint
    }
