from dash import html

from components import windsComponents


def render() -> html.Div:
    return html.Div(
        [
            windsComponents.renderWindsAloft(),
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent',
        }
    )
