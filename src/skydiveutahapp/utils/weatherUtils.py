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


def get_metar(airportIdentifier:str, hours=0) -> Metar.Metar:
    try:
        if hours == 0:
            metar = _get_raw_metar(airportIdentifier, hours=hours)
            return Metar.Metar(metar)
        else:
            return [Metar.Metar(metar.text) for metar in _get_raw_metar(airportIdentifier, hours=hours)]
    except IndexError as e:
        print('error: Airport identifier may not have a valid METAR, check surrounding areas for valid metar')
        raise e


def _fetch_hourly_forecast_data(gridpointLocation:str):
    retries = 0
    while retries < 5:
        try:
            response = requests.get(
                f"https://api.weather.gov/gridpoints/{gridpointLocation}/forecast/hourly")
            json_response = response.json()
            return json_response.get("properties").get("periods")
        except AttributeError as e:
            # For some reason sometimes this errors out, so try again
            retries += 1
            pass
    # If you're here its fucked
    return None

def get_forecast(hours: int, gridpointLocation:str):
    data = _fetch_hourly_forecast_data(gridpointLocation)
    return data[:hours]


def _calculate_density_altitude(altimeter_in: float, outside_air_temp_c: float):
    pressure_altitude = ((altimeter_in - 29.92) * 1000) + 4321
    density_altitude = pressure_altitude + (120 * (outside_air_temp_c - 15))
    return round(density_altitude, 0)
