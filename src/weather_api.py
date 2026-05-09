import requests

# =========================
# WEATHER API FUNCTION
# =========================

def get_current_weather(city):

    # =========================
    # CITY COORDINATES
    # =========================

    city_coordinates = {

        "Delhi": {
            "lat": 28.61,
            "lon": 77.20
        },

        "Mumbai": {
            "lat": 19.07,
            "lon": 72.87
        },

        "Lucknow": {
            "lat": 26.85,
            "lon": 80.95
        },

        "Kolkata": {
            "lat": 22.57,
            "lon": 88.36
        },

        "Chennai": {
            "lat": 13.08,
            "lon": 80.27
        },

        "Bangalore": {
            "lat": 12.97,
            "lon": 77.59
        },

        "Hyderabad": {
            "lat": 17.38,
            "lon": 78.48
        },

        "Pune": {
            "lat": 18.52,
            "lon": 73.85
        },

        "Jaipur": {
            "lat": 26.91,
            "lon": 75.78
        },

        "Ahmedabad": {
            "lat": 23.02,
            "lon": 72.57
        },

        "Bhopal": {
            "lat": 23.25,
            "lon": 77.41
        },

        "Patna": {
            "lat": 25.59,
            "lon": 85.13
        }
    }

    # =========================
    # INVALID CITY CHECK
    # =========================

    if city not in city_coordinates:

        return {
            "error": "City not found"
        }, 404

    # =========================
    # GET LATITUDE & LONGITUDE
    # =========================

    lat = city_coordinates[city]["lat"]

    lon = city_coordinates[city]["lon"]

    # =========================
    # OPEN-METEO API URL
    # =========================

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current="
        f"temperature_2m,"
        f"relative_humidity_2m,"
        f"wind_speed_10m,"
        f"weather_code"
        f"&hourly="
        f"temperature_2m,"
        f"relative_humidity_2m,"
        f"wind_speed_10m"
    )

    # =========================
    # API REQUEST
    # =========================

    response = requests.get(url)

    # =========================
    # RETURN DATA
    # =========================

    return response.json(), response.status_code