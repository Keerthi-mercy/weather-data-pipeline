import requests
import os
from sqlalchemy import create_engine, text
from datetime import datetime
from prefect import flow, task
from dotenv import load_dotenv

load_dotenv()

@task
def fetch_weather():
    API_KEY = os.getenv("WEATHER_API_KEY")
    CITY = "Chennai"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "recorded_at": datetime.now()
    }
    print("Fetched:", weather_info)
    return weather_info


@task
def save_weather(weather_info):
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    engine = create_engine(f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost/weather_pipeline")

    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS weather_readings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(100),
                temperature FLOAT,
                feels_like FLOAT,
                humidity INT,
                description VARCHAR(100),
                recorded_at DATETIME
            )
        """))
        conn.commit()

        conn.execute(text("""
            INSERT INTO weather_readings (city, temperature, feels_like, humidity, description, recorded_at)
            VALUES (:city, :temperature, :feels_like, :humidity, :description, :recorded_at)
        """), weather_info)
        conn.commit()

    print("Saved to database!")


@flow(name="weather-pipeline-flow")
def weather_pipeline():
    weather_info = fetch_weather()
    save_weather(weather_info)


if __name__ == "__main__":
    weather_pipeline.serve(
        name="weather-pipeline-deployment",
        interval=3600  # runs every 3600 seconds = 1 hour
    )