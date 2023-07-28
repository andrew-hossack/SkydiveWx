from dash import html

from components.home import weatherRadarComponents


def render() -> html.Div:
    return html.Div(
        id='forecast-page-container',
        children=weatherRadarComponents.getAllComponents(),
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
