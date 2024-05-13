from dash import html
from utils import weatherUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    currentMetar = weatherUtils.get_metar(
        dropZone.airportIdentifier.metarAirportIdentifier
    )
    return html.Div(
        [
            html.Div(
                [
                    html.Footer(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.A(
                                                children="Support this Project",
                                                href="https://github.com/sponsors/andrew-hossack",
                                                target="_blank",
                                                style={
                                                    "textAlign": "center",
                                                    "padding": "0px",
                                                    "position": "sticky",
                                                    "color": "#fff",
                                                    "display": "inline-block",
                                                },
                                            ),
                                            html.P(
                                                "•",
                                                style={
                                                    "display": "inline-block",
                                                    "color": "#fff",
                                                    "margin-right": "5px",
                                                    "margin-left": "5px",
                                                },
                                            ),
                                            html.A(
                                                "Contact Us",
                                                href=f"mailto:hello@skydivewx.com",
                                                target="_blank",
                                                style={
                                                    "display": "inline-block",
                                                    "color": "#fff",
                                                },
                                            ),
                                        ],
                                        style={"margin-bottom": "-5px"},
                                    ),
                                ]
                            ),
                            html.A(
                                f"{currentMetar.code if currentMetar else ''} ",
                                id="footer-metar-data",
                            ),
                        ]
                    )
                ],
                style={
                    "textAlign": "center",
                    "paddingTop": "5px",
                    "fontSize": "10px",
                    "paddingLeft": "10px",
                    "paddingRight": "10px",
                    "backgroundColor": "rgba(51, 51, 51, 0.5)",
                    "position": "relative",
                    "bottom": "0",
                    "width": "100%",
                    "fontSize": "10px",
                    "color": "white",
                    "zIndex": "998",
                    "text-wrap": "wrap",
                },
            )
        ],
        style={},
    )
