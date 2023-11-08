from components.home import homePageComponents
from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        id="weather-page-container",
        children=homePageComponents.getAllComponents(dropZone),
        style={
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "flex-direction": "column",
            "marginTop": "0",
            "backgroundColor": "transparent",
            "padding": "2rem 1rem",
        },
    )
