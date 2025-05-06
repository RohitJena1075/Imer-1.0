from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.chatbot import generate_reply
from backend.emotions import detect_emotion
from backend.gifs import fetch_gif
from backend.suggestions import get_quote, get_music_link
from backend.memory import save_chat_to_json

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://SoulGainer1075--Imer-1-0.hf.space"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Imer Chatbot! Use POST /chat with JSON data."}

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        message = data["message"]
        personality = data.get("personality", "Friendly")

        emotion = detect_emotion(message)
        reply = generate_reply(message, emotion, personality)
        gif_url = fetch_gif(emotion)
        quote = get_quote()
        music = get_music_link(emotion)

        save_chat_to_json(message, reply, emotion, personality)

        return {
            "reply": reply,
            "emotion": emotion,
            "gif": gif_url,
            "quote": quote,
            "music": music
        }
    except Exception as e:
        print(f"API Error: {e}")  # Logs to terminal
        return {"error": str(e)}

        
