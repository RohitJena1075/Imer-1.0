import os
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def detect_emotion(text):
    data = {"inputs": text}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()  # Raises error if status is not 200
        predictions = response.json()

        if isinstance(predictions, list) and len(predictions) > 0:
            top_prediction = sorted(predictions[0], key=lambda x: x["score"], reverse=True)[0]
            return top_prediction["label"]
        else:
            return "neutral"  # fallback emotion
    except Exception as e:
        print(f"Emotion detection error: {e}")
        return "neutral"
