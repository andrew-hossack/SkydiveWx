from dash import html

from components.home import weatherComponents


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
            'backgroundColor': 'transparent',
            'marginBottom': '20px',
        }
    )
