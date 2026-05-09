import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Weather Analytics Dashboard",
    page_icon="🌩️",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b1120;
        color: #e2e8f0;
    }

    .main-heading {
        font-size: 48px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .sub-heading {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 25px;
    }

    .black-card {
        background-color: #111827;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #1e293b;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.25);
    }

    .chart-title {
        font-size: 28px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# CITY DATA
# ==================================================

city_coordinates = {

    "Delhi": {"lat": 28.61, "lon": 77.20},
    "Mumbai": {"lat": 19.07, "lon": 72.87},
    "Lucknow": {"lat": 26.85, "lon": 80.95},
    "Kolkata": {"lat": 22.57, "lon": 88.36},
    "Chennai": {"lat": 13.08, "lon": 80.27},
    "Bangalore": {"lat": 12.97, "lon": 77.59},
    "Hyderabad": {"lat": 17.38, "lon": 78.48},
    "Pune": {"lat": 18.52, "lon": 73.85},
    "Jaipur": {"lat": 26.91, "lon": 75.78},
    "Ahmedabad": {"lat": 23.02, "lon": 72.57}
}

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🌩️ Weather Dashboard")

city = st.sidebar.selectbox(
    "🏙️ Select City",
    list(city_coordinates.keys())
)

# ==================================================
# WEATHER API
# ==================================================

def get_weather(city_name):

    lat = city_coordinates[city_name]["lat"]

    lon = city_coordinates[city_name]["lon"]

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

    response = requests.get(url)

    return response.json()

# ==================================================
# WEATHER CONDITIONS
# ==================================================

weather_conditions = {

    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    51: "Drizzle",
    61: "Rain",
    63: "Heavy Rain",
    71: "Snow",
    80: "Rain Showers",
    95: "Thunderstorm",
    99: "Severe Thunderstorm"
}

# ==================================================
# FETCH DATA
# ==================================================

weather_data = get_weather(city)

temperature = weather_data["current"]["temperature_2m"]

humidity = weather_data["current"]["relative_humidity_2m"]

wind_speed = weather_data["current"]["wind_speed_10m"]

weather_code = weather_data["current"]["weather_code"]

weather = weather_conditions.get(weather_code, "Unknown")

# ==================================================
# REAL WEATHER COLORS
# ==================================================

weather_color = "#2563eb"

if "Thunderstorm" in weather:
    weather_color = "#dc2626"

elif "Rain" in weather:
    weather_color = "#0284c7"

elif "Fog" in weather:
    weather_color = "#64748b"

elif "Clear" in weather:
    weather_color = "#0f766e"

elif "Cloud" in weather:
    weather_color = "#475569"

# ==================================================
# ALERT ENGINE
# ==================================================

alerts = []

if temperature > 38:
    alerts.append("🔥 Extreme Heat Alert")

if humidity > 80:
    alerts.append("💧 High Humidity Alert")

if wind_speed > 25:
    alerts.append("🌪️ Strong Wind Alert")

if "Rain" in weather:
    alerts.append("🌧️ Rain Alert")

if "Thunderstorm" in weather:
    alerts.append("⛈️ Thunderstorm Warning")

# ==================================================
# MAIN HEADING
# ==================================================

st.markdown(
    """
    <div class='main-heading'>
    🌩️ Weather Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='sub-heading'>
    Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# CITY BLACK BOX
# ==================================================

st.markdown(
    f"""
    <div class='black-card'>

    <h2>📍 {city}</h2>

    <h3 style='color:{weather_color};'>
    {weather}
    </h3>

    <h1>{temperature} °C</h1>

    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# METRICS
# ==================================================

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#1e293b,#334155);
            padding:22px;
            border-radius:18px;
            border-left:6px solid #f97316;
            box-shadow:0px 4px 15px rgba(0,0,0,0.2);
        ">

        <h4 style='color:#fdba74;'>🌡️ Temperature</h4>

        <h1 style='color:white;'>{temperature} °C</h1>

        </div>
        """,
        unsafe_allow_html=True
    )

with m2:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#0f172a,#1e293b);
            padding:22px;
            border-radius:18px;
            border-left:6px solid #06b6d4;
            box-shadow:0px 4px 15px rgba(0,0,0,0.2);
        ">

        <h4 style='color:#67e8f9;'>💧 Humidity</h4>

        <h1 style='color:white;'>{humidity}%</h1>

        </div>
        """,
        unsafe_allow_html=True
    )

with m3:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#172554,#1e3a8a);
            padding:22px;
            border-radius:18px;
            border-left:6px solid #3b82f6;
            box-shadow:0px 4px 15px rgba(0,0,0,0.2);
        ">

        <h4 style='color:#93c5fd;'>🌪️ Wind Speed</h4>

        <h1 style='color:white;'>{wind_speed}</h1>

        </div>
        """,
        unsafe_allow_html=True
    )

with m4:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#1e293b,#334155);
            padding:22px;
            border-radius:18px;
            border-left:6px solid {weather_color};
            box-shadow:0px 4px 15px rgba(0,0,0,0.2);
        ">

        <h4 style='color:#cbd5e1;'>☁️ Condition</h4>

        <h2 style='color:white;'>{weather}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# ALERTS
# ==================================================

st.markdown("## 🚨 Weather Alerts")

if alerts:

    for alert in alerts:

        if (
            "Heat" in alert
            or "Thunderstorm" in alert
            or "Rain" in alert
        ):

            bg_color = "#7f1d1d"
            border_color = "#ef4444"

        elif (
            "Humidity" in alert
            or "Wind" in alert
        ):

            bg_color = "#082f49"
            border_color = "#38bdf8"

        else:

            bg_color = "#14532d"
            border_color = "#22c55e"

        st.markdown(
            f"""
            <div style="
                background:{bg_color};
                padding:15px;
                border-radius:14px;
                margin-bottom:12px;
                color:white;
                font-weight:bold;
                border-left:6px solid {border_color};
                box-shadow:0px 4px 15px rgba(0,0,0,0.2);
            ">

            {alert}

            </div>
            """,
            unsafe_allow_html=True
        )

else:

    st.markdown(
        """
        <div style="
            background:#14532d;
            padding:15px;
            border-radius:14px;
            color:white;
            font-weight:bold;
            border-left:6px solid #22c55e;
        ">

        ✅ No Active Alerts

        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# FORECAST DATA
# ==================================================

forecast_df = pd.DataFrame({

    "Time": weather_data["hourly"]["time"][:24],

    "Temperature": weather_data["hourly"]["temperature_2m"][:24],

    "Humidity": weather_data["hourly"]["relative_humidity_2m"][:24],

    "Wind Speed": weather_data["hourly"]["wind_speed_10m"][:24]
})

# ==================================================
# CHARTS ROW 1
# ==================================================

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        "<div class='chart-title'>🌡️ Temperature Trend</div>",
        unsafe_allow_html=True
    )

    temp_fig = px.line(
        forecast_df,
        x="Time",
        y="Temperature",
        template="plotly_dark"
    )

    temp_fig.update_layout(
        height=350,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        temp_fig,
        use_container_width=True
    )

with c2:

    st.markdown(
        "<div class='chart-title'>💧 Humidity Analysis</div>",
        unsafe_allow_html=True
    )

    humidity_fig = px.bar(
        forecast_df,
        x="Time",
        y="Humidity",
        color="Humidity",
        template="plotly_dark"
    )

    humidity_fig.update_layout(
        height=350,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        humidity_fig,
        use_container_width=True
    )

# ==================================================
# GAP
# ==================================================

st.markdown("<br>", unsafe_allow_html=True)

# ==================================================
# CHARTS ROW 2
# ==================================================

c3, c4 = st.columns(2)

with c3:

    st.markdown(
        "<div class='chart-title'>🌪️ Wind Speed Trend</div>",
        unsafe_allow_html=True
    )

    wind_fig = px.area(
        forecast_df,
        x="Time",
        y="Wind Speed",
        template="plotly_dark"
    )

    wind_fig.update_layout(
        height=350,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        wind_fig,
        use_container_width=True
    )

with c4:

    st.markdown(
        "<div class='chart-title'>📊 Weather Distribution</div>",
        unsafe_allow_html=True
    )

    pie_df = pd.DataFrame({

        "Category": [
            "Temperature",
            "Humidity",
            "Wind Speed"
        ],

        "Values": [
            temperature,
            humidity,
            wind_speed
        ]
    })

    pie_fig = px.pie(
        pie_df,
        names="Category",
        values="Values",
        hole=0.5,
        template="plotly_dark"
    )

    pie_fig.update_layout(
        height=350,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

# ==================================================
# DATA TABLE
# ==================================================

st.markdown("## 📋 Forecast Data")

st.dataframe(
    forecast_df,
    use_container_width=True
)

# ==================================================
# DOWNLOAD BUTTON
# ==================================================

csv = forecast_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Forecast Report",
    data=csv,
    file_name=f"{city}_weather_report.csv",
    mime="text/csv"
)
