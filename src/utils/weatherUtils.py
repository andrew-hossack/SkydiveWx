from metar import Metar
import requests
from bs4 import BeautifulSoup
import requests


def _get_raw_metar(airport_code, hours=0):
    # Returns parsed json or list of parsed json
    url = f"https://www.aviationweather.gov/metar/data?ids={airport_code}&format=raw&date=&hours={hours}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if hours == 0:
        return soup.find_all('code')[0].text
    else:
        return soup.find_all('code')


def get_metar(hours=0) -> Metar.Metar:
    if hours == 0:
        metar = _get_raw_metar("KTVY", hours=hours)
        return Metar.Metar(metar)
    else:
        return [Metar.Metar(metar.text) for metar in _get_raw_metar("KTVY", hours=hours)]


def get_weather_forecast():
    # https://open-meteo.com/en/docs#latitude=40.6127&longitude=-112.3044&hourly=temperature_2m,rain,cloudcover,visibility,windspeed_10m,windgusts_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=40.6127&longitude=-112.3044&hourly=temperature_2m,rain,cloudcover,visibility,windspeed_10m,windgusts_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1')
    data = response.json()

    # Extract hourly data
    hourly_data = data["hourly"]

    # Create a list of dictionaries, each representing an hour's weather forecast
    forecast_data = [
        {
            "time": hourly_data["time"][i],
            "temperature_2m": hourly_data["temperature_2m"][i],
            "rain": hourly_data["rain"][i],
            "cloudcover": hourly_data["cloudcover"][i],
            "visibility": hourly_data["visibility"][i],
            "windspeed_10m": hourly_data["windspeed_10m"][i],
            "windgusts_10m": hourly_data["windgusts_10m"][i]
        }
        for i in range(len(hourly_data["time"]))
    ]

    return forecast_data
