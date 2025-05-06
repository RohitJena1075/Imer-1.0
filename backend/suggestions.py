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

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        if res.status_code == 200:
            quote_data = res.json()
            return f'{quote_data[0]["q"]} — {quote_data[0]["a"]}'
        else:
            return "Stay positive and keep going!"
    except Exception as e:
        return "Stay positive!"

