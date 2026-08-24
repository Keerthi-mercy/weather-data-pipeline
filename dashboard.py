import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Connect to our database
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
engine = create_engine(f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost/weather_pipeline")

# Load all weather readings into a table
df = pd.read_sql("SELECT * FROM weather_readings ORDER BY recorded_at", engine)

# ---- Dashboard layout ----
st.title("🌤️ Chennai Weather Pipeline Dashboard")
st.write("Live weather data collected automatically every hour")

# Show the latest reading as big numbers
latest = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f"{latest['temperature']} °C")
col2.metric("Feels Like", f"{latest['feels_like']} °C")
col3.metric("Humidity", f"{latest['humidity']} %")

st.write(f"Current condition: **{latest['description']}**")

# Line chart of temperature over time
st.subheader("Temperature Over Time")
st.line_chart(df.set_index("recorded_at")["temperature"])

# Show the raw data table
st.subheader("All Recorded Readings")
st.dataframe(df)