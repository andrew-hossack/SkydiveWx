import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones import dropzoneUtils


def renderSearchbar() -> html.Div:
    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'fontSize': '20px',
            'color': 'white',
            'margin': 'auto',
        },
        children=[
            html.H2("SkydiveWx Home", className="display-7",
                    style={'color': 'white', 'textAlign': 'center'}),
            html.Div([
                dmc.Select(
                    data=[{"value": dz.id, "label": dz.friendlyName}
                          for dz in dropzoneUtils.Dropzones],
                    searchable=True,
                    nothingFound="No match found",
                    style={"width": 'auto'},
                    placeholder='Select your Dropzone',
                    icon=DashIconify(icon="radix-icons:magnifying-glass"),
                    id='dropzone-select',
                )
            ], style={'margin': 'auto'}),
            dcc.Markdown([
                "Not finding your location?"
            ], style={
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'fontSize': '14px',
                'color': 'rgba(255,255,255, 0.3)',
                'paddingTop': '5px'
            }, className='nomargin-p'),
        ]
    )


def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            renderSearchbar(),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'width': '80vw',
            'maxWidth': '750px',
            'marginBottom': '45vh',
        }),
    ]
