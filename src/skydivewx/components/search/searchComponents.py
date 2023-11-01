import dash_mantine_components as dmc
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones.dropzones import Dropzones


def mapBox(dropZones: Dropzones) -> dcc.Graph:
    latitudes = [float(dropzone.lat) for dropzone in dropZones]
    longitudes = [float(dropzone.long) for dropzone in dropZones]
    dropzone_names = [dropzone.friendlyName for dropzone in dropZones]

    fig = px.scatter_mapbox(
        lat=latitudes,
        lon=longitudes,
        hover_name=dropzone_names,
        color_discrete_sequence=["darkorchid"],
        zoom=3,
        height=300,
    )
    fig.update_traces(marker=dict(size=14))
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_layers=[
            {
                "below": "traces",
                "sourcetype": "raster",
                "sourceattribution": "OpenStreetMap",
                "source": ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            },
            {
                "sourcetype": "raster",
                "sourceattribution": "Stadia Maps",
                "source": [
                    "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
                ],
            },
        ],
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(mapbox=dict(center=dict(lat=40.0902, lon=-108.7129), zoom=4))
    return html.Div(
        [dcc.Graph(id="search-graph", figure=fig, style={"height": "100vh"})]
    )


def help_modal() -> html.Div():
    return html.Div(
        [
            dmc.Modal(
                title="About Us",
                overlayBlur=5,
                id="help-modal",
                overflow="inside",
                centered=True,
                closeOnEscape=True,
                zIndex=100000,
                children=[
                    dcc.Markdown(
                        "SkydiveWx is an application developed for skydivers to view current weather and jump conditions at their dropzone. Contact [hello@skydivewx.com](mailto:hello@skydivewx.com) for any inquiries. Consider [Sponsoring](https://github.com/sponsors/andrew-hossack) the project."
                    )
                ],
            ),
        ]
    )


def info_modal() -> html.Div():
    return html.Div(
        [
            dmc.Modal(
                title="New Dropzone Enrollment",
                overlayBlur=5,
                id="info-modal",
                overflow="inside",
                centered=True,
                closeOnEscape=True,
                zIndex=100000,
                children=[
                    dcc.Markdown(
                        "To request a new dropzone be added, please reach out to [hello@skydivewx.com](mailto:hello@skydivewx.com) for more information on enrolling a new location."
                    )
                ],
            ),
        ]
    )


def renderSearchbar(dropZones: Dropzones) -> html.Div:
    return html.Div(
        style={
            "z-index": "9999",
            "position": "absolute",
            "left": "0",
            "top": "0",
            # 'width': '30vw',
            "height": "100%",
            "maxWidth": "420px",
            "backgroundColor": "rgb(245, 245, 246)",
            "color": "black",
            "paddingTop": "80px",
            "paddingLeft": "30px",
            "paddingRight": "30px",
        },
        children=[
            html.H2(
                f"{len(dropZones)} Dropzones Available",
                style={
                    "color": "black",
                    "textAlign": "center",
                    "fontWeight": "330",
                    "marginTop": "15px",
                },
            ),
            html.Div(
                style={"textAlign": "justify", "fontSize": "16px", "padding": "20px"},
                children=[
                    "Select your dropzone from the list below for real-time weather updates and more with SkydiveWx. Let the skies be your playground. Blue skies and happy landings await!"
                ],
            ),
            html.Div(
                [
                    dmc.Select(
                        data=[
                            {"value": dz.id, "label": dz.friendlyName}
                            for dz in dropZones
                        ],
                        searchable=True,
                        nothingFound="No match found",
                        style={"width": "auto"},
                        placeholder="Find a Dropzone",
                        icon=DashIconify(icon="radix-icons:magnifying-glass"),
                        id="dropzone-select",
                        size="md",
                        variant="default",
                        initiallyOpened=True,
                        clearable=True,
                        radius=10,
                        maxDropdownHeight=400,
                    )
                ],
                style={"margin": "auto", "paddingTop": "20px"},
            ),
            html.Div(
                [
                    dmc.Divider(
                        variant="dotted",
                        style={
                            "width": "100%",
                        },
                        color="rgba(0,0,0, 0.2)",
                        size=1,
                    ),
                    html.Button(
                        id="info-modal-button",
                        children=["Missing your location?"],
                        style={
                            "color": "rgba(0,0,0, 0.2)",
                            "border": "none",
                            "background": "none",
                            "fontSize": "13px",
                        },
                        className="nomargin-p",
                    ),
                ],
                style={
                    "flex-direction": "column",
                    "position": "absolute",
                    "bottom": "0",
                    "align-items": "center",
                    "justify-content": "center",
                    "marginBottom": "20px",  # Remove padding
                },
            ),
        ],
    )


def renderInfo() -> html.Div:
    return dmc.Alert(
        "Scroll and zoom to find a dropzone location near you.",
        title="Info",
        icon=DashIconify(icon="fe:info"),
        color="violet",
        className="alert-div",  # Add this line
        style={
            "z-index": "99999",
            "position": "absolute",
            "border-radius": "10px",
            "right": "60px",
            "top": "80px",
        },
    )


def getAllComponents(dropZones: Dropzones) -> list[html.Div]:
    return [
        html.Div(
            [
                info_modal(),
                help_modal(),
                renderInfo(),
                renderSearchbar(dropZones),
                mapBox(dropZones),
            ],
            style={
                "width": "100%",
                "height": "100%",
                "fontSize": "20px",
                "color": "white",
                "margin": "auto",
            },
        ),
    ]
