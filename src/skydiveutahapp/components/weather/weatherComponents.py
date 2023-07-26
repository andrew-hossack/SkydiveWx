import pandas as pd
from dash import dcc, html
from components.calendar import calenderComponents
from utils import timeUtils, weatherUtils


def renderCurrentWeather() -> html.Div:
    metar = weatherUtils.get_metar()
    return html.Div(
        style={
            'padding': '20px',
            'margin': '20px',
            'fontSize': '20px',
            'color': 'white',
            'margin': 'auto',
        },
        children=[
            html.Div([
                html.H2('Current Conditions',
                        style={
                            'textAlign': 'center',
                            'fontSize': '26px',
                            'color': '#3498db',
                        }),
                renderWind(),
                html.Div(style={
                    'backgroundColor': 'rgba(47, 62, 70, 0)',
                    'paddingTop': '1px',
                    'paddingBottom': '1px',
                    'borderRadius': '5px',
                    'maxWidth': '550px',
                    'margin': 'auto',
                },
                    className='right-align',
                    children=[
                    html.Div(style={'marginTop': '15px', 'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Updated: ', style={
                                    'marginRight': '10px'}),
                        html.Span(timeUtils.time_diff(metar.time),
                                  id='time-since-last-update')
                    ]),
                    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Sky: ', style={'marginRight': '10px'}),
                        html.Span(str.capitalize(metar.sky_conditions()))
                    ]),
                    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Visibility: ', style={
                            'marginRight': '10px'}),
                        html.Span(str(metar.vis))
                    ]),
                    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Wind: ', style={'marginRight': '10px'}),
                        html.Span(str.capitalize(metar.wind("MPH")))
                    ]),
                    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Gust: ', style={'marginRight': '10px'}),
                        html.Span(
                            metar.wind_gust.string("MPH") if metar.wind_gust else 'No gusts, winds are steady!')
                    ]),
                    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'},
                             children=[
                        html.Strong('Temperature: ', style={
                            'marginRight': '10px'}),
                        html.Span(metar.temp.string('F'))
                    ]),
                ])
            ], style={'margin': 'auto'})
        ]
    )


def _generate_compass_component(direction, speed, rotation) -> html.Div:
    return html.Div(
        [
            html.Div([], className="west"),
            html.Div([], className="east"),
            html.Div(
                [
                    html.P(
                        [
                            direction,
                            html.Br(),
                            html.Span(f'{speed}')
                        ],
                        style={'marginTop': '20px'}
                    )
                ],
                className="direction"
            ),
            html.Div(
                [],
                className="arrow",
                style={
                    'transform': f'rotate({rotation}deg)',
                    '-webkit-transform': f'rotate({rotation}deg)',
                    '-moz-transform': f'rotate({rotation}deg)',
                    '-ms-transform': f'rotate({rotation}deg)',
                    '-o-transform': f'rotate({rotation}deg)'
                }
            )
        ],
        className="compass"
    )


def renderWind() -> html.Div:
    metar = weatherUtils.get_metar()
    # Access the wind direction and speed
    wind_dir = metar.wind_dir.value() if metar.wind_dir.value() else 0
    wind_speed = metar.wind_speed.string("MPH") if metar.wind_speed else 0

    # Convert the wind direction degrees to rotation in css
    css_degrees = (wind_dir + 180) % 360 if wind_speed != '0 mph' else 0

    return html.Div(
        children=[
            html.Div(
                f'Winds from {metar.wind_dir.compass()} ({wind_dir}°) at {wind_speed}',
                className='wind-direction-text',
            ),
            _generate_compass_component(
                metar.wind_dir.compass(), wind_speed, css_degrees),
        ],
        className='outer-div',
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'center',
            'justify-content': 'center',
            'height': '100%',
        }
    )


def renderWindTrends() -> html.Div:
    # List of metar objects
    historical_weather = weatherUtils.get_metar(hours=4)

    df_historical = pd.DataFrame([(timeUtils.convert_utc_to_mst(metar.time).strftime('%-I:%M%p'), int(metar.wind_speed.string("MPH").replace(" mph", "")) if metar.wind_speed else 0, int(metar.wind_gust.string("MPH").replace(" mph", "")) if metar.wind_gust else 0) for metar in historical_weather],
                                 columns=['time', 'windspeed_10m', 'windgusts_10m']).iloc[::-1]

    return html.Div(
        style={
            'fontSize': '20px',
            'color': 'white',
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
                style={'margin': 'auto', 'height': '60vh', 'maxHeight': '650px'},
                figure={
                    'data': [
                        {
                            'x': df_historical['time'],
                            'y': df_historical['windspeed_10m'],
                            'type': 'line',
                            'name': 'Wind speed (mph)',
                            'line': {'width': 4, 'shape': 'spline'}
                        },
                        {
                            'x': df_historical['time'],
                            'y': df_historical['windgusts_10m'],
                            'type': 'line',
                            'name': 'Wind gusts (mph)',
                            'line': {'width': 4, 'shape': 'spline'}
                        },
                    ],
                    'layout': {
                        'plot_bgcolor': 'rgba(47, 62, 70, 0)',
                        'paper_bgcolor': 'rgba(47, 62, 70, 0)',
                        'font': {
                            'color': 'white'
                        },
                        'xaxis': {
                            'gridcolor': 'rgba(255,255,255,0.1)',
                        },
                        'yaxis': {
                            'gridcolor': 'rgba(255,255,255,0.1)',
                            'tickformat': '~s',
                            'ticksuffix': ' mph',
                        },
                        'legend': {'orientation': 'h', 'y': 1.1, 'x': 0.5, 'xanchor': 'center'},
                        'autosize': True,
                        'dragmode': False,
                        'hovermode': 'x unified',
                        'hoverlabel': {
                            'font': {'color': 'black'}
                        }
                    }
                },
            )
        ]
    )


def renderCalendarCurrentDay() -> html.Div:
    return html.Div(
        style={
            'padding': '20px',
            'fontSize': '20px',
            'color': 'white',
            'maxHeight': '650px',
            'margin': 'auto'
        },
        children=html.Div([
            html.H2("Today's Calendar",
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),
            html.Div([
                calenderComponents.getTodaysEventsIFrame(),
            ], style={
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
            }),
        ], style={'maxWidth': '80vw',
                  'flex-direction': 'column',
                  'margin': '0 auto',
                  'maxWidth': '550px', })
    )


def renderWeatherOutlook() -> html.Div:
    # Fetch weather data
    forecast_num_hours = 4
    forecast_data = weatherUtils.get_forecast(hours=forecast_num_hours)

    # Calculate the maximum probability of rain
    max_rain_chance = max(
        [data.get('probabilityOfPrecipitation').get('value', 0) for data in forecast_data])
    rain_hours = [data for data in forecast_data[::-1] if data.get(
        'probabilityOfPrecipitation').get('value', 0) == max_rain_chance]
    rain_hours = timeUtils.convert_to_mst_from_ISO_8601(
        rain_hours[0]['endTime']) if rain_hours else None

    # Calculate wind speed changes
    wind_speeds = [int(data.get('windSpeed').split()[0])
                   for data in forecast_data if data.get('windSpeed')]
    min_wind_speed, max_wind_speed = min(
        wind_speeds), max(wind_speeds) if wind_speeds else (0, 0)

    wind_speed_info = ""
    if min_wind_speed == max_wind_speed:
        wind_speed_info = " The wind speed may be consistently about **{} mph**.".format(
            min_wind_speed)
    else:
        wind_speed_info = " The wind speed may change from **{} mph** to **{} mph**.".format(
            min_wind_speed, max_wind_speed)

    # Determine wind direction
    wind_directions = {data.get('windDirection')
                       for data in forecast_data if data.get('windDirection')}
    if len(wind_directions) > 1:
        wind_direction_info = " The wind direction may change and vary among **{}.**".format(
            ", ".join(wind_directions))
    else:
        wind_direction_info = " The wind direction may consistently be **{}**.".format(
            next(iter(wind_directions), "unknown"))

    # Generate weather forecast summary
    forecast_summary = ("In the next {} hours, there is a **{}%** chance of rain till {}.{}{}".format(forecast_num_hours,
                                                                                                      max_rain_chance,
                                                                                                      rain_hours if rain_hours else "unknown",
                                                                                                      wind_speed_info,
                                                                                                      wind_direction_info))
    return html.Div(
        style={
            'padding': '20px',
            'fontSize': '20px',
            'color': 'white',
            'maxHeight': '650px',
            'margin': 'auto',
            'marginBottom': '0',
        },
        children=html.Div([
            html.H2('Weather Outlook',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db'
                    }),
            dcc.Markdown([
                forecast_summary,
            ], style={
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
            }),
        ], style={'maxWidth': '80vw',
                  'flex-direction': 'column',
                  'margin': 'auto',
                  'maxWidth': '550px', })
    )


def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            renderCurrentWeather(),
            renderWeatherOutlook(),
            renderCalendarCurrentDay(),
            renderWindTrends(),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'boxShadow': '0 0 1px 5px rgba(47,62,70,0.5)',
            'width': '80vw',
            'maxWidth': '750px',
        }),
    ]
