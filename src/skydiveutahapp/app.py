import datetime
import os
import dash_bootstrap_components as dbc
import pytz
from components.footer import footerComponent
from components.header import headerComponent
from components.weather import weatherComponents
from components.webcam import webcamComponents
from components.winds import windsComponents
from dash import Dash, Input, Output, dcc, html
from pages import calendarPage, weatherPage, webcamPage, windsAloftPage, forecastPage, aircraftPage

app = Dash(
    title="Skydive Utah Dashboard",
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
        <meta property="og:title" content="Skydive Utah Dashboard"">
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
        return [weatherPage.render()]
    elif pathname == "/winds":
        return [windsAloftPage.render()]
    elif pathname == "/calendar":
        return [calendarPage.render()]
    elif pathname == "/webcam":
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


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
