import requests
import json

def fetch_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

def display_weather_data(weather_data):
    if weather_data is None:
        print("Unable to fetch weather data.")
        return

    main_data = weather_data["main"]
    weather = weather_data["weather"][0]

    print("Current weather in", weather_data["name"], ":", weather["description"])
    print("Temperature:", main_data["temp"], "°C")
    print("Humidity:", main_data["humidity"], "%")
    print("Wind Speed:", weather_data["wind"]["speed"], "m/s")

def main():
    api_key = "16f46e8e2a1c31911c83fb761e13a482"  # Replace with your OpenWeatherMap API key
    location = input("Enter a location: ")
    
    weather_data = fetch_weather_data(api_key, location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
