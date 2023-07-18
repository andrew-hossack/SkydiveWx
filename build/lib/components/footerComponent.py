from dash import html
from ..utils import weatherUtils


def render() -> html.Div:
    currentMetar = weatherUtils.get_metar()
    return html.Div([
        # html.P(currentMetar.remarks()),
        html.Footer(f'{currentMetar.code}', style={
            'textAlign': 'center',
            'paddingTop': '10px',
            'backgroundColor': 'rgba(51, 51, 51, 0.8)',
            'position': 'fixed',
            'bottom': '0',
            'height': '10px',
            'paddingBottom': '20px',
            'width': '100%',
            'fontSize': '10px',
            'color': 'white',
            'zIndex': '998',
        })
    ])
