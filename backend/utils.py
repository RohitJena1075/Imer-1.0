from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        # "openai_key": os.getenv("OPENAI_API_KEY"),     # Optional now
        "giphy_key": os.getenv("GIPHY_API_KEY"),
        "cohere_key": os.getenv("COHERE_API_KEY")
    }


