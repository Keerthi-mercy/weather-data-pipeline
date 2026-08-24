import requests

API_KEY ="c164b3769a827c9de29eec7c69cc2bfe"
CITY = "Chennai"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Pick out only the pieces we care about
weather_info = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"]
}

print(weather_info)