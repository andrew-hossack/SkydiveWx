import datetime

import dash_bootstrap_components as dbc
import pytz
from dash import Input, Output, dcc, html, Dash

from components.footer import footerComponent
from components.header import headerComponent
from components.weather import weatherComponents
from components.winds import windsComponents
from pages import calendarPage, weatherPage, windsAloftPage

app = Dash(
    title="Skydive Utah - Live Dashboard",
    external_stylesheets=[dbc.themes.MATERIA],
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


if __name__ == "__main__":
    print('TODO:')
    print('\t- Calendar iFrame src')
    print('\t- Loading spinner component that doesnt run on each callback update')
    # Improvement: if you pull the forecast at 2:50pm MDT, that's 20:50 UTC, so it used the forecast issued for 20Z. Ideally, you'd want to use 21Z at the point, which you can get by setting hourOffset=1
    # not sure if you want to bother with adding a condition on whether the current time is before or after :30
    # Improvement: Fix the weather direction plot to be continuous
    app.run_server(debug=True, port=8050)
