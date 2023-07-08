import requests


def geocoding(city):
    GEOCODING_API = "https://geocoding-api.open-meteo.com/v1/search"
    PARAMS = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    result = requests.get(GEOCODING_API, params=PARAMS)
    data = result.json()
    latitude = data.get("results")[0].get("latitude")
    longitude = data.get("results")[0].get("longitude")
    return latitude, longitude


def forecast(location):
    FORECAST_API = f"https://api.open-meteo.com/v1/forecast"
    PARAMS = {
        "latitude": location[0],
        "longitude": location[1],
        "hourly": "temperature_2m",
        "current_weather": "true",
        "forecast_days": 1
    }
    response = requests.get(FORECAST_API, params=PARAMS)
    data = response.json()
    current_temperature = data.get('current_weather').get("temperature")
    return current_temperature


def main():
    city = input("Enter a city: ")
    print(round(forecast(geocoding(city))))


if __name__ == '__main__':
    main()
