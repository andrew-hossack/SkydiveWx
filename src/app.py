import datetime

import dash
import dash_bootstrap_components as dbc
import pytz
from dash import Input, Output, dcc, html

from components import headerComponent, footerComponent
from pages import weatherPage, webcamPage, windsAloftPage, calendarPage

app = dash.Dash(
    title="Skydive Utah - Current Weather",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        headerComponent.render(),
        html.Div(id="page-content", style={
            "padding": "2rem 1rem",
        }),
        footerComponent.render()
    ]
)

server = app.server

########################
###### CALLBACKS #######
########################


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return weatherPage.render()
    elif pathname == "/winds":
        return windsAloftPage.render()
    elif pathname == "/webcam":
        return webcamPage.render()
    elif pathname == "/calendar":
        return calendarPage.render()
    else:
        return weatherPage.render()


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
    print('TODO:')
    print('\t- Refresh metar data regularily with callback')
    print('\t- Style homepage better')
    print('\t- Make winds aloft chart')
    print('\t- Host somewhere')
    print('\t- Set up ci/cd')
    app.run_server(debug=True, port=8050)
