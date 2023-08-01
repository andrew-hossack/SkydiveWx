import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones.dropzoneUtils import Dropzones
from utils.dropzones import dropzoneUtils


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
        dcc.Graph(id='search-graph', figure=fig, style={'height': '100vh'})
    ])


def _info_modal() -> html.Div():
    return html.Div(
        [
            dmc.Modal(
                title="New Dropzone Request",
                overlayBlur=5,
                id="info-modal",
                overflow="inside",
                centered=True,
                closeOnEscape=True,
                zIndex=100000,
                children=[dmc.Text(
                    "To request a new dropzone be added, please reach out to andrew_hossack@outlook.com for more information.")],
            ),
        ]
    )


def _renderSearchbar() -> html.Div:
    return html.Div(
        style={
            'z-index': '99999',
            'position': 'absolute',
            'left': '50%',  # Center horizontally
            'top': '30%',  # Center vertically
            'transform': 'translate(-50%, -50%)',
            'width': '80vw',
            'maxWidth': '450px',
        },
        children=[
            html.H2("SkydiveWx Home", className="display-6",
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
                    size='md'
                )
            ], style={'margin': 'auto', 'paddingTop': '20px'}),
            html.Button(
                id='info-modal-button',
                children=[
                    "Not finding your location?"
                ], style={
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'fontSize': '12px',
                    'color': 'rgba(255,255,255, 0.4)',
                    'paddingTop': '5px',
                    "border": "none",  # Remove the border
                    "background": "none",  # Remove the background
                    "padding": "0",  # Remove padding
                    "fontSize": "16px",  # Set font size for better visibility
                }, className='nomargin-p'),
        ]
    )


def getAllComponents(dropZones: Dropzones) -> list[html.Div]:
    return [
        html.Div([
            _info_modal(),
            mapBox(dropZones),
        ], style={
            'width': '100%',
            'height': '100%',
            'fontSize': '20px',
            'color': 'white',
            'margin': 'auto',
        }),
    ]
