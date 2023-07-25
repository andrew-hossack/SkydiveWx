import json

import requests
from dash import dash_table, dcc, html
from plotly.graph_objs import Scatter
from utils import timeUtils, weatherUtils


def _get_data():
    # Getting the data from the url
    url = 'https://markschulze.net/winds/winds.php?lat=40.61318686&lon=-112.3481226&hourOffset=0%3F&referrer=SkydiveUtah'
    response = requests.get(url)
    return json.loads(response.text)


def _render_table(data) -> dash_table.DataTable:
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
    return dash_table.DataTable(
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
                    'backgroundColor': 'rgba(47, 62, 70, 0)',
                    'color': 'white'},
        style_data={'whiteSpace': 'normal'},
        css=[{
            'selector': '.dash-cell div.dash-cell-value',
            'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
        }],
    )


def _resolve_wind_direction(data: dict, altitudes: list) -> list[list]:
    # This method probably sucks, I used chatgpt for help lol
    wrapped_altitudes = []
    wrapped_wind_dirs = []
    dir_data = [data['direction'][str(alt)] for alt in altitudes]

    temp_alts = [altitudes[0]]
    temp_dirs = [dir_data[0]]
    for i in range(1, len(dir_data)):
        if abs(dir_data[i] - dir_data[i-1]) > 180:
            wrapped_altitudes.append(temp_alts)
            wrapped_wind_dirs.append(temp_dirs)
            temp_alts = [altitudes[i]]
            temp_dirs = [dir_data[i]]
        else:
            temp_alts.append(altitudes[i])
            temp_dirs.append(dir_data[i])
    wrapped_altitudes.append(temp_alts)
    wrapped_wind_dirs.append(temp_dirs)

    return wrapped_altitudes, wrapped_wind_dirs


def renderWindsAloft() -> html.Div:
    winds_aloft_data = _get_data()
    metar = weatherUtils.get_metar()

    # # UNCOMMENT FOR "DISJOINTED" WIND DIRECTION TEST DATA
    # ##############
    # # Wrap right
    # wind_dir = [70, 80, 90, 100, 110, 120, 130, 140, 150, 200,
    #             250, 300, 350, 50, 60, 70, 80, 90, 95, 100, 100]

    # # Wrap left
    # # wind_dir = [150, 140, 140, 130, 110, 100, 100, 100, 50, 350,
    # #             300, 280, 250, 240, 180, 160, 140, 120, 110, 100, 100]

    # # Here we have a shortened list, let's just fit it with altitude <= 20000
    # new_directions = {altitude: direction
    #                   for (altitude, direction) in zip([key for key in data['direction'] if int(key) <= 20000], wind_dir)}

    # # Then we replace the corresponding parts in original data with new directions
    # data['direction'].update(new_directions)
    # ##############

    altitude_list = [
        altFt for altFt in winds_aloft_data['altFt'] if altFt <= 20000]

    wind_speed_trace = Scatter(y=[altFt for altFt in winds_aloft_data['altFt'] if altFt <= 20000],
                               x=[winds_aloft_data['speed'][str(altFt)]
                                  for altFt in winds_aloft_data['altFt'] if altFt <= 20000],
                               mode='lines',
                               name='Wind Speed (Kts)',
                               line=dict(color='coral'))

    altitudes_by_trace, winds_by_trace = _resolve_wind_direction(
        winds_aloft_data, altitude_list)
    wind_dir_traces = [Scatter(y=altitudes_by_trace[i],
                               x=winds_by_trace[i],
                               mode='lines',
                               xaxis='x2' if i % 2 == 0 else 'x3',
                               name='Wind Direction (°)',
                               showlegend=True if i == 0 else False,
                               line=dict(shape='linear'),
                               marker=dict(color='mintcream'))
                       for i in range(len(altitudes_by_trace))]

    tickrange = [min(int(value) for value in winds_aloft_data['direction'].values()), max(
        int(value) for value in winds_aloft_data['direction'].values())]
    tickvals = [i for i in range(min(tickrange), max(tickrange) + 1, 30)]
    ticktext = [f"{i%360}°" for i in tickvals]

    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'fontSize': '20px',
            'color': 'black',
        },
        children=[
            html.H2(f'Winds Aloft - Updated at {timeUtils.zulu_to_mst_string(winds_aloft_data["validtime"])}',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),
            html.Div(style={
                'backgroundColor': 'rgba(47, 62, 70, 0)',
                'paddingLeft': '10px',
                'paddingRight': '10px',
                'paddingTop': '1px',
                'borderRadius': '5px',
                'maxWidth': '400px',
                'margin': 'auto',
                'color': 'white',
                'font-size': '15px',
                'marginBottom': '-20px',
                'marginTop': '-10px',
            },
                children=[
                html.Div(style={'marginTop': '15px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Altimeter: ', style={'marginRight': '10px'}),
                    html.Span(str.capitalize(metar.press.string("in")))
                ]),
                html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Density Altitude: ', style={
                                'marginRight': '10px'}),
                    html.Span(
                        f'{weatherUtils._calculate_density_altitude(metar.press.value("in"), metar.temp.value("C"))} ft')
                ]),
                html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Altitude Info Updated At: ', style={
                                'marginRight': '10px', 'text-align': 'left'}),
                    html.Span(timeUtils.time_diff(metar.time),
                              id='time-since-last-update', style={'text-align': 'right',})
                ]),
            ]),
            dcc.Graph(
                style={'width': '100%',
                       'display': 'inline-block', 'height': '600px'},
                figure=dict(
                    data=[wind_speed_trace, *wind_dir_traces],
                    layout=dict(
                        xaxis=dict(title='Wind Speed (Kts)',
                                   showgrid=True,
                                   gridcolor='rgba(255, 255, 255, 0.2)',
                                   color='coral',
                                   showline=False,
                                   linecolor='coral',
                                   fixedrange=True),
                        xaxis2=dict(title='Wind Direction (°)',
                                    overlaying='x',
                                    side='top',
                                    showgrid=False,
                                    gridcolor='rgba(255, 255, 255, 0.2)',
                                    range=tickrange,
                                    tickvals=tickvals,
                                    ticktext=ticktext,
                                    color='mintcream',
                                    showline=False,
                                    linecolor='mintcream',
                                    fixedrange=True),
                        xaxis3=dict(overlaying='x', side='bottom',
                                    showgrid=False,
                                    range=tickrange,
                                    tickvals=tickvals,
                                    ticktext=ticktext,
                                    color='mintcream',
                                    showline=False,
                                    showticklabels=False,
                                    fixedrange=True),
                        yaxis=dict(title='Altitude (ft)',
                                   showgrid=True,
                                   gridcolor='rgba(255, 255, 255, 0.2)',
                                   fixedrange=True),
                        hovermode="y unified",
                        template='plotly_dark',
                        plot_bgcolor='rgba(47, 62, 70, 0)',
                        paper_bgcolor='rgba(47, 62, 70, 0)',
                        font={'color': 'white'},
                        autosize=True,
                        showlegend=False
                    )
                ),
                config=dict(displayModeBar=False),
            ),
            html.Div(_render_table(winds_aloft_data),
                     style={'paddingTop': '20px', 'marginTop':'-20px'}),
            dcc.Markdown('''
            _*Credit to Mark Schulze ([markschulze.net/winds](http://markschulze.net/winds)) for providing API access to winds aloft data._
            ''', style={'color': 'white', 'font-size': '12px', 'margin-top': '10px'})
        ]
    )


def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            renderWindsAloft()
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'boxShadow': '0 0 1px 5px rgba(47,62,70,0.5)',
            'width': '80vw',
            'maxWidth': '750px',
        }),
    ]
