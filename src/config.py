import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

TEMP_THRESHOLD = 35
HUMIDITY_THRESHOLD = 80
WIND_THRESHOLD = 10