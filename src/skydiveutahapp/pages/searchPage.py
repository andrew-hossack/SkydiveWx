from components.search import searchComponents
from dash import html
from utils.dropzones.dropzoneUtils import Dropzones


def render(dropZones: Dropzones) -> html.Div:
    return html.Div(
        id='search-page-container',
        children=searchComponents.getAllComponents(dropZones),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'margin': '0',
            'height': '100vh',
            'width': '100vw',
        },
    )
