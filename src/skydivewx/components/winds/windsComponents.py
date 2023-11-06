import json

import requests
from dash import dash_table, dcc, html
from plotly.graph_objs import Scatter
from utils.dropzones.dropzoneUtils import DropzoneType
from utils import timeUtils, weatherUtils
import dash_mantine_components as dmc


def _get_data(lat: str, long: str) -> dict:
    # Getting the data from the url
    url = f"https://markschulze.net/winds/winds.php?lat={lat}&lon={long}&hourOffset=0%3F&referrer=SkydiveUtah"
    response = requests.get(url)
    return json.loads(response.text)


def _render_table(data) -> dmc.Table:
    # Prepare data for the table
    table_data = [
        html.Tr(
            [
                html.Td(f"{altFt} Ft"),
                html.Td(f"{data['directionRaw'][str(altFt)]}°"),
                html.Td(f"{data['speedRaw'][str(altFt)]} Kts"),
                html.Td(f"{int(float(data['tempRaw'][str(altFt)]) * (9 / 5) + 32)}°F"),
            ]
        )
        for altFt in data["altFtRaw"]
        if altFt <= 20000
    ]

    # Create the table
    return dmc.Table(
        [
            html.Thead(
                html.Tr(
                    [
                        html.Th("Altitude", style={"color": "white"}),
                        html.Th("Direction", style={"color": "white"}),
                        html.Th("Speed", style={"color": "white"}),
                        html.Th("Temperature", style={"color": "white"}),
                    ],
                )
            ),
            html.Tbody(table_data),
        ],
        horizontalSpacing=2,
        style={
            "color": "white",
            "width": "100%",
            "table-layout": "fixed",
            "font-size": "1vw",
            "word-wrap": "break-word",
        },
    )


def _resolve_wind_direction(data: dict, altitudes: list) -> list[list]:
    # This method probably sucks, I used chatgpt for help lol
    wrapped_altitudes = []
    wrapped_wind_dirs = []
    dir_data = [data["directionRaw"][str(alt)] for alt in altitudes]

    temp_alts = [altitudes[0]]
    temp_dirs = [dir_data[0]]
    for i in range(1, len(dir_data)):
        if abs(dir_data[i] - dir_data[i - 1]) > 180:
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


def _handleWindsData(data) -> dict:
    """speedRaw and directionRaw are strings not ints -
    modify the data to reflect this"""
    # Modify the original fields to store the converted values
    data["speedRaw"] = {k: int(v) for k, v in data["speedRaw"].items()}
    data["directionRaw"] = {k: int(v) for k, v in data["directionRaw"].items()}
    return data


def renderWindsAloft(dropZone: DropzoneType) -> html.Div:
    winds_aloft_data = _get_data(dropZone.lat, dropZone.long)
    winds_aloft_data = _handleWindsData(winds_aloft_data)
    metar = weatherUtils.get_metar(dropZone.airportIdentifier)

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

    altitude_list = [altFt for altFt in winds_aloft_data["altFtRaw"] if altFt <= 20000]

    wind_speed_trace = Scatter(
        y=[altFt for altFt in winds_aloft_data["altFtRaw"] if altFt <= 20000],
        x=[
            winds_aloft_data["speedRaw"][str(altFt)]
            for altFt in winds_aloft_data["altFtRaw"]
            if altFt <= 20000
        ],
        mode="lines",
        name="Wind Speed (Kts)",
        # hovertemplate='Wind speed: %{y} kts<extra></extra>',
        line=dict(color="coral", shape="spline", width=3),
    )

    altitudes_by_trace, winds_by_trace = _resolve_wind_direction(
        winds_aloft_data, altitude_list
    )
    wind_dir_traces = [
        Scatter(
            y=altitudes_by_trace[i],
            x=winds_by_trace[i],
            mode="lines",
            xaxis="x2" if i % 2 == 0 else "x3",
            name="Wind Direction (°)",
            # hovertemplate='Wind direction: %{y}°<extra></extra>',
            showlegend=True if i == 0 else False,
            line=dict(shape="spline", width=3),
            marker=dict(color="mintcream"),
        )
        for i in range(len(altitudes_by_trace))
    ]

    tickrange = [
        min(
            int(value)
            for key, value in winds_aloft_data["directionRaw"].items()
            if int(key) <= 20000
        ),
        max(
            int(value)
            for key, value in winds_aloft_data["directionRaw"].items()
            if int(key) <= 20000
        ),
    ]
    tickvals = [i for i in range(min(tickrange), max(tickrange) + 1, 30)]
    ticktext = [f"{i%360}°" for i in tickvals]

    return html.Div(
        style={
            "padding": "20px",
            "margin-top": "20px",
            "margin-left": "20px",
            "margin-right": "20px",
            "margin-bottom": "0px",
            "fontSize": "20px",
            "color": "black",
        },
        children=[
            html.H2(
                f'Winds Aloft - Updated at {timeUtils.zulu_to_mst_string(winds_aloft_data["validtime"])}',
                style={"textAlign": "center", "fontSize": "26px", "color": "#3498db"},
            ),
            html.Div(
                style={
                    "backgroundColor": "rgba(47, 62, 70, 0)",
                    "padding": "10px",
                    "maxWidth": "400px",
                    "margin": "auto",
                    "color": "white",
                    "fontSize": "12px",
                    "display": "grid",
                    "gridTemplateColumns": "1fr 2fr",
                    "alignItems": "center",
                    "justifyContent": "space-between",
                    "gridGap": "5px",
                },
                children=[
                    html.Strong("Altimeter: "),
                    html.Span(
                        str.capitalize(metar.press.string("in")),
                        style={
                            "text-align": "right",
                            "white-space": "normal",
                        },
                    ),
                    html.Strong("Density Altitude: "),
                    html.Span(
                        f'{weatherUtils._calculate_density_altitude(metar.press.value("in"), metar.temp.value("C"))} ft',
                        style={
                            "text-align": "right",
                            "white-space": "normal",
                        },
                    ),
                    html.Strong(
                        "Updated At: ",
                        style={"text-align": "left"},
                    ),
                    html.Span(
                        timeUtils.time_diff(metar.time),
                        id="time-since-last-update",
                        style={
                            "text-align": "right",
                            "white-space": "normal",
                        },
                    ),
                ],
            )
            if metar
            else None,
            dcc.Graph(
                style={"width": "100%", "display": "inline-block", "height": "600px"},
                figure=dict(
                    data=[wind_speed_trace, *wind_dir_traces],
                    layout=dict(
                        margin=dict(l=40, r=10, t=80, b=80),
                        xaxis=dict(
                            title="Wind Speed (Kts)",
                            showgrid=True,
                            gridcolor="rgba(255, 255, 255, 0.2)",
                            color="coral",
                            showline=False,
                            linecolor="coral",
                            fixedrange=True,
                        ),
                        xaxis2=dict(
                            title="Wind Direction (°)",
                            overlaying="x",
                            side="top",
                            showgrid=False,
                            gridcolor="rgba(255, 255, 255, 0.2)",
                            range=tickrange,
                            tickvals=tickvals,
                            ticktext=ticktext,
                            color="mintcream",
                            showline=False,
                            linecolor="mintcream",
                            fixedrange=True,
                        ),
                        xaxis3=dict(
                            overlaying="x",
                            side="bottom",
                            showgrid=False,
                            range=tickrange,
                            tickvals=tickvals,
                            ticktext=ticktext,
                            color="mintcream",
                            showline=False,
                            showticklabels=False,
                            fixedrange=True,
                        ),
                        yaxis=dict(
                            title="Altitude (ft)",
                            showgrid=True,
                            gridcolor="rgba(255, 255, 255, 0.2)",
                            fixedrange=True,
                        ),
                        hovermode="y unified",
                        dragmode=False,
                        template="plotly_dark",
                        plot_bgcolor="rgba(47, 62, 70, 0)",
                        paper_bgcolor="rgba(47, 62, 70, 0)",
                        font={"color": "white"},
                        autosize=True,
                        showlegend=False,
                    ),
                ),
                config=dict(displayModeBar=False),
            ),
            html.Div(
                _render_table(winds_aloft_data),
                style={
                    "paddingTop": "20px",
                    "marginTop": "-20px",
                },
            ),
            dcc.Markdown(
                """
            _Credit to [Mark Schulze](http://markschulze.net/winds) for providing API access to winds aloft data._
            """,
                style={"color": "white", "font-size": "12px", "margin-top": "10px"},
            ),
        ],
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div(
            [renderWindsAloft(dropZone)],
            style={
                "borderRadius": "15px",
                "backgroundColor": "rgba(47, 62, 70, 0.5)",
                "width": "80vw",
                "maxWidth": "750px",
            },
        ),
    ]
