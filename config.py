from dotenv import load_dotenv
import os
import logging
from logger_func import setup_logger

load_dotenv()

setup_logger()


API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    logging.error("API Key Not found!")
    raise ValueError("API_KEY not found in .env file")

API_URL="https://api.weatherapi.com/v1/current.json"