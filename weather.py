import requests
import json

def getWeather():
    city = input("Enter City: ")
    api_key = "f355d9f514bc78317504ca527c6ff706"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    temp = round(data["main"]["temp"] - 273.15, 2)
    description = data["weather"][0]["description"]
    msg = f"The current weather in {city} is {description} with a temperature of {temp}°C."
    return msg