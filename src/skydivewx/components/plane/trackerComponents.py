from dash import html
from utils.dropzones.dropzoneUtils import DropzoneType


def planeTrackIframe(
    dropZone: DropzoneType,
    width: str = "100%",
    height: str = "500px",
    hideSidebar: bool = True,
    hideButtons: bool = True,
) -> html.Iframe:
    return html.Iframe(
        # https://www.adsbexchange.com/map-help/
        src=f"https://globe.adsbexchange.com?scale=1{'&hideSidebar' if hideSidebar else ''}{'&hideButtons' if hideButtons else ''}&airport={dropZone.airportIdentifier}&zoom=11&extendedLabels=1&icao={dropZone.aircraftInfo.aircraftIcao if dropZone.aircraftInfo.aircraftIcao else ''}",
        style={
            "width": width,
            "height": height,
            "frameBorder": "0",
            "margin-bottom": "-10px",
        },
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div(
            [
                planeTrackIframe(
                    dropZone,
                    width="100%",
                    height="100%",
                    hideButtons=False,
                    hideSidebar=False,
                )
            ],
            style={
                "width": "100%",
                "height": "80vh",
            },
        ),
    ]
