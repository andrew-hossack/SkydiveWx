import datetime

import dash
import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
import pytz
from dash import Input, Output, dcc, html

from components import footerComponent, headerComponent
from pages import calendarPage, weatherPage, webcamPage, windsAloftPage
from utils import weatherUtils

app = dash.Dash(
    title="Skydive Utah - Live Conditions",
    external_stylesheets=[dbc.themes.MATERIA],
    name=__name__,
    update_title=None,
)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        # 10 minute refresh interval
        dcc.Interval(id='refresh-interval',
                     interval=10*60*1000, n_intervals=0),
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
    [
        Output("page-content", "children"),
        Output("footer-metar-data", "children"),
    ],
    [
        Input("url", "pathname"),
        Input("refresh-interval", "n_intervals"),
    ])
def render_page_content(pathname, refresh):
    # Refresh the footer and page every 10 minutes
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
    # print('\t- Set up ci/cd')
    # print('\t- Add historical metar for home winds')
    # print('\t- Add error handler modal to show prod errors')
    # Improvement: if you pull the forecast at 2:50pm MDT, that's 20:50 UTC, so it used the forecast issued for 20Z. Ideally, you'd want to use 21Z at the point, which you can get by setting hourOffset=1
    # not sure if you want to bother with adding a condition on whether the current time is before or after :30
    app.run_server(debug=False, port=8050)
