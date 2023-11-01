from dash import html
from utils import weatherUtils
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    currentMetar = weatherUtils.get_metar(dropZone.airportIdentifier)
    return html.Div(
        [
            html.Div(
                [
                    html.Footer(
                        [
                            html.A(f"{currentMetar.code} ", id="footer-metar-data"),
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
                                    "margin-right": "5px",
                                },
                            ),
                            html.A(
                                "admin@skydivewx.com",
                                href=f"mailto:admin@skydivewx.com?subject=SkydiveWx - Application Error Report",
                                target="_blank",
                                style={"display": "inline-block", "color": "#fff"},
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
                    # 'height': '20px',
                    # 'margin-bottom': '-15px',
                    "paddingBottom": "5px",
                    "width": "100%",
                    "fontSize": "10px",
                    "color": "white",
                    "zIndex": "998",
                    # 'whiteSpace': 'nowrap',
                    "text-wrap": "wrap",
                },
            )
        ],
        style={},
    )
