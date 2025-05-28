import requests

API_KEY = "f35455d89339b81fef34e9664c107d1f"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
print(f"Current weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
