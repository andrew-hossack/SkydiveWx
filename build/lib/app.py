'''
# This app creates a simple sidebar layout using inline style arguments and the
# dbc.Nav component.
# dcc.Location is used to track the current location, and a callback uses the
# current location to render the appropriate page content. The active prop of
# each NavLink is set automatically according to the current pathname. To use
# this feature you must install dash-bootstrap-components >= 0.11.0.
# For more details on building multi-page Dash applications, check out the Dash
# documentation: https://dash.plot.ly/urls
# Source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
# @ Create Time: 2023-07-17 20:10:07.921404
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
'''
import datetime

import dash
import dash_bootstrap_components as dbc
import pytz
from dash import Input, Output, dcc, html

from components import headerComponent, footerComponent
from pages import homePage, webcamPage, windsAloftPage

app = dash.Dash(
    title="SkydiveUtahApp",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# the styles for the main content position it to the right of the sidebar and
# add some padding.
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

########################
###### CALLBACKS #######
########################


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return homePage.render()
    elif pathname == "/winds":
        return windsAloftPage.render()
    elif pathname == "/webcam":
        return webcamPage.render()
    else:
        return homePage.render()


@app.callback(
    Output("live-clock", "children"),
    Input("interval", "n_intervals")
)
def update_time(n):
    dt_utc = datetime.datetime.now()
    # Change from MST to America/Denver
    dt_mst = dt_utc.astimezone(pytz.timezone("America/Denver"))
    return dt_mst.strftime("%a %m/%d %I:%M:%S %p")


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
