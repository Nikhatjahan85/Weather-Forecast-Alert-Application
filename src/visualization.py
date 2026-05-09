import matplotlib.pyplot as plt
import os

def generate_chart(weather_data):

    labels = ["Temperature", "Humidity", "Wind Speed"]

    values = [
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["wind_speed"]
    ]

    plt.figure(figsize=(6, 4))

    plt.bar(labels, values)

    plt.title(f"Weather Analysis - {weather_data['city']}")

    os.makedirs("outputs", exist_ok=True)

    chart_path = f"outputs/{weather_data['city']}_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path