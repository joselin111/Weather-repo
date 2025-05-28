# weather.py
import requests
import os

# Get API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# City to fetch weather for
city = "London"

# Construct API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Make the GET request
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current weather in {city}: {temp}°C, {weather}")
else:
    print(f"Failed to retrieve weather data. Status: {response.status_code}")
    print("Response:", response.text)
