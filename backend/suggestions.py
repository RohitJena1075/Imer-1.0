import random
import urllib.parse
import requests

def get_music_link(emotion):
    try:
        query = f"{emotion} mood music"
        encoded_query = urllib.parse.quote(query)
        return f"https://www.youtube.com/results?search_query={encoded_query}"
    except Exception as e:
        print(f"Music suggestion error: {e}")
    
    # Fallback if even that fails
    return "https://www.youtube.com/"

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

