import requests
import random
from backend.utils import load_env

GIPHY_API_KEY = load_env()["giphy_key"]

def fetch_gif(emotion):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": GIPHY_API_KEY,
        "q": emotion,
        "limit": 10,  # fetch up to 10 gifs
        "rating": "pg"  # avoid explicit content
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["data"]:
        gif_data = random.choice(data["data"])
        return gif_data["images"]["downsized_medium"]["url"]
    else:
        # fallback gif
        return "https://media.giphy.com/media/YaOxRsmrv9IeA/giphy.gif"

