from dash import html
from utils import weatherUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    currentMetar = weatherUtils.get_metar(dropZone.airportIdentifier)
    return html.Div([
        html.Div([
            html.Footer([
                html.A(f'{currentMetar.code} ', id='footer-metar-data'),
                html.A('View Raw METAR', href='https://www.aviationweather.gov/metar/data?ids=ktvy&format=decoded&hours=1&taf=off&layout=on', target='_blank')
            ])
        ], style={
            'textAlign': 'center',
            'paddingTop': '10px',
            'paddingLeft': '10px',
            'paddingRight': '10px',
            'backgroundColor': 'rgba(51, 51, 51, 0.5)',
            'position': 'fixed',
            'bottom': '0',
            'height': '10px',
            'paddingBottom': '20px',
            'width': '100%',
            'fontSize': '10px',
            'color': 'white',
            'zIndex': '998',
            'whiteSpace': 'nowrap'
        })
    ])