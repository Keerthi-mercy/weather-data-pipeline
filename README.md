# 🌤️ Weather Data Pipeline

An automated ETL data pipeline that fetches live weather data from a public API, stores it in a MySQL database on a scheduled basis, and visualizes it through an interactive dashboard.

## Features
- **Extract:** Pulls real-time weather data (temperature, humidity, conditions) from the OpenWeatherMap API
- **Transform:** Cleans and structures raw JSON into a usable format
- **Load:** Stores data in a MySQL database with automatic table creation
- **Orchestration:** Uses Prefect to schedule and monitor automated hourly runs
- **Visualization:** Interactive Streamlit dashboard showing live metrics and historical trends

## Tech Stack
Python · Prefect · MySQL · SQLAlchemy · Streamlit · OpenWeatherMap API

## How It Works
1. `fetch_weather.py` — initial data extraction script
2. `save_to_db.py` — Prefect-orchestrated pipeline that fetches and loads data into MySQL on an hourly schedule
3. `dashboard.py` — Streamlit dashboard that queries the database and displays live weather metrics and trends

## Setup
1. Clone this repository
2. Install dependencies: `pip install requests pandas sqlalchemy prefect streamlit pymysql python-dotenv`
3. Create a `.env` file with your `WEATHER_API_KEY` and `MYSQL_PASSWORD`
4. Run the pipeline: `python save_to_db.py`
5. Launch the dashboard: `streamlit run dashboard.py`
