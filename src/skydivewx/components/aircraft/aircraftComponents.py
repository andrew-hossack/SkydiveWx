from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def iframeComponent(dropZone: DropzoneType) -> html.Div():
    return html.Div(
        html.Iframe(src=dropZone.radarBoxUrl,
                    style={"frameborder": "0", "scrolling": "no", "marginheight": "0", "marginwidth": "0", "width": "1200px", "height": "1000px"})
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div([
            iframeComponent(dropZone),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
        }),
    ]
