import requests
import random

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


def get_music_link(emotion):
    music_map = {
        "happy": [
            "https://open.spotify.com/track/3tC5TGzZBNUiPax4BfZYmM",
            "https://open.spotify.com/track/2d8JP84HNLKhmd6IYOoupQ",
        ],
        "sad": [
            "https://open.spotify.com/track/1jJci4qxiYcOHhQR247rEU",
            "https://open.spotify.com/track/7LVHVU3tWfcxj5aiPFEW4Q",
        ],
        "angry": [
            "https://open.spotify.com/track/4vUmTMuQqjdnvlZmAH61Qk",
            "https://open.spotify.com/track/0HcHPBu9aaF1MxOiZmUQTl",
        ],
        "surprised": [
            "https://open.spotify.com/track/5YqQJACd1hz0U3i5RYsY8N",
            "https://open.spotify.com/track/6j7hih15xG2aYC5RzVZz0M",
        ],
        "neutral": [
            "https://open.spotify.com/track/3H7ihDc1dqLriiWXwsc2po",
            "https://open.spotify.com/track/5HCyWlXZPP0y6Gqq8TgA20",
        ]
    }

    songs = music_map.get(emotion.lower(), music_map["neutral"])
    return random.choice(songs)
