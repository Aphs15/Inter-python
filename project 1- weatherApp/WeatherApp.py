import requests
import os

API_KEY = os.getenv("OPENWEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q" : city,
        "appid": API_KEY,
        "units": "metric"
    }


    try:
        response = requests.get(BASE_URL, params=params, timeout=5 )
        response.raise_for_status() # raises HTTPError for 4xx/5xx
    except requests.exceptions.Timeout:
        return "Request timed out. Try again."
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"City '{city}' not found."
        return f"HTTP error: {e}"
    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"

    data = response.json()

    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }

def main():
    city = input("Enter city : ").strip()
    result = get_weather(city)

    if isinstance(result, dict):
        print(f"\nWeather in {result['city']}:")
        print(f"  Temp: {result['temp']}°C (feels like {result['feels_like']}°C)")
        print(f"  Condition: {result['description']}")
        print(f"  Humidity: {result['humidity']}%")
    else:
        print(result)

if __name__ == "__main__":
    main()

