import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash import html, dcc
from metar import Metar
from datetime import datetime, timedelta
from pytz import timezone
from utils import weatherUtils
from datetime import datetime


def _format_datetime_in_mst(dt: datetime) -> str:
    # Convert to datetime object and set it to UTC
    utc_time = timezone('UTC').localize(dt)

    # Convert to the appropriate Mountain Time (could be MST or MDT)
    mt = timezone('America/Denver')
    mt_time = utc_time.astimezone(mt)

    # Output in the format: "Monday, January 14th 2023 at 02:55PM"
    return f"{mt_time.strftime('%A, %B %-d %Y at %I:%M %p').replace('AM', 'am').replace('PM', 'pm')}"


def renderCurrentWeather(metar: Metar.Metar) -> html.Div:
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
                     html.Span(_format_datetime_in_mst(metar.time))
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
                         metar.wind_gust if metar.wind_gust else 'No gusts, winds are steady!')
                     ]),
            html.Div(style={'marginBottom': '8px', 'display': 'flex', 'justifyContent': 'space-between'},
                     children=[
                     html.Strong('Temperature: ', style={
                                 'marginRight': '10px'}),
                     html.Span(metar.temp.string('F'))
                     ]),
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
    weather_forecasts = weatherUtils.get_weather_forecast()[:12]

    df = pd.DataFrame(weather_forecasts)

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
            html.H2('Weather Forecasts',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),

            html.Div(children='''Weather forecasts for the next 12 hours.''',
                     style={
                         'textAlign': 'center', 'color': 'white'}),

            dcc.Graph(
                id='example-graph',
                style={'width': '80vw'},
                figure={
                    'data': [
                        {'x': df['time'], 'y': df['temperature_2m'],
                         'type': 'bar', 'name': 'Temperature (°F)'},
                        {'x': df['time'], 'y': df['windspeed_10m'],
                         'type': 'bar', 'name': 'Wind speed (mph)'},
                        {'x': df['time'], 'y': df['rain'],
                         'type': 'line', 'name': 'Rain'},
                        {'x': [None], 'y': [None],
                         'mode': 'markers', 'marker': {'color': 'red'},
                         'showlegend': True, 'name': '15 mph'},
                    ],
                    'layout': {
                        'plot_bgcolor': 'rgba(47, 62, 70, 0.5)',
                        'paper_bgcolor': 'rgba(47, 62, 70, 1)',
                        'font': {
                            'color': 'white'
                        },
                        'shapes': [
                            {
                                'type': 'line',
                                'x0': df['time'].min(),
                                'y0': 15,
                                'x1': df['time'].max(),
                                'y1': 15,
                                'line': {
                                    'color': 'red',
                                    'width': 2,
                                },
                            },
                        ],
                        'legend': {'orientation': 'h', 'y': 1.1, 'x': 0.5, 'xanchor': 'center'},
                    }
                }
            )
        ]
    )
