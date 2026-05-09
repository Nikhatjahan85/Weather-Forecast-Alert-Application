from src.config import (
    TEMP_THRESHOLD,
    HUMIDITY_THRESHOLD,
    WIND_THRESHOLD
)

def generate_alerts(weather_data):

    alerts = []

    if weather_data["temperature"] > TEMP_THRESHOLD:
        alerts.append("⚠️ High Temperature Alert")

    if weather_data["humidity"] > HUMIDITY_THRESHOLD:
        alerts.append("⚠️ High Humidity Alert")

    if weather_data["wind_speed"] > WIND_THRESHOLD:
        alerts.append("⚠️ High Wind Speed Alert")

    if "rain" in weather_data["weather"].lower():
        alerts.append("⚠️ Rain Alert")

    if not alerts:
        alerts.append("✅ No Weather Alerts")

    return alerts