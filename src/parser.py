def parse_current_weather(data):

    temperature = data["current"]["temperature_2m"]

    humidity = data["current"]["relative_humidity_2m"]

    wind_speed = data["current"]["wind_speed_10m"]

    weather_code = data["current"]["weather_code"]

    # =========================
    # WEATHER CONDITION MAPPING
    # =========================

    weather_conditions = {

        0: "Clear Sky",

        1: "Mainly Clear",

        2: "Partly Cloudy",

        3: "Overcast",

        45: "Fog",

        48: "Depositing Rime Fog",

        51: "Light Drizzle",

        53: "Moderate Drizzle",

        55: "Dense Drizzle",

        61: "Slight Rain",

        63: "Moderate Rain",

        65: "Heavy Rain",

        71: "Slight Snow",

        73: "Moderate Snow",

        75: "Heavy Snow",

        80: "Rain Showers",

        81: "Moderate Rain Showers",

        82: "Violent Rain Showers",

        95: "Thunderstorm",

        96: "Thunderstorm with Hail",

        99: "Heavy Thunderstorm with Hail"
    }

    weather = weather_conditions.get(
        weather_code,
        "Unknown Weather"
    )

    weather_data = {

        "city": "Selected City",

        "temperature": temperature,

        "humidity": humidity,

        "weather": weather,

        "wind_speed": wind_speed
    }

    return weather_data