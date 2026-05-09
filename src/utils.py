def print_weather(weather_data):

    print("\n===== WEATHER REPORT =====")

    print(f"City: {weather_data['city']}")
    print(f"Temperature: {weather_data['temperature']} °C")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Weather: {weather_data['weather']}")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")