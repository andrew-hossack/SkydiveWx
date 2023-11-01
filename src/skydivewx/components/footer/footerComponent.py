from dash import html
from utils import weatherUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    currentMetar = weatherUtils.get_metar(dropZone.airportIdentifier)
    return html.Div([
        html.Div([
            html.Footer([
                html.A(f'{currentMetar.code} ', id='footer-metar-data'),

                html.A(children="Support this Project",
                       href='https://github.com/sponsors/andrew-hossack',
                       target='_blank',
                       style={'textAlign': 'center',
                              'color': '#fff',
                              'padding': '0px',
                              'position': 'sticky',
                              "fontSize": '10px',
                              "display": 'block',
                              }),
            ])
        ], style={
            'textAlign': 'center',
            'paddingTop': '5px',
            'paddingLeft': '10px',
            'paddingRight': '10px',
            'backgroundColor': 'rgba(51, 51, 51, 0.5)',
            'position': 'relative',
            'bottom': '0',
            # 'height': '20px',
            # 'margin-bottom': '-15px',
            'paddingBottom': '5px',
            'width': '100%',
            'fontSize': '10px',
            'color': 'white',
            'zIndex': '998',
            # 'whiteSpace': 'nowrap',
            'text-wrap': 'wrap'
        })
    ],
        style={})
