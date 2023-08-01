import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones.dropzoneUtils import Dropzones
from utils.dropzones import dropzoneUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def mapBox(dropZones: Dropzones) -> dcc.Graph:
    latitudes = [float(dropzone.lat) for dropzone in dropZones]
    longitudes = [float(dropzone.long) for dropzone in dropZones]
    dropzone_names = [dropzone.friendlyName for dropzone in dropZones]

    fig = px.scatter_mapbox(lat=latitudes, lon=longitudes, hover_name=dropzone_names,
                            color_discrete_sequence=["coral"], zoom=3, height=300)
    fig.update_traces(marker=dict(size=10))
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            },
            {
                "sourcetype": "raster",
                "sourceattribution": "Government of Canada",
                "source": ["https://geo.weather.gc.ca/geomet/?"
                           "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                           "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
            }
        ])
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return html.Div([
        _renderSearchbar(),
        dcc.Graph(figure=fig, style={'height': '100vh'})
    ])


def _renderSearchbar() -> html.Div:
    return html.Div(
        style={
            'z-index': '99999',
            'position': 'absolute',
            'left': '50%',  # Center horizontally
            'top': '30%',  # Center vertically
            'transform': 'translate(-50%, -50%)',
            'width': '80vw',
            'maxWidth':'400px'
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
            ], style={'margin': 'auto', 'paddingTop': '20px'}),
            dcc.Markdown([
                "Not finding your location?"
            ], style={
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'fontSize': '14px',
                'color': 'rgba(255,255,255, 0.3)',
                'paddingTop': '5px',
            }, className='nomargin-p'),
        ]
    )


def getAllComponents(dropZones: Dropzones) -> list[html.Div]:
    return [
        html.Div([
            mapBox(dropZones),
        ], style={
            'width': '100%',
            'height': '100%',
            'fontSize': '20px',
            'color': 'white',
            'margin': 'auto',
        }),
    ]
