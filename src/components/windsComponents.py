from plotly.graph_objs import Scatter
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
    table_data = [dict(Altitude=f'{altFt} Ft',
                       Direction=f"{data['direction'][str(altFt)]}°",
                       Speed=f"{data['speed'][str(altFt)]} Kts",
                       Temperature=f"{data['temp'][str(altFt)]}°C")
                  for altFt in data['altFt'] if altFt <= 25000]

    # Create the table
    table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in table_data[0]],
        data=table_data,
        style_table={'maxWidth': '80vw', 'border': 'thin lightgrey solid','overflow':'scroll'},
        style_header={
            'backgroundColor': 'rgba(47, 62, 70, 1)',
            'fontWeight': 'bold',
            'color': 'white'
        },
        style_cell={'textAlign': 'left',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'minWidth': '0px', 'maxWidth': '180px',
                    'whiteSpace': 'normal',
                    'backgroundColor': 'rgba(47, 62, 70, 0.5)',
                    'color': 'white'},
        style_data={'whiteSpace': 'normal'},
        css=[{
            'selector': '.dash-cell div.dash-cell-value',
            'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
        }],
    )

    wind_speed_trace = Scatter(x=data['altFt'],
                               y=[data['speed'][str(altFt)]
                                  for altFt in data['altFt']],
                               mode='lines',
                               name='Wind Speed (Kts)')

    temp_trace = Scatter(x=data['altFt'],
                         y=[data['temp'][str(altFt)]
                            for altFt in data['altFt']],
                         mode='lines',
                         name='Temperature (°C)')

    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'fontSize': '20px',
            'color': 'black',
            'borderRadius': '15px',
            'boxShadow': '0 0 1px 5px rgba(47,62,70,0.5)'
        },
        children=[
            html.H2('Winds Aloft',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),
            html.Div(children='''Windspeed and temperature at altitude.''',
                     style={
                         'textAlign': 'center', 'color': 'white'}),
            dcc.Graph(
                id='example-graph',
                style={'width': '80vw'},
                figure=dict(
                    data=[wind_speed_trace, temp_trace],
                    layout=dict(
                        template='plotly_dark',
                        plot_bgcolor='rgba(47, 62, 70, 0.5)',
                        paper_bgcolor='rgba(47, 62, 70, 1)',
                        font={'color': 'white'},
                        legend={'orientation': 'h', 'y': 1.1,
                                'x': 0.5, 'xanchor': 'center'},
                        xaxis_title='Altitude',
                        yaxis_title='Value'
                    )
                ),
                config=dict(displayModeBar=False),
            ),
            html.Div(table, style={'paddingTop':'10px'})
        ]
    )
