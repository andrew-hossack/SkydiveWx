from dash import Dash, html

from components.weather import weatherComponents


def render() -> html.Div:
    return html.Div(
        id='weather-page-container',
        children=weatherComponents.getAllComponents(),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent'
        }
    )
