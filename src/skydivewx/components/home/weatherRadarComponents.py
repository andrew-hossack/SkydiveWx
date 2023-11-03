from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def radarComponent(dropZone: DropzoneType, height: str = "80vh") -> html.Div():
    return html.Div(
        [
            html.Iframe(
                src=dropZone.weatherRadariFrameUrl,
                style={"border": "0", "width": "100%", "height": height},
            )
        ]
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div(
            [
                radarComponent(dropZone),
            ],
            style={
                "width": "100%",
                "height": "100%",
            },
        ),
    ]
