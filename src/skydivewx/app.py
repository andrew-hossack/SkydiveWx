import datetime
import os

import dash_bootstrap_components as dbc
import pytz
from components.footer import footerComponent
from components.header import headerComponent
from components.home import homePageComponents
from components.webcam import webcamComponents
from components.winds import windsComponents
from dash import (
    Dash,
    Input,
    Output,
    State,
    clientside_callback,
    dcc,
    html,
    no_update,
    ALL,
)
from pages import (
    calendarPage,
    dropzoneMainPage,
    forecastPage,
    planeTrackPage,
    searchPage,
    webcamPage,
    windsAloftPage,
    errorPage,
    manifestPage,
)
from components.manifest.manifestComponents import screenshotImage
from utils.dropzones import dropzones
from utils.dropzones.dropzoneUtils import DropzoneType

app = Dash(
    title="Home | SkydiveWx",
    external_stylesheets=[
        dbc.themes.MATERIA,
        "https://fonts.googleapis.com/css?family=Dosis:200,400,500,600",
    ],
    name=__name__,
    update_title=None,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
)

announcements = html.Div(
    id="announcement-banner",
    children=[
        html.H6(
            children=[
                "Track Your Skydive Live With ",
                html.A(
                    "Paratag",
                    href="https://flyparatag.com/",
                    target="_blank",
                    style={
                        "color": "#0056b3",
                        "textDecoration": "underline",
                    },
                ),
            ],
            style={"margin": "0"},
        ),
    ],
    style={
        "backgroundColor": "rgb(22, 25, 28)",
        "color": "white",
        "padding": "3px",
        "textAlign": "center",
        "fontSize": "14px",
        "fontWeight": "normal",
        "borderRadius": "5px",
        "border": "0.5px solid #A6B3B9",
    },
)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        html.Div(id="hidden-div-callbacks", style={"display": "hidden"}),
        announcements,
        # Refresh interval component - refreshes components every 60 seconds
        dcc.Interval(id="refresh-interval", interval=1000 * 60, n_intervals=0),
        dcc.Interval(id="quick-refresh-interval", interval=1000 * 10, n_intervals=0),
        html.Div(id="page-content"),
    ]
)

# Google Analytics Configuration
ga_measurement_id = os.environ.get("GOOGLE_ANALYTICS_ID", "No GA Measurement ID Given")
app.index_string = (
    """<!DOCTYPE html>
<html>
    <head>
        <!-- Google tag (gtag.js) -->"""
    + """<script async src="https://www.googletagmanager.com/gtag/js?id={0}"></script>""".format(
        ga_measurement_id
    )
    + """<script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        """
    + """gtag('config', '{0}');""".format(ga_measurement_id)
    + """</script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <meta property="og:type" content="article">
        <meta property="og:title" content="Home | SkydiveWx"">
        <meta property="og:site_name" content="https://www.skydivewx.com/">
        <meta property="og:url" content="https://www.skydivewx.com/">
        <meta property="og:image" content="https://www.skydivewx.com/assets/raw_logo.png">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""
)

server = app.server


def _with_header_footer(content: html.Div, dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div(id="header-container", children=headerComponent.render(dropZone)),
        content,
        html.Div(id="footer-container", children=footerComponent.render(dropZone)),
    ]


def _get_dropzone_from_search(search) -> (DropzoneType, None):
    query_parameters = (
        dict(p.split("=") for p in search[1:].split("&")) if search else {}
    )
    possibleDropzoneId = query_parameters.get("id", None)
    return dropzones.Dropzones.get_dropzone_by_id(possibleDropzoneId)


########################
###### CALLBACKS #######
########################


@app.callback(
    Output("page-content", "children"), Input("url", "pathname"), State("url", "search")
)
def render_content(pathname, search):
    try:
        dropZone = _get_dropzone_from_search(search)
        if dropZone:
            if pathname == "/home":
                return _with_header_footer(dropzoneMainPage.render(dropZone), dropZone)
            elif pathname == "/winds":
                return _with_header_footer(windsAloftPage.render(dropZone), dropZone)
            elif pathname == "/calendar":
                return _with_header_footer(calendarPage.render(dropZone), dropZone)
            elif pathname == "/cameras":
                return _with_header_footer(webcamPage.render(dropZone), dropZone)
            elif pathname == "/forecast":
                return _with_header_footer(forecastPage.render(dropZone), dropZone)
            elif pathname == "/track":
                return _with_header_footer(planeTrackPage.render(dropZone), dropZone)
            elif pathname == "/manifest":
                return _with_header_footer(manifestPage.render(dropZone), dropZone)
            else:
                return _with_header_footer(dropzoneMainPage.render(dropZone), dropZone)
        else:
            return html.Div(
                [
                    html.Div(
                        id="header-container",
                        children=headerComponent.searchpageHeader(),
                    ),
                    searchPage.render(dropzones.Dropzones),
                ],
                style={"overflow": "hidden", "position": "fixed"},
            )

    except Exception:
        return errorPage.render()


@app.callback(
    Output("live-clock", "children"),
    Input("header-interval", "n_intervals"),
)
def update_time(n):
    dt_utc = datetime.datetime.now()
    # Change from MST to America/Denver
    dt_mst = dt_utc.astimezone(pytz.timezone("America/Denver"))
    return f'{dt_mst.strftime("%a %m/%d %I:%M:%S %p")} MST'


@app.callback(
    Output("footer-container", "children"),
    Input("refresh-interval", "n_intervals"),
    State("url", "search"),
)
def update_footer(n, search):
    return footerComponent.render(_get_dropzone_from_search(search))


@app.callback(
    Output("weather-page-container", "children"),
    Input("refresh-interval", "n_intervals"),
    State("url", "search"),
)
def refresh_weather(refresh, search):
    return homePageComponents.getAllComponents(_get_dropzone_from_search(search))


@app.callback(
    Output("winds-page-container", "children"),
    Input("refresh-interval", "n_intervals"),
    State("url", "search"),
)
def refresh_winds(refresh, search):
    return windsComponents.getAllComponents(_get_dropzone_from_search(search))


@app.callback(
    Output("webcam-page-container", "children"),
    Input("refresh-interval", "n_intervals"),
    State("url", "search"),
)
def refresh_winds(refresh, search):
    return webcamComponents.getAllComponents(_get_dropzone_from_search(search))


@app.callback(
    Output("header-drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    Input("drawer-demo-label", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(icn, lbl):
    return True


@app.callback(
    Output("url", "href"),
    Input("dropzone-select-mobile", "value"),
    Input("dropzone-select-web", "value"),
)
def search_router(dz1, dz2):
    if dz1 != None:
        # dropzoneId will always be valid from this callback
        return f"/home?id={dz1}"
    if dz2 != None:
        # dropzoneId will always be valid from this callback
        return f"/home?id={dz2}"
    return no_update


clientside_callback(
    """
    function(url) {
        if (url === '/') {
            document.title = 'Home | SkydiveWx'
        } else if (url === '/calendar') {
            document.title = 'Calendar | SkydiveWx'
        } else if (url === '/winds') {
            document.title = 'Winds Aloft | SkydiveWx'
        } else if (url === '/cameras') {
            document.title = 'Live Cameras | SkydiveWx'
        } else if (url === '/forecast') {
            document.title = 'Weather Forecast | SkydiveWx'
        } else if (url === '/search') {
            document.title = 'Find a Dropzone | SkydiveWx'
        } else if (url === '/track') {
            document.title = 'Track Aircraft | SkydiveWx'
        } else {
            document.title = 'Home | SkydiveWx'
        }
    }
    """,
    Output("hidden-div-callbacks", "children"),
    Input("url", "pathname"),
)


@app.callback(
    Output("info-modal", "opened"),
    Input("info-modal-button", "n_clicks"),
    State("info-modal", "opened"),
    prevent_initial_call=True,
)
def info_modal(nc1, opened):
    return not opened


@app.callback(
    Output("help-modal", "opened"),
    Input("help-modal-button", "n_clicks"),
    State("help-modal", "opened"),
    prevent_initial_call=True,
)
def help_modal(nc1, opened):
    return not opened


@app.callback(
    Output("live-manifest-image-container", "children"),
    Input("refresh-interval", "n_intervals"),
    State("url", "search"),
    prevent_initial_call=False,
)
def updateManifest(_, search):
    dropZone = _get_dropzone_from_search(search)
    image = screenshotImage(dropZone)
    return [
        html.Div(
            id="live-manifest-fullscreen-modal",
            children=[html.Button(image, style={"border": "none"})],
        )
    ]


@app.callback(
    Output("live-manifest-fullscreen-modal", "style"),
    Input("live-manifest-image-container", "n_clicks"),
)
def expandManifest(n):
    if n % 2 == 0:
        return {"width": "100%"}
    else:
        return {
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "position": "fixed",
            "zIndex": "1000",
            "paddingTop": "100",
            "left": "0",
            "top": "0",
            "width": "100vw",
            "height": "100vh",
            "overflow": "auto",
            "backdropFilter": "blur(10px)",
        }


@app.callback(
    Output("url", "href", allow_duplicate=True), Input("search-graph", "clickData")
)
def map_click_data(clickData):
    if clickData:
        dz: DropzoneType = dropzones.Dropzones.get_dropzone_by_friendlyName(
            clickData["points"][0]["hovertext"]
        )
        return f"/home?id={dz.id}"


# 'jump-score-help-button' open help modal
@app.callback(
    Output("jump-score-help-modal", "opened"),
    Input("jump-score-help-button", "n_clicks"),
    State("jump-score-help-modal", "opened"),
)
def map_click_data(n, opened):
    if n:
        return not opened


if __name__ == "__main__":
    # TODO AWS Hosting
    # TODO lambda for live manifest
    # TODO lambda for jumpability percentage
    # TODO caching for improved load time
    # TODO: changeable dz page background
    app.run_server(debug=True, port=8050)
