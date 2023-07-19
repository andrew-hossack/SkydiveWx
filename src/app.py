import datetime

import dash
import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
import pytz
from dash import Input, Output, dcc, html, State

from components import footerComponent, headerComponent
from pages import calendarPage, weatherPage, webcamPage, windsAloftPage
from utils import timeUtils, weatherUtils

app = dash.Dash(
    title="Skydive Utah - Live Dashboard",
    external_stylesheets=[dbc.themes.MATERIA],
    name=__name__,
    update_title=None,
)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        # Interval to check if metar is older than X minutes; every minute
        dcc.Interval(id='refresh-interval', interval=1000*60, n_intervals=0),
        headerComponent.render(),
        html.Div(
            [
                dls.Grid(id="page-content",
                         color="#435278",
                         speed_multiplier=2,
                         ),
            ],
            style={
                "padding": "2rem 1rem",
            },
        ),
        footerComponent.render()
    ]
)

server = app.server

########################
###### CALLBACKS #######
########################

@app.callback(
    Output("url", "pathname"),
    [Input("refresh-interval", "n_intervals")],
    [State('url','pathname')])
def refresh_page(refresh, currentPathname):
    metar = weatherUtils.get_metar()
    if int(timeUtils.time_diff(metar.time).replace(' minutes ago','')) > 15:
        # Force a page refresh every 15 minutes
        return currentPathname
    else:
        raise dash.exceptions.PreventUpdate


@app.callback(
    [
        Output("page-content", "children"),
        Output("footer-metar-data", "children"),
    ],
    [
        Input("url", "pathname"),
    ])
def render_page_content(pathname):
    currentMetar = weatherUtils.get_metar()
    if pathname == "/":
        return [weatherPage.render(), f'{currentMetar.code} ']
    elif pathname == "/winds":
        return [windsAloftPage.render(), f'{currentMetar.code} ']
    elif pathname == "/webcam":
        return [webcamPage.render(), f'{currentMetar.code} ']
    elif pathname == "/calendar":
        return [calendarPage.render(), f'{currentMetar.code} ']
    else:
        return [weatherPage.render(), f'{currentMetar.code} ']


@app.callback(
    Output("live-clock", "children"),
    Input("header-interval", "n_intervals")
)
def update_time(n):
    dt_utc = datetime.datetime.now()
    # Change from MST to America/Denver
    dt_mst = dt_utc.astimezone(pytz.timezone("America/Denver"))
    return f'{dt_mst.strftime("%a %m/%d %I:%M:%S %p")} MST'


if __name__ == "__main__":
    # print('TODO:')
    # print('\t- Calendar iFrame src')
    # Improvement: do some smart shit with the client and only query the api's when we need to, not based on client refresh
    # Improvement: if you pull the forecast at 2:50pm MDT, that's 20:50 UTC, so it used the forecast issued for 20Z. Ideally, you'd want to use 21Z at the point, which you can get by setting hourOffset=1
    # not sure if you want to bother with adding a condition on whether the current time is before or after :30
    app.run_server(debug=False, port=8050)
