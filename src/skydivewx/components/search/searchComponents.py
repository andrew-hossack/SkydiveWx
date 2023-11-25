import dash_mantine_components as dmc
from pandas import DataFrame
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify
from utils.dropzones.dropzones import Dropzones


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
    fig.update_layout(mapbox=dict(center=dict(lat=40.6117, lon=-120.3475), zoom=3))

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


def renderSearchbar(dropZones: Dropzones) -> html.Div:
    return html.Div(
        style={
            "z-index": "9999",
            "position": "absolute",
            "left": "0",
            "top": "0",
            "height": "100%",
            "maxWidth": "420px",
            "backgroundColor": "rgb(22,25,28)",
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
                },
            ),
        ],
    )


def renderInfo() -> html.Div:
    return dmc.Alert(
        "Scroll and zoom to find a dropzone location near you.",
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
