from utils.metar import Metar
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


def _fetch_hourly_forecast_data():
    response = requests.get(
        "https://api.weather.gov/gridpoints/SLC/85,170/forecast/hourly")
    json_response = response.json()

    return json_response.get("properties").get("periods")


def get_forecast(hours: int):
    data = _fetch_hourly_forecast_data()
    return data[:hours]


def _calculate_density_altitude(altimeter_in: float, outside_air_temp_c: float):
    pressure_altitude = ((altimeter_in - 29.92) * 1000) + 4321
    density_altitude = pressure_altitude + (120 * (outside_air_temp_c - 15))
    return round(density_altitude, 0)
