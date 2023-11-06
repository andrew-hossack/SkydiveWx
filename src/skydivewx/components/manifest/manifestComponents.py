from dash import html
import dash_bootstrap_components as dbc
from utils.dropzones.dropzoneUtils import DropzoneType
from utils.screenshotUtils import getBurbleScreenshot
from uuid import uuid1


def screenshotImage(
    dropZone: DropzoneType,
    width: any = "100%",
    height: any = "100%",
    includeLink: bool = False,
) -> html.Div:
    image = html.Img(
        src="data:image/png;base64, " + getBurbleScreenshot(dropZone.liveManifestUrl),
        width=width,
        height=height,
    )
    if includeLink:
        return html.A(
            image,
            href=dropZone.liveManifestUrl,
            target="_blank",
        )
    else:
        return image


def getScreenshotImageContainer() -> html.Div:
    return html.Div(
        children=[
            html.Div(
                dbc.Spinner(color="primary"),
                style={"width": "100%", "textAlign": "center", "padding-top": "20px"},
            )
        ],
        id={"type": "live-manifest-image-container", "index": str(uuid1())},
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.H2(f"{dropZone.friendlyName} Live Manifest", style={"color": "white"}),
        html.A(
            "Burble Live Manifest Link",
            href=dropZone.liveManifestUrl,
            target="_blank",
            style={"color": "white", "padding-bottom": "20px"},
            className="darker-link-color",
        ),
        getScreenshotImageContainer(),
    ]
