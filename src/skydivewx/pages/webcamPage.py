from components.webcam import webcamComponents
from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        id="webcam-page-container",
        children=webcamComponents.getAllComponents(dropZone),
        style={
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "flex-direction": "column",
            "marginTop": "0",
            "backgroundColor": "transparent",
            "marginBottom": "20px",
            "padding": "2rem 1rem",
        },
    )
