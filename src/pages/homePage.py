import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, dash
from .components import weatherComponents
from ..utils import weatherUtils


def render() -> html.Div:
    currentMetar = weatherUtils.get_metar()
    return html.Div(
        [
            weatherComponents.renderWind(metar=currentMetar),
            weatherComponents.renderWeather(metar=currentMetar),
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0'
        }
    )