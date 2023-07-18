from dash import html

from components import weatherComponents


def render() -> html.Div:
    return html.Div(
        [
            weatherComponents.renderCurrentWeather(),
            weatherComponents.renderWeatherForecast(),
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent'
        }
    )
