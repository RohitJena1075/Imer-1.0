import requests
import random
from backend.utils import load_env
import os
def load_env():
    return {
        "giphy_key": os.getenv("GIPHY_API_KEY"),
        # add more keys if needed
    }
    
GIPHY_API_KEY = load_env()["giphy_key"]

def fetch_gif(emotion):
    try:
        url = "https://api.giphy.com/v1/gifs/search"
        params = {
            "api_key": GIPHY_API_KEY,
            "q": emotion,
            "limit": 10,
            "rating": "pg"
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # raises exception for HTTP errors
        data = response.json()

        if data["data"]:
            gif_data = random.choice(data["data"])
            return gif_data["images"]["downsized_medium"]["url"]
    except Exception as e:
        print(f"Giphy API error: {e}")
    
    # fallback gif
    return "https://media.giphy.com/media/YaOxRsmrv9IeA/giphy.gif"
