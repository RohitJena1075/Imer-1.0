import json

def save_chat_to_json(user_msg, bot_msg, emotion, personality):
    entry = {
        "user": user_msg,
        "bot": bot_msg,
        "emotion": emotion,
        "personality": personality
    }
    with open("chat_memory.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
