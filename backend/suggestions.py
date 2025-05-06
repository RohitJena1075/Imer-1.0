import requests
import random

def get_music_link(emotion):
    query = f"{emotion} mood"
    url = f"https://api.deezer.com/search?q={query}"
    try:
        response = requests.get(url)
        data = response.json()
        if "data" in data and data["data"]:
            track = random.choice(data["data"])
            return track["link"]  # Deezer track link
    except Exception as e:
        print(f"Deezer API error: {e}")
    
    # fallback if Deezer fails
    return "https://www.deezer.com/en/"
