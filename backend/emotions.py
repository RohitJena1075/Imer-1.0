import os
import requests

# Get the API token from environment variables
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def detect_emotion(text):
    data = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=data)
    try:
        predictions = response.json()
        if isinstance(predictions, list) and len(predictions) > 0:
            # Return the label with the highest score
            return sorted(predictions[0], key=lambda x: x["score"], reverse=True)[0]["label"]
        else:
            return "Error: Unexpected response format"
    except Exception as e:
        return f"Error: {str(e)}"

