from dash import html
from utils import weatherUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    currentMetar = weatherUtils.get_metar(dropZone.airportIdentifier)
    return html.Div([
        html.Div([
            html.Footer([
                html.A(children="Support this Project - Consider Donating 🙏",
                   href='https://github.com/sponsors/andrew-hossack',
                   target='_blank',
                   style={'textAlign': 'center',
                          'color': '#fff',
                          'padding': '0px',
                          'position': 'sticky',
                          "fontSize": '10px',
                          "display": 'block',
                          }),
                html.A(f'{currentMetar.code} ', id='footer-metar-data'),
            ])
        ], style={
            'textAlign': 'center',
            'paddingTop': '5px',
            'paddingLeft': '10px',
            'paddingRight': '10px',
            'backgroundColor': 'rgba(51, 51, 51, 0.5)',
            'position': 'fixed',
            'bottom': '0',
            'height': 'auto',
            'margin-bottom': '-15px',
            'paddingBottom': '20px',
            'width': '100%',
            'fontSize': '10px',
            'color': 'white',
            'zIndex': '998',
            # 'whiteSpace': 'nowrap',
            'text-wrap':'wrap'
        })
    ],
    style={})