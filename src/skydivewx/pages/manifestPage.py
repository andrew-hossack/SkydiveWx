from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType
from components.manifest import manifestComponents


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        id="manifest-page-container",
        children=manifestComponents.getAllComponents(dropZone),
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
