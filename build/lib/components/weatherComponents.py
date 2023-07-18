from dash import html
from ..utils.metar import Metar
from datetime import datetime
from pytz import timezone


def _format_datetime_in_mst(dt: datetime) -> str:
    # Convert to datetime object and set it to UTC
    utc_time = timezone('UTC').localize(dt)

    # Convert to the appropriate Mountain Time (could be MST or MDT)
    mt = timezone('America/Denver')
    mt_time = utc_time.astimezone(mt)

    # Output in the format: "Monday, January 14th 2023 at 02:55PM"
    return mt_time.strftime("%A, %B %-d %Y at %I:%M %p").replace('AM', 'am').replace('PM', 'pm')


def renderWeather(metar: Metar.Metar) -> html.Div:
    return html.Div(
        style={
            'border': 'thin lightgrey solid',
            'border-radius': '5px',
            'padding': '20px',
            'margin': '20px',
            'maxWidth': '500px',
            'backgroundColor':'white'
        },
        children=[
            html.H2('Weather Report', style={'textAlign': 'center'}),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Time: '),
                     html.Span(_format_datetime_in_mst(metar.time))
                     ]),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Sky: '),
                     html.Span(str.capitalize(metar.sky_conditions()))
                     ]),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Visibility: '),
                     html.Span(str(metar.vis))
                     ]),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Wind: '),
                     html.Span(metar.wind())
                     ]),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Gust: '),
                     html.Span(metar.wind_gust if metar.wind_gust else 'No gusts, winds are steady!')
                     ]),
            html.Div(style={'marginBottom': '8px'},
                     children=[
                     html.Strong('Temperature: '),
                     html.Span(str(metar.temp))
                     ]),
        ]
    )


def renderWind(metar: Metar.Metar) -> html.Div:
    # Access the wind direction and speed
    wind_dir = metar.wind_dir.value() if metar.wind_dir.value() else 0
    wind_speed = metar.wind_speed.string("KT") if metar.wind_speed else 0

    # Convert the wind direction degrees to rotation in css
    css_degrees = (wind_dir + 180) % 360 if wind_speed != '0 knots' else 0

    return html.Div(
        children=[
            html.Div(
                'Winds from {}° at {}'.format(wind_dir, wind_speed),
                className='wind-direction-text'
            ),
            html.Div(
                # Arrow unicode for windy condition, cloud unicode for calm condition
                '⬆' if wind_speed != '0 knots' else '☁',
                className='wind-arrow',
                style={
                    'transform': 'rotate({}deg)'.format(css_degrees),
                    '-webkit-transform': 'rotate({}deg)'.format(css_degrees),
                    '-moz-transform': 'rotate({}deg)'.format(css_degrees),
                    '-ms-transform': 'rotate({}deg)'.format(css_degrees),
                    '-o-transform': 'rotate({}deg)'.format(css_degrees)
                } if wind_speed != '0 knots' else {}  # if condition also added for the css style
            )
        ]
    )


def renderWindsAloft() -> html.Div:
    return html.Div()