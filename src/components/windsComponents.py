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
                  for altFt in data['altFt'] if altFt <= 20000]

    # Convert temperature to Fahrenheit
    for row in table_data:
        tempC = float(row['Temperature'][:-2])
        tempF = tempC * (9/5) + 32
        row['Temperature'] = f"{int(tempF)}°F"

    # Create the table
    table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in table_data[0]],
        data=table_data,
        style_table={'maxWidth': '80vw',
                     'border': 'thin lightgrey solid', 'overflow': 'scroll'},
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

    wind_speed_trace = Scatter(y=[altFt for altFt in data['altFt'] if altFt <= 20000],
                               x=[data['speed'][str(altFt)]
                                  for altFt in data['altFt'] if altFt <= 20000],
                               mode='lines',
                               name='Wind Speed (Kts)')

    temp_trace = Scatter(y=[altFt for altFt in data['altFt'] if altFt <= 20000],
                         x=[(data['temp'][str(altFt)]*(9/5)+32)
                            for altFt in data['altFt'] if altFt <= 20000],
                         mode='lines',
                         name='Temperature (°F)')

    wind_dir_trace = Scatter(y=[altFt for altFt in data['altFt'] if altFt <= 20000],
                             x=[data['direction'][str(altFt)]
                                for altFt in data['altFt'] if altFt <= 20000],
                             mode='markers',
                             name='Wind Direction (°)')

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
            html.Div(children='''Windspeed, Temperature and Direction at altitude.''',
                     style={
                         'textAlign': 'center', 'color': 'white'}),
            dcc.Graph(
                id='example-graph',
                style={'width': '80vw'},
                figure=dict(
                    data=[wind_speed_trace, temp_trace, wind_dir_trace],
                    layout=dict(
                        template='plotly_dark',
                        plot_bgcolor='rgba(47, 62, 70, 0.5)',
                        paper_bgcolor='rgba(47, 62, 70, 1)',
                        font={'color': 'white'},
                        legend={'orientation': 'h', 'y': 1.1,
                                'x': 0.5, 'xanchor': 'center'},
                        yaxis_title='Altitude',
                        xaxis_title='Value'
                    )
                ),
                config=dict(displayModeBar=False),
            ),
            html.Div(table, style={'paddingTop': '10px'})
        ]
    )
