import os

def load_env():
    return {
        "giphy_key": os.getenv("GIPHY_API_KEY"),
        "cohere_key": os.getenv("COHERE_API_KEY")
    }



