from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY not found in .env file")

API_URL="https://api.weatherapi.com/v1/current.json"