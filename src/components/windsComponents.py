import json
from dash import html, dcc, dash_table
import requests

def _get_data():
    # Getting the data from the url
    url = 'https://markschulze.net/winds/winds.php?lat=40.61318686&lon=-112.3481226&hourOffset=0%3F&referrer=SkydiveUtah'
    response = requests.get(url)
    return json.loads(response.text)


def renderTable() -> html.Div:

    data = _get_data()

    # Prepare data for the table
    table_data = [dict(AltFt=altFt,
                       Direction=data['direction'][str(altFt)],
                       Speed=data['speed'][str(altFt)],
                       Temp=data['temp'][str(altFt)])
                  for altFt in data['altFt']]

    # Create the table
    table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in table_data[0]],
        data=table_data,
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
        style_data={'whiteSpace': 'normal'},
        css=[{
            'selector': '.dash-cell div.dash-cell-value',
            'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
        }],
    )

    return html.Div([
        dcc.Graph(
            figure=dict(data=[], layout=dict(template='plotly_dark')),
            config=dict(displayModeBar=False),
            style=dict(height='calc(100vh - 53px -44px)')
        ),
        table
    ], style={'width':'80vw'})
