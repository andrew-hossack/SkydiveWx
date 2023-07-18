import dash_bootstrap_components as dbc
from dash import html

from components import weatherComponents
from utils import weatherUtils


def render() -> html.Div:
    currentMetar = weatherUtils.get_metar()
    return html.Div(
        [
            weatherComponents.renderCurrentWeather(metar=currentMetar),
            weatherComponents.renderWeatherForecast(),
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor':'transparent'
        }
    )