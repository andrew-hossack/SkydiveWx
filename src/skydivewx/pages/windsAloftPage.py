from components.winds import windsComponents
from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        id='winds-page-container',
        children=windsComponents.getAllComponents(dropZone),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'marginBottom': '20px',
            'backgroundColor': 'transparent',
            "padding": "2rem 1rem",
        }
    )
