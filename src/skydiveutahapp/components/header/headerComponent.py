from dash import html, dcc
import dash_bootstrap_components as dbc


def render() -> html.Div:
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Skydive Utah - Live Dashboard", className="display-7",
                            style={'color': 'white', 'textAlign': 'center'}),
                    html.Div(
                        [
                            html.H1(id="live-clock", children="Loading...",
                                    style={'textAlign': 'center',
                                           'color': '#fff',
                                           'padding': '0px',
                                           'position': 'sticky',
                                           "fontSize": '10px',
                                           "zIndex": '999',
                                           }),
                            dcc.Interval(id="header-interval",
                                         interval=1*1000, n_intervals=0)
                        ],
                        style={
                            'zIndex': '999',
                        }
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("Home", href="/", active="exact"),
                            dbc.NavLink("Winds Aloft",
                                        href="/winds", active="exact"),
                            dbc.NavLink("Event Calendar",
                                        href="/calendar", active="exact"),
                            dbc.NavLink((
                                [
                                    html.Div("Live Manifest", style={
                                             'display': 'inline-block'}),
                                    html.Img(style={'display': 'inline-block'},
                                             src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==',
                                             className='external-link'),
                                ]), 
                                href="https://dzm.burblesoft.com/jmp?dz_id=385",
                                target="_blank"),
                            dbc.NavLink(
                                "Webcam - Unavailable", href="/webcam", active="exact", disabled=True),
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
