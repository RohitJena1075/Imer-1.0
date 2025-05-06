import os
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def detect_emotion(text):
    data = {"inputs": text}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
        predictions = response.json()

        if isinstance(predictions, list) and len(predictions) > 0:
            top_prediction = sorted(predictions[0], key=lambda x: x["score"], reverse=True)[0]
            return top_prediction["label"]
        else:
            return "neutral"
    except Exception as e:
        print(f"Emotion detection error: {e}")
        return "neutral"
