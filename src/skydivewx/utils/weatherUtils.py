from utils.metar import Metar
import requests


def _get_raw_metar(airport_code, hours=0):
    # Returns parsed json or list of parsed json
    url = f"https://aviationweather.gov/cgi-bin/data/metar.php?ids={airport_code}&hours={hours}"
    retries = 0
    while retries < 5:
        try:
            response = requests.get(url).text.split("\n")
            if hours > 0:
                response.pop()
            else:
                response = response[0]
            return response
        except Exception as e:
            print(f'{e}... retrying {retries}')
            retries += 1
    return None


def get_metar(airportIdentifier: str, hours=0) -> Metar.Metar | None:
    try:
        metar = _get_raw_metar(airportIdentifier, hours=hours)
        if not metar:
            print('No metar found, returning None')
            return None
        if hours == 0:
            return Metar.Metar(metar)
        else:
            return [
                Metar.Metar(metar)
                for metar in _get_raw_metar(airportIdentifier, hours=hours)
            ]
    except IndexError as e:
        print(
            "error: Airport identifier may not have a valid METAR, check surrounding areas for valid metar"
        )
        raise e


def _fetch_hourly_forecast_data(gridpointLocation: str):
    retries = 0
    while retries < 5:
        try:
            response = requests.get(
                f"https://api.weather.gov/gridpoints/{gridpointLocation}/forecast/hourly"
            )
            json_response = response.json()
            return json_response.get("properties").get("periods")
        except AttributeError as e:
            # For some reason sometimes this errors out, so try again
            retries += 1
            pass
    # If you're here its fucked
    return None


def get_forecast(hours: int, gridpointLocation: str):
    data = _fetch_hourly_forecast_data(gridpointLocation)
    return data[:hours]


def _calculate_density_altitude(altimeter_in: float, outside_air_temp_c: float):
    pressure_altitude = ((altimeter_in - 29.92) * 1000) + 4321
    density_altitude = pressure_altitude + (120 * (outside_air_temp_c - 15))
    return round(density_altitude, 0)
