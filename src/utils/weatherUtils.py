from metar import Metar
import requests
from bs4 import BeautifulSoup
import requests
import json


def _get_raw_metar(airport_code):
    url = f"https://www.aviationweather.gov/metar/data?ids={airport_code}&format=raw&date=&hours=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    metar_data = soup.find_all('code')[0].text
    return metar_data


def get_metar() -> Metar.Metar:
    metar = _get_raw_metar("KTVY")
    # station: KTVY
    # type: routine report, cycle 2 (automatic report)
    # time: Tue Jul 18 02:15:00 2023
    # temperature: 30.0 C
    # dew point: 11.0 C
    # wind: N at 6 knots
    # visibility: 10 miles
    # pressure: 1017.6 mb
    # sky: clear
    # remarks:
    # - Automated station (type 2)
    # METAR: KTVY 180215Z AUTO 01006KT 10SM CLR 30/11 A3005 RMK AO2
    return Metar.Metar(metar)


# https://api.open-meteo.com/v1/forecast?latitude=40.6127&longitude=-112.3044&hourly=temperature_2m,rain,cloudcover,visibility,windspeed_10m

# async def _getweather():
#     async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
#         weather = await client.get('4663 N Airport Rd, Erda, UT 84074')
#         forecasts = []
#         # get the weather forecast for a few days
#         for forecast in weather.forecasts:
#             # hourly forecasts
#             for hourly in forecast.hourly:
#                 forecasts.append(hourly)
#         return forecasts


# def get_weather_forecast():
#     if os.name == 'nt':
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     # Capture the returned weather object
#     return asyncio.run(_getweather())[:3]


def get_weather_forecast():
    # https://open-meteo.com/en/docs#latitude=40.6127&longitude=-112.3044&hourly=temperature_2m,rain,visibility,windspeed_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=40.6127&longitude=-112.3044&hourly=temperature_2m,rain,cloudcover,visibility,windspeed_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1')
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
            "windspeed_10m": hourly_data["windspeed_10m"][i]
        }
        for i in range(len(hourly_data["time"]))
    ]

    return forecast_data
