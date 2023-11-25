import pandas as pd
from dash import dcc, html
from components.calendar import calenderComponents
from components.home.weatherRadarComponents import radarComponent
from components.plane.trackerComponents import planeTrackIframe
from components.manifest.manifestComponents import getScreenshotImageContainer
from utils.jumpability.jumpabilityService import getJumpability, describeJumpability
from utils.dropzones.dropzoneUtils import DropzoneType
from utils import timeUtils, weatherUtils
import dash_mantine_components as dmc
from utils.metar import Metar
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash_iconify import DashIconify


def renderCurrentWeather(
    dropZone: DropzoneType, metar: Metar, forecastData: list
) -> html.Div:
    try:
        shortForecast = [
            data.get("shortForecast")
            for data in forecastData
            if data.get("shortForecast")
        ][0]
    except Exception:
        shortForecast = None
    return html.Div(
        style={
            "padding": "20px",
            "margin": "20px",
            "fontSize": "20px",
            "color": "white",
            "margin": "auto",
        },
        children=[
            html.Div(
                [
                    html.A(
                        "Current Conditions",
                        href=f"/winds?id={dropZone.id}",
                        style={
                            "textAlign": "center",
                            "fontSize": "26px",
                            "color": "#3498db",
                            "display": "block",
                            "margin-top": "0",
                            "margin-bottom": "0.5rem",
                            "font-weight": "500",
                            "line-height": "1.2",
                        },
                    ),
                    _renderCompass(dropZone),
                    html.Div(
                        style={
                            "backgroundColor": "rgba(47, 62, 70, 0)",
                            "paddingTop": "1px",
                            "paddingBottom": "1px",
                            "borderRadius": "5px",
                            "maxWidth": "550px",
                            "margin": "auto",
                        },
                        className="right-align",
                        children=[
                            html.Div(
                                style={
                                    "marginTop": "15px",
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Updated: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(
                                        timeUtils.time_diff(metar.time),
                                        id="time-since-last-update",
                                    ),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong("Sky: ", style={"marginRight": "10px"}),
                                    html.Span(str.capitalize(metar.sky_conditions())),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Visibility: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(str(metar.vis)),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Wind: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(str.capitalize(metar.wind("MPH"))),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Gust: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(
                                        metar.wind_gust.string("MPH")
                                        if metar.wind_gust
                                        else "No gusts, winds are steady!"
                                    ),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Temperature: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(metar.temp.string("F")),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "space-between",
                                },
                                children=[
                                    html.Strong(
                                        "Forecast: ", style={"marginRight": "10px"}
                                    ),
                                    html.Span(shortForecast),
                                ],
                            )
                            if shortForecast
                            else None,
                        ],
                    ),
                ],
                style={"margin": "auto"},
            )
        ],
    )


def _generate_compass_component(direction, speed, rotation) -> html.Div:
    # If direction and rotation = -1 then don't show arrow
    showDisplay = True
    if rotation < 0:
        showDisplay = False
    return html.Div(
        [
            html.Div([], className="west"),
            html.Div([], className="east"),
            html.Div(
                [
                    html.P(
                        [direction, html.Br(), html.Span(f"{speed}")],
                        style={"marginTop": "20px"},
                    )
                ],
                className="direction",
            ),
            html.Div(
                [],
                className="arrow",
                style={
                    "transform": f"rotate({rotation}deg)",
                    "-webkit-transform": f"rotate({rotation}deg)",
                    "-moz-transform": f"rotate({rotation}deg)",
                    "-ms-transform": f"rotate({rotation}deg)",
                    "-o-transform": f"rotate({rotation}deg)",
                    "display": "none" if not showDisplay else "",
                },
            ),
        ],
        className="compass",
    )


def _renderCompass(dropZone: DropzoneType) -> html.Div:
    metar = weatherUtils.get_metar(dropZone.airportIdentifier)
    if not metar:
        return None
    # Access the wind direction and speed
    wind_speed = metar.wind_speed.string("MPH") if metar.wind_speed else 0
    if "variable" in metar.wind("MPH"):
        wind_dir_str = "variable"
        css_degrees = -1
        direction = -1
    else:
        wind_dir = metar.wind_dir.value() if metar.wind_dir.value() else 0
        css_degrees = (wind_dir + 180) % 360 if wind_speed != "0 mph" else -1
        wind_dir_str = f"{metar.wind_dir.compass()} ({wind_dir}°)"
        direction = metar.wind_dir.compass()

    windSpeedString = (
        f"Winds from {wind_dir_str} at {wind_speed}"
        if str(wind_speed) != "0 mph"
        else f"No Wind Reported"
    )
    # If css_degrees = -1 then handle below
    return html.Div(
        children=[
            html.Div(
                windSpeedString,
                className="wind-direction-text",
            ),
            _generate_compass_component(direction, wind_speed, css_degrees),
        ],
        className="outer-div",
        style={
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "justify-content": "center",
            "height": "100%",
        },
    )


def renderWindTrends(dropZone: DropzoneType, historicalMetar: any) -> html.Div:
    if not historicalMetar:
        return None
    # List of metar objects
    df_historical = pd.DataFrame(
        [
            (
                timeUtils.convert_utc_to_mst(metar.time).strftime("%-I:%M%p"),
                int(metar.wind_speed.string("MPH").replace(" mph", ""))
                if metar.wind_speed
                else 0,
                int(metar.wind_gust.string("MPH").replace(" mph", ""))
                if metar.wind_gust
                else 0,
            )
            for metar in historicalMetar
        ],
        columns=["time", "windspeed_10m", "windgusts_10m"],
    ).iloc[::-1]

    return html.Div(
        style={
            "fontSize": "20px",
            "color": "white",
            "padding": "20px",
        },
        children=[
            html.A(
                "Wind Trends",
                href=f"/winds?id={dropZone.id}",
                style={
                    "textAlign": "center",
                    "fontSize": "26px",
                    "color": "#3498db",
                    "display": "block",
                    "margin-top": "0",
                    "margin-bottom": "0.5rem",
                    "font-weight": "500",
                    "line-height": "1.2",
                },
            ),
            html.Div(
                children="Wind and gust trends from the past 4 hours",
                style={
                    "textAlign": "center",
                    "color": "white",
                    "maxWidth": "550px",
                    "margin": "auto",
                    "paddingLeft": "20px",
                    "paddingRight": "20px",
                },
            ),
            dcc.Graph(
                style={
                    "height": "60vh",
                },
                config={
                    "displayModeBar": False,
                },
                figure={
                    "data": [
                        {
                            "x": df_historical["time"],
                            "y": df_historical["windspeed_10m"],
                            "type": "line",
                            "hovertemplate": "Wind speed: %{y} mph<extra></extra>",
                            "line": {"width": 3, "shape": "spline"},
                            "name": "Wind Speed",
                        },
                        {
                            "x": df_historical["time"],
                            "y": df_historical["windgusts_10m"],
                            "type": "line",
                            "hovertemplate": "Wind gusts: %{y} mph<extra></extra>",
                            "line": {"width": 3, "shape": "spline"},
                            "name": "Wind Gusts",
                        },
                    ],
                    "layout": {
                        "margin": {"l": 55, "r": 25, "t": 30, "b": 65},
                        "plot_bgcolor": "rgba(47, 62, 70, 0)",
                        "paper_bgcolor": "rgba(47, 62, 70, 0)",
                        "font": {"color": "white"},
                        "xaxis": {
                            "gridcolor": "rgba(255,255,255,0.1)",
                        },
                        "yaxis": {
                            "gridcolor": "rgba(255,255,255,0.1)",
                            "tickformat": "~s",
                        },
                        "legend": {
                            "orientation": "h",
                            "y": 1.1,
                            "x": 0.5,
                            "xanchor": "center",
                        },
                        "autosize": True,
                        "dragmode": False,
                        "hovermode": "x unified",
                        "hoverlabel": {"font": {"color": "black"}},
                    },
                },
            ),
        ],
    )


def renderWeatherOutlook(
    dropZone: DropzoneType, forecastData: list, forecastNumHours: int
) -> html.Div:
    # Calculate the maximum probability of rain
    max_rain_chance = max(
        [
            data.get("probabilityOfPrecipitation").get("value", 0)
            for data in forecastData
        ]
    )
    rain_hours = [
        data
        for data in forecastData[::-1]
        if data.get("probabilityOfPrecipitation").get("value", 0) == max_rain_chance
    ]
    rain_hours = (
        timeUtils.convert_to_mst_from_ISO_8601(rain_hours[0]["endTime"])
        if rain_hours
        else None
    )

    # Calculate wind speed changes
    wind_speeds = [
        int(data.get("windSpeed").split()[0])
        for data in forecastData
        if data.get("windSpeed")
    ]
    min_wind_speed, max_wind_speed = min(wind_speeds), max(
        wind_speeds
    ) if wind_speeds else (0, 0)

    wind_speed_info = ""
    if min_wind_speed == max_wind_speed:
        wind_speed_info = (
            " The wind speed may be consistently about **{} mph**.".format(
                min_wind_speed
            )
        )
    else:
        wind_speed_info = (
            " The wind speed may change from **{} mph** to **{} mph**.".format(
                min_wind_speed, max_wind_speed
            )
        )

    # Determine wind direction
    wind_directions = {
        data.get("windDirection") for data in forecastData if data.get("windDirection")
    }
    if len(wind_directions) > 1:
        wind_direction_info = (
            " The wind direction may change and vary among **{}.**".format(
                ", ".join(wind_directions)
            )
        )
    else:
        wind_direction_info = " The wind direction may consistently be **{}**.".format(
            next(iter(wind_directions), "unknown")
        )

    # Generate weather forecast summary
    forecast_summary = "In the next {} hours, there is a **{}%** chance of precipitation till {}.{}{}".format(
        forecastNumHours,
        max_rain_chance,
        rain_hours if rain_hours else "unknown",
        wind_speed_info,
        wind_direction_info,
    )
    return html.Div(
        style={
            "padding": "20px",
            "fontSize": "20px",
            "color": "white",
            "margin": "auto",
            "marginBottom": "0",
        },
        children=html.Div(
            [
                html.A(
                    "Weather Outlook",
                    href=f"/forecast?id={dropZone.id}",
                    style={
                        "textAlign": "center",
                        "fontSize": "26px",
                        "color": "#3498db",
                        "display": "block",
                        "margin-top": "0",
                        "margin-bottom": "0.5rem",
                        "font-weight": "500",
                        "line-height": "1.2",
                    },
                ),
                dcc.Markdown(
                    [
                        forecast_summary,
                    ],
                    style={
                        "flex-direction": "column",
                        "align-items": "center",
                        "justify-content": "center",
                        "padding-bottom": "20px",
                    },
                    className="nomargin-p",
                ),
                html.Div(
                    radarComponent(dropZone, height="500px"), style={"height": "500px"}
                ),
            ],
            style={
                "maxWidth": "80vw",
                "flex-direction": "column",
                "margin": "auto",
                "maxWidth": "550px",
            },
        ),
    )


def renderJumpability(
    dropZone: DropzoneType, metar: Metar.Metar, forecastData: list
) -> html.Div:
    jump_score_results = getJumpability(metar, forecastData[0])
    return html.Div(
        style={
            "padding": "20px",
            "fontSize": "20px",
            "color": "white",
            "margin": "auto",
            "marginBottom": "0",
        },
        children=html.Div(
            [
                dmc.Modal(
                    title="About Jump Score",
                    id="jump-score-help-modal",
                    overflow="inside",
                    centered=True,
                    closeOnEscape=True,
                    zIndex=100000,
                    children=[
                        """
                        The Jump Score is calculated from the current wind, 
                        gust, precipitation, temperature and cloud coverage,
                        and can be used as a guide on how pleasant jump 
                        conditions will feel.
                        """,
                    ],
                ),
                html.P(
                    children=[
                        "Today's Jump Score",
                        html.Button(
                            id="jump-score-help-button",
                            children=DashIconify(
                                icon="fluent:chat-help-24-regular",
                                color="#3498db",
                                height=24,
                                style={
                                    "padding-left": "5px",
                                    "padding-bottom": "1px",
                                    "display": "inline-block",
                                },
                            ),
                            style={
                                "border": "none",
                                "background": "none",
                            },
                        ),
                    ],
                    style={
                        "textAlign": "center",
                        "fontSize": "26px",
                        "color": "#3498db",
                        "display": "block",
                        "margin-top": "0",
                        "margin-bottom": "0.5rem",
                        "font-weight": "500",
                        "line-height": "1.2",
                    },
                ),
                dcc.Markdown(
                    describeJumpability(jump_score_results["results"]["jump_score"]),
                    # "todo - prediction and description using getJumpability limits and penalty results",
                    style={
                        "flex-direction": "column",
                        "align-items": "center",
                        "textAlign": "center",
                        "justify-content": "center",
                    },
                    className="nomargin-p wind-direction-text",
                ),
                daq.Gauge(
                    color={
                        "gradient": True,
                        "ranges": {
                            "red": [0, 50],
                            "yellow": [50, 70],
                            "green": [70, 100],
                        },
                    },
                    value=jump_score_results["results"]["jump_score"],
                    showCurrentValue=True,
                    max=100,
                    min=0,
                    style={"maxHeight": "210px"},
                    className="white-text",
                    units="Jump Score",
                ),
            ],
            style={
                "maxWidth": "80vw",
                "flex-direction": "column",
                "margin": "auto",
                "maxWidth": "550px",
                "justify-content": "center",
                "align-items": "center",
                "display": "flex",
            },
        ),
    )


def renderManifest(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        style={
            "padding": "20px",
            "fontSize": "20px",
            "color": "white",
            "margin": "auto",
            "marginBottom": "0",
        },
        # TOODO to save loading time only return a div and have
        # the renderer be called in a callback
        children=html.Div(
            [
                html.A(
                    "Live Manifest",
                    href=dropZone.liveManifestUrl,
                    style={
                        "textAlign": "center",
                        "fontSize": "26px",
                        "color": "#3498db",
                        "display": "block",
                        "margin-top": "0",
                        "margin-bottom": "0.5rem",
                        "font-weight": "500",
                        "line-height": "1.2",
                    },
                    target="_blank",
                ),
                html.Div(
                    getScreenshotImageContainer(),
                    style={
                        "maxWidth": "80vw",
                        "maxWidth": "550px",
                    },
                ),
            ],
            style={
                "maxWidth": "80vw",
                "flex-direction": "column",
                "margin": "auto",
                "maxWidth": "550px",
            },
        ),
    )


def renderAdsbInfo(dropZone: DropzoneType) -> html.Div:
    description = f"Live airspace for the {dropZone.airportIdentifier} airport."

    # validate if aircraftInfo is not None
    if dropZone.aircraftInfo is not None:
        aircraft_reg = dropZone.aircraftInfo.aircraftRegistraionNumber
        aircraft_icao = dropZone.aircraftInfo.aircraftIcao

        if aircraft_reg:  # if the aircraft registration number is not None
            description += f" Your aircraft is {aircraft_reg}"

        # adds "." at the end only if aircraft_icao is not None
        if aircraft_icao:
            description += "."
    return html.Div(
        style={
            "padding": "20px",
            "fontSize": "20px",
            "color": "white",
            "margin": "auto",
        },
        children=html.Div(
            [
                html.A(
                    "Airspace Tracker",
                    href=f"/track?id={dropZone.id}",
                    style={
                        "textAlign": "center",
                        "fontSize": "26px",
                        "color": "#3498db",
                        "display": "block",
                        "margin-top": "0",
                        "margin-bottom": "0.5rem",
                        "font-weight": "500",
                        "line-height": "1.2",
                    },
                ),
                html.Div(
                    children=description,
                    style={
                        "textAlign": "center",
                        "color": "white",
                        "maxWidth": "550px",
                        "margin": "auto",
                        "padding-bottom": "20px",
                    },
                ),
                planeTrackIframe(dropZone),
            ],
            style={
                "maxWidth": "80vw",
                "flex-direction": "column",
                "margin": "auto",
                "maxWidth": "550px",
            },
        ),
    )


def renderMetarError(airportIdentifier: str, friendlyName: str, id: str) -> html.Div:
    return html.Div(
        [
            dmc.Modal(
                title="Weather Error",
                opened=True,
                overlayBlur=5,
                overflow="inside",
                centered=True,
                closeOnEscape=True,
                children=[
                    html.A(
                        f"There seems to have been an error fetching the latest METAR weather report for {friendlyName} ({airportIdentifier})."
                    ),
                    html.Br(),
                    html.Br(),
                    html.A(
                        "Please be patient as this is not an issue with our site and may take time to be resolved. In the meantime, please check on the "
                    ),
                    html.A("local weather radar", href=f"/forecast?id={id}"),
                    html.A(" or "),
                    html.A("go back.", href=f"/search"),
                ],
            )
        ]
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    metar = weatherUtils.get_metar(dropZone.airportIdentifier)
    historicalMetar = weatherUtils.get_metar(dropZone.airportIdentifier, hours=4)
    forecastNumHours = 6
    forecastData = weatherUtils.get_forecast(
        forecastNumHours, dropZone.weatherGovGridpointLocation
    )
    return [
        renderMetarError(
            dropZone.airportIdentifier,
            dropZone.friendlyName,
            dropZone.id,
        )
        if not metar or not metar.code
        else None,
        dbc.Row(
            [
                dbc.Col(
                    [
                        renderCurrentWeather(dropZone, metar, forecastData)
                        if metar
                        else None,
                        renderJumpability(dropZone, metar, forecastData)
                        if metar
                        else None,
                        renderManifest(dropZone),
                        calenderComponents.renderCalendarCurrentDay(dropZone),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        renderWeatherOutlook(dropZone, forecastData, forecastNumHours),
                        renderAdsbInfo(dropZone),
                        renderWindTrends(dropZone, historicalMetar),
                    ],
                    md=6,
                ),
            ],
            style={
                "borderRadius": "15px",
                "backgroundColor": "rgba(47, 62, 70, 0.5)",
                "width": "80vw",
                "maxWidth": "1300px",
            },
        ),
    ]
