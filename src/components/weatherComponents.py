import pandas as pd
from dash import dcc, html
from metar import Metar

from utils import timeUtils, weatherUtils


def renderCurrentWeather() -> html.Div:
    metar = weatherUtils.get_metar()
    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'fontSize': '20px',
            'color': 'white',
            'borderRadius': '15px',
            'boxShadow': '0 0 1px 5px rgba(47,62,70,0.5)'
        },
        children=[
            html.Div([

                html.H2('Current Weather',
                        style={
                            'textAlign': 'center',
                            'fontSize': '26px',
                            'color': '#3498db'
                        }),
                renderWind(metar),
                html.Div(style={'marginBottom': '8px', 'marginTop': '15px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Updated: ', style={'marginRight': '10px'}),
                    html.Span(timeUtils.time_diff(metar.time), id='time-since-last-update')
                ]),
                html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Sky: ', style={'marginRight': '10px'}),
                    html.Span(str.capitalize(metar.sky_conditions()))
                ]),
                html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Visibility: ', style={
                        'marginRight': '10px'}),
                    html.Span(str(metar.vis))
                ]),
                html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Wind: ', style={'marginRight': '10px'}),
                    html.Span(str.capitalize(metar.wind("MPH")))
                ]),
                html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Gust: ', style={'marginRight': '10px'}),
                    html.Span(
                        metar.wind_gust.string("MPH") if metar.wind_gust else 'No gusts, winds are steady!')
                ]),
                html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                         children=[
                    html.Strong('Temperature: ', style={
                        'marginRight': '10px'}),
                    html.Span(metar.temp.string('F'))
                ]),
            ], style={'minWidth': '80vw'})
        ]
    )


def renderWind(metar: Metar.Metar) -> html.Div:
    # Access the wind direction and speed
    wind_dir = metar.wind_dir.value() if metar.wind_dir.value() else 0
    wind_speed = metar.wind_speed.string("MPH") if metar.wind_speed else 0

    # Convert the wind direction degrees to rotation in css
    css_degrees = (wind_dir + 180) % 360 if wind_speed != '0 mph' else 0

    return html.Div(
        children=[
            html.Div(
                f'Winds from {metar.wind_dir.compass()} ({wind_dir}°) at {wind_speed}',
                className='wind-direction-text'
            ),
            html.Div(
                # Arrow unicode for windy condition, cloud unicode for calm condition
                '⬆' if wind_speed != '0 mph' else '💤',
                className='wind-arrow',
                style={
                    'transform': 'rotate({}deg)'.format(css_degrees),
                    '-webkit-transform': 'rotate({}deg)'.format(css_degrees),
                    '-moz-transform': 'rotate({}deg)'.format(css_degrees),
                    '-ms-transform': 'rotate({}deg)'.format(css_degrees),
                    '-o-transform': 'rotate({}deg)'.format(css_degrees)
                } if wind_speed != '0 mph' else {}  # if condition also added for the css style
            )
        ]
    )


def renderWindsAloft() -> html.Div:
    return html.Div("In Progress", style={'color': 'white'})


def renderWeatherForecast() -> html.Div:
    # List of metar objects
    historical_weather = weatherUtils.get_metar(hours=4)

    df_historical = pd.DataFrame([(timeUtils.convert_utc_to_mst(metar.time).strftime('%-I:%M%p'), int(metar.wind_speed.string("MPH").replace(" mph", "")) if metar.wind_speed else 0, int(metar.wind_gust.string("MPH").replace(" mph", "")) if metar.wind_gust else 0) for metar in historical_weather],
                             columns=['time', 'windspeed_10m', 'windgusts_10m']).iloc[::-1]

    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'fontSize': '20px',
            'color': 'white',
            'borderRadius': '15px',
            'boxShadow': '0 0 1px 5px rgba(47,62,70,0.5)'
        },
        children=[
            html.H2('Wind Trends',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),

            html.Div(children='Wind and gust trends from the past 4 hours',
                     style={
                         'textAlign': 'center', 'color': 'white'}),

            dcc.Graph(
                id='example-graph',
                style={'width': '80vw', 'height':'60vh'},
                figure={
                    'data': [
                        {'x': df_historical['time'], 'y': df_historical['windspeed_10m'],
                         'type': 'line', 'name': 'Wind speed (mph)'},
                        {'x': df_historical['time'], 'y': df_historical['windgusts_10m'],
                         'type': 'line', 'name': 'Wind gusts (mph)'},
                    ],
                    'layout': {
                        'plot_bgcolor': 'rgba(47, 62, 70, 0.5)',
                        'paper_bgcolor': 'rgba(47, 62, 70, 1)',
                        'font': {
                            'color': 'white'
                        },
                        'legend': {'orientation': 'h', 'y': 1.1, 'x': 0.5, 'xanchor': 'center'},
                        'autosize': True,
                    }
                }
            )
        ]
    )