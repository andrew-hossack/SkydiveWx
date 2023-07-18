from dash import html, dcc
import dash_bootstrap_components as dbc


def render() -> html.Div:
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Skydive Utah - Live App", className="display-7",
                            style={'color': 'white', 'textAlign': 'center'}),
                    html.Div(
                        [
                            html.H1(id="live-clock", children="current time",
                                    style={'textAlign': 'center',
                                        'color': '#fff',
                                        'padding': '0px',
                                        'position': 'sticky',
                                        "fontSize": '10px',
                                        "zIndex": '999',
                                    }),
                            dcc.Interval(id="header-interval", interval=1*1000, n_intervals=0)
                        ],
                        style={
                            'zIndex': '999',
                        }
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("Home", href="/", active="exact"),
                            dbc.NavLink("Winds Aloft", href="/winds", active="exact"),
                            dbc.NavLink("Webcam", href="/webcam", active="exact"),
                            dbc.NavLink("Live Manifest", href="https://dzm.burblesoft.com/jmp?dz_id=385", target="_blank", className="external"),
                            dbc.NavLink("Skydive Utah", href="https://skydiveutah.com", target="_blank", className="external"),
                        ],
                        horizontal="center",
                        pills=True,
                    )
                ],
                style={
                    'backgroundColor': 'rgba(51, 51, 51, 0.5)', 
                    'padding': '10px', 
                    'position': 'sticky', 
                    'top': '32px',
                }
            )
        ]
    )