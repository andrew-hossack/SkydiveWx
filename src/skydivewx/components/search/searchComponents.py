import dash_mantine_components as dmc
from pandas import DataFrame
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones.dropzones import Dropzones
from components.common.html import mobileDiv, webDiv


def mapBox(dropZones: Dropzones) -> dcc.Graph:
    latitudes = [float(dropzone.lat) for dropzone in dropZones]
    longitudes = [float(dropzone.long) for dropzone in dropZones]
    dropzone_names = [dropzone.friendlyName for dropzone in dropZones]

    data = {
        "lat": latitudes,
        "lon": longitudes,
        "name": dropzone_names,
    }
    df = DataFrame.from_dict(data)

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="name",
        hover_data={"lat": False, "lon": False},
        color_discrete_sequence=["darkgoldenrod"],
        zoom=3,
        height=300,
    )
    fig.update_traces(marker=dict(size=14))
    fig.update_layout(
        hoverlabel=dict(
            font_size=15,
            # font_family="Helvetica Neue",
        )
    )

    fig.update_layout(
        mapbox_style="carto-positron",
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(mapbox=dict(center=dict(lat=39.5, lon=-98.35), zoom=3))

    return html.Div(
        [
            dcc.Graph(id="search-graph", figure=fig, style={"height": "100vh"}),
            html.Div(id="graph-output-none", style={"visibility": "hidden"}),
        ]
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
                        "SkydiveWx is an application developed for skydivers to view current weather and jump conditions at their dropzone. Contact [hello@skydivewx.com](mailto:hello@skydivewx.com) for any inquiries"
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


def renderSearchbarMobile(dropZones: Dropzones) -> html.Div:
    return html.Div(
        style={
            "z-index": "9999",
            "position": "absolute",
            "left": "0",
            "top": "0",
            "height": "100%",
            "maxWidth": "480px",
            "color": "white",
            "paddingTop": "80px",
            "paddingLeft": "30px",
            "paddingRight": "30px",
        },
        children=[
            html.H2(
                f"{len(dropZones)} Dropzones Available",
                style={
                    "color": "white",
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
                        dropdownPosition="bottom",
                        initiallyOpened=True,
                        clearable=True,
                        radius=10,
                        maxDropdownHeight="30vh",
                    )
                ],
                style={"margin": "auto", "padding": "20px"},
            ),
            html.Div(
                [
                    dmc.Divider(
                        variant="dotted",
                        style={
                            "width": "100%",
                        },
                        color="rgba(182, 194, 207, 0.4)",
                        size=1,
                    ),
                    html.Button(
                        id="info-modal-button",
                        children=["Missing your location?"],
                        style={
                            "color": "rgb(182, 194, 207)",
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
                    "marginBottom": "20px",
                    "marginLeft": "20px",
                },
            ),
        ],
    )


def renderSearchbarWeb(dropZones: Dropzones) -> html.Div:
    return html.Div(
        style={
            "z-index": "9999",
            "position": "absolute",
            "margin": "100px 50px",
            "height": "80vh",
            "width": "360px",
            "backgroundColor": "rgba(22,25,28, 0.7)",
            "color": "white",
            "paddingTop": "20px",
            "paddingLeft": "30px",
            "paddingRight": "30px",
            "backdrop-filter": "blur(10px)",
            "border-radius": "10px",
            "overflow": "auto",
        },
        children=[
            html.H2(
                f"{len(dropZones)} Dropzones Available",
                style={
                    "color": "white",
                    "textAlign": "center",
                    "fontWeight": "330",
                    "marginTop": "15px",
                    "padding-left": "20px",
                    "padding-right": "20px",
                },
            ),
            html.Div(
                style={"textAlign": "justify", "fontSize": "16px", "padding": "20px"},
                children=[
                    dcc.Markdown(
                        """
                        Select your dropzone from the list below for real-time weather and jump condition updates with SkydiveWx. 
                        
                        If you do not see your dropzone and would like to add it to the map, please click the "Missing your location?" button below.
                        """
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
                                dropdownPosition="bottom",
                                initiallyOpened=True,
                                clearable=True,
                                radius=10,
                                maxDropdownHeight="250px",
                            )
                        ],
                        style={
                            "margin": "auto",
                            "padding-top": "10px",
                            "width": "260px",
                            "height": "100%",
                            "max-height": "50%",
                            "position": "absolute",
                            "overflow": "hidden",
                        },
                    ),
                ],
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dmc.Divider(
                                variant="dotted",
                                style={
                                    "width": "100%",
                                },
                                color="rgba(182, 194, 207, 0.4)",
                                size=1,
                            ),
                            html.Button(
                                id="info-modal-button",
                                children=["Missing your location?"],
                                style={
                                    "color": "rgb(182, 194, 207)",
                                    "border": "none",
                                    "background": "none",
                                    "fontSize": "13px",
                                },
                                className="nomargin-p",
                            ),
                        ],
                        style={
                            "width": "260px",
                            "margin": "auto",
                        },
                    )
                ],
                style={
                    "flex-direction": "column",
                    "position": "absolute",
                    "bottom": "0",
                    "align-items": "center",
                    "justify-content": "center",
                    "marginBottom": "20px",
                    "width": "300px",
                },
            ),
        ],
    )


def renderInfo() -> html.Div:
    return dmc.Alert(
        "Select a dropzone location from the dropdown or on the map.",
        title="Info",
        icon=DashIconify(icon="fe:info"),
        color="yellow",
        className="alert-div",
        style={
            "z-index": "99999",
            "position": "absolute",
            "border-radius": "10px",
            "right": "60px",
            "top": "80px",
            "font-weight": "500",
        },
    )


def getAllComponents(dropZones: Dropzones) -> list[html.Div]:
    return [
        html.Div(
            [
                info_modal(),
                help_modal(),
                renderInfo(),
                mobileDiv(
                    children=[
                        renderSearchbarMobile(dropZones),
                    ]
                ),
                webDiv(
                    children=[
                        renderSearchbarWeb(dropZones),
                        mapBox(dropZones),
                    ]
                ),
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
