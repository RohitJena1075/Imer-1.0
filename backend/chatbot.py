import cohere
from backend.utils import load_env
import os
cohere_key = load_env()["cohere_key"]
co = cohere.Client(cohere_key)

def generate_reply(message, emotion, personality):
    tones = {
        "Friendly": "Respond in a friendly and empathetic tone.",
        "Funny": "Respond with humor and witty remarks.",
        "Serious": "Respond professionally and informatively."
    }
    tone = tones.get(personality, "Respond in a friendly tone.")

    full_message = f"{tone} The user feels {emotion}. Message: {message}"

    response = co.chat(
    model="command-r",  # ✅ supported model
    message=full_message,
    max_tokens=150
)


    return response.text.strip()

