from src.weather_api import get_current_weather
from src.parser import parse_current_weather
from src.alerts import generate_alerts
from src.visualization import generate_chart
from src.report_generator import save_weather_report
from src.utils import print_weather

# =========================
# CITY INPUT
# =========================

city = input("Enter City Name: ")

# =========================
# FETCH WEATHER DATA
# =========================

data, status = get_current_weather(city)

# =========================
# ERROR HANDLING
# =========================

if status != 200:

    print("❌ Error Fetching Weather Data")

    exit()

# =========================
# PARSE WEATHER DATA
# =========================

weather_data = parse_current_weather(data)

weather_data["city"] = city

# =========================
# PRINT WEATHER REPORT
# =========================

print_weather(weather_data)

# =========================
# GENERATE ALERTS
# =========================

alerts = generate_alerts(weather_data)

print("\n===== WEATHER ALERTS =====")

for alert in alerts:

    print(alert)

# =========================
# GENERATE CHART
# =========================

chart_path = generate_chart(weather_data)

# =========================
# SAVE REPORT
# =========================

report_path = save_weather_report(weather_data)

# =========================
# FINAL OUTPUT
# =========================

print(f"\n📊 Chart Saved: {chart_path}")

print(f"📁 Report Saved: {report_path}")