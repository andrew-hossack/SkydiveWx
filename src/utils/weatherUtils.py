from utils.metar import Metar
import requests
from bs4 import BeautifulSoup

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

if __name__ == "__main__":
    print(get_metar())