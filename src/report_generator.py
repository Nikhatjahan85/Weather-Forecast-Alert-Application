import pandas as pd
import os
from datetime import datetime

def save_weather_report(weather_data):

    report = pd.DataFrame({
        "City": [weather_data["city"]],
        "Temperature": [weather_data["temperature"]],
        "Humidity": [weather_data["humidity"]],
        "Weather": [weather_data["weather"]],
        "Wind Speed": [weather_data["wind_speed"]],
        "Generated Time": [datetime.now()]
    })

    os.makedirs("reports", exist_ok=True)

    file_path = "reports/weather_report.csv"

    report.to_csv(file_path, index=False)

    return file_path