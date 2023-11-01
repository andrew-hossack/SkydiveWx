from components.calendar import calenderComponents
from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        id="calendar-page-container",
        children=calenderComponents.getAllComponents(dropZone),
        style={
            "padding": "2rem 1rem",
        },
    )
