import datetime
import os

import dash_bootstrap_components as dbc
import pytz
from components.footer import footerComponent
from components.header import headerComponent
from components.home import weatherComponents
from components.webcam import webcamComponents
from components.winds import windsComponents
from dash import Dash, Input, Output, clientside_callback, dcc, html
from pages import (aircraftPage, calendarPage, forecastPage, homePage,
                   webcamPage, windsAloftPage)

app = Dash(
    title="Dashboard | Skydive Utah App",
    external_stylesheets=[
        dbc.themes.MATERIA,
        "https://fonts.googleapis.com/css?family=Dosis:200,400,500,600"],
    name=__name__,
    update_title=None,
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        html.Div(id='hidden-div-callbacks', style={'display': 'hidden'}),
        # Refresh interval component - refreshes components every 60 seconds
        dcc.Interval(id='refresh-interval', interval=1000*60, n_intervals=0),
        html.Div(id='header-container', children=headerComponent.render()),
        html.Div(
            id='page-content',
            style={
                "padding": "2rem 1rem",
            },
        ),
        html.Div(id='footer-container', children=footerComponent.render())
    ]
)

# Google Analytics Configuration
ga_measurement_id = os.environ.get(
    'GOOGLE_ANALYTICS_ID', 'No GA Measurement ID Given')
app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Google tag (gtag.js) -->""" +\
    """<script async src="https://www.googletagmanager.com/gtag/js?id={0}"></script>""".format(ga_measurement_id) +\
    """<script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        """ +\
    """gtag('config', '{0}');""".format(ga_measurement_id) +\
    """</script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <meta property="og:type" content="article">
        <meta property="og:title" content="Skydive Utah App - Dashboard"">
        <meta property="og:site_name" content="https://skydive-utah-app.onrender.com">
        <meta property="og:url" content="https://skydive-utah-app.onrender.com">
        <meta property="og:image" content="https://images.squarespace-cdn.com/content/v1/5873e8be197aeae83a43b6fa/1524793837166-4WWI32TLDQIVQSPNF0WT/Newer+Logo.png?format=1500w">
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

server = app.server

########################
###### CALLBACKS #######
########################


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"))
def router(pathname):
    if pathname == "/":
        return [homePage.render()]
    elif pathname == "/winds":
        return [windsAloftPage.render()]
    elif pathname == "/calendar":
        return [calendarPage.render()]
    elif pathname == "/cameras":
        return [webcamPage.render()]
    elif pathname == "/forecast":
        return [forecastPage.render()]
    elif pathname == "/aircraft":
        return [aircraftPage.render()]
    else:
        return [dcc.Location(pathname="/", id='redirect')]


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
)
def update_footer(n):
    return footerComponent.render()


@app.callback(
    Output("weather-page-container", "children"),
    Input("refresh-interval", "n_intervals"))
def refresh_weather(refresh):
    return weatherComponents.getAllComponents()


@app.callback(
    Output("winds-page-container", "children"),
    Input("refresh-interval", "n_intervals"),
)
def refresh_winds(refresh):
    return windsComponents.getAllComponents()


@app.callback(
    Output("webcam-page-container", "children"),
    Input("refresh-interval", "n_intervals"),
)
def refresh_winds(refresh):
    return webcamComponents.getAllComponents()


@app.callback(
    Output("drawer-simple", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    Input("drawer-demo-label", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(icn, lbl):
    return True


clientside_callback(
    """
    function(url) {
        if (url === '/') {
            document.title = 'Home | Skydive Utah App'
        } else if (url === '/calendar') {
            document.title = 'Calendar | Skydive Utah App'
        } else if (url === '/winds') {
            document.title = 'Winds Aloft | Skydive Utah App'
        } else if (url === '/cameras') {
            document.title = 'Live Cameras | Skydive Utah App'
        } else if (url === '/forecast') {
            document.title = 'Weather Forecast | Skydive Utah App'
        } else {
            document.title = 'Home | Skydive Utah App'
        }
    }
    """,
    Output('hidden-div-callbacks', 'children'),
    Input('url', 'pathname')
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
