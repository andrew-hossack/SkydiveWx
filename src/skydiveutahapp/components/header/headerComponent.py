import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html, get_asset_url
from dash_iconify import DashIconify
from utils.dropzones.dropzoneUtils import DropzoneType


def _get_icon(icon, color: str | None = None, height=16):
    return DashIconify(icon=icon, height=height, color=color)


def _renderNavDrawer(dropZone: DropzoneType) -> html.Div:
    return [
        dmc.Stack(
            [
                html.Div([
                    _get_icon(icon="uil:bolt", height=14),
                    dmc.Divider(label="General Information",
                                style={'width': '100%', 'marginLeft': '5px'}),
                ], style={'display': 'flex', 'width': '100%', 'alignItems': 'center'}),

                dmc.NavLink(
                    label="Local Weather Radar",
                    icon=_get_icon(
                        icon="clarity:radar-line"),
                    href=f'/forecast?id={dropZone.id}'
                ),
                dmc.NavLink(
                    label="Plane Tracker - Coming Soon",
                    icon=_get_icon(
                        icon="clarity:airplane-line"),
                    href='/aircraft',
                    disabled=True
                ),

                html.Div([
                    _get_icon(icon="basil:chat-outline", height=14),
                    dmc.Divider(label="Connect With Us",
                                style={'width': '100%', 'marginLeft': '5px'}),
                ], style={'display': 'flex', 'width': '100%', 'alignItems': 'center'}),

                dmc.NavLink(
                    label="Skydive Utah Website",
                    icon=_get_icon(
                        icon="mdi:web"),
                    href='https://skydiveutah.com/'
                ),
                dmc.NavLink(
                    label="Instagram",
                    icon=_get_icon(
                        icon="mdi:instagram"),
                    href='https://www.instagram.com/skydiveutah/'
                ),
                dmc.NavLink(
                    label="Facebook",
                    icon=_get_icon(
                        icon="ic:baseline-facebook"),
                    href='http://www.facebook.com/skydiveutah'
                ),
                dmc.NavLink(
                    label="TikTok",
                    icon=_get_icon(
                        icon="ic:baseline-tiktok"),
                    href='https://www.tiktok.com/@skydiveutah'
                ),
                dmc.NavLink(
                    label="Email",
                    icon=_get_icon(
                        icon="fontisto:email"),
                    href='mailto:fly@skydiveutah.com'
                ),

                html.Div([
                    _get_icon(icon="mdi:about-circle-outline", height=14),
                    dmc.Divider(label="About",
                                style={'width': '100%', 'marginLeft': '5px'}),
                ], style={'display': 'flex', 'width': '100%', 'alignItems': 'center'}),

                dmc.NavLink(
                    label="Project GitHub",
                    icon=_get_icon(
                        icon="mdi:github"),
                    href='https://github.com/andrew-hossack/Skydive-Utah-Community'
                ),

                dmc.NavLink(
                    label="Support Us",
                    icon=_get_icon(
                        icon="octicon:sponsor-tiers-24"),
                    href='https://github.com/sponsors/andrew-hossack'
                ),
            ],
            align='flex-start',
            spacing='md',
        )
    ]


def render(dropZone: DropzoneType) -> html.Div:
    return html.Div(
        [
            html.Div(
                [
                    html.A(
                        DashIconify(
                            icon="ep:back",
                            width=20),
                        style={'float': 'left', 'color': 'white',
                               'opacity': '0.8', 'position': 'absolute'},
                        href='/search'),
                    html.H2(f"{dropZone.friendlyName} Dashboard", className="display-7",
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
                            dbc.NavLink(
                                "Home", href=f"/home?id={dropZone.id}", active="exact"),
                            dbc.NavLink("Calendar",
                                        href=f"/calendar?id={dropZone.id}", active="exact"),
                            dbc.NavLink("Winds Aloft",
                                        href=f"/winds?id={dropZone.id}", active="exact"),
                            dbc.NavLink("Live Cameras",
                                        href=f"/cameras?id={dropZone.id}", active="exact"),
                            dbc.NavLink(
                                [
                                    html.Div([
                                        html.Div("Live Manifest", style={
                                            'display': 'block'
                                        }),
                                        html.Img(style={},
                                                 src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==',
                                                 className='external-link'),
                                    ], style={'alignItems': 'center', 'display': 'flex'}),
                                ],
                                href=dropZone.liveManifestUrl,
                                target="_blank"),
                            dbc.NavLink((
                                [
                                    html.Div("More", style={
                                             'display': 'inline-block', 'cursor': 'pointer'},
                                             id="drawer-demo-label",
                                             ),
                                    html.Div(
                                        [
                                            dmc.ActionIcon(
                                                DashIconify(
                                                    icon="clarity:menu-line", width=15),
                                                size="sm",
                                                variant="transparent",
                                                id="drawer-demo-button",
                                                style={'marginLeft': '5px',
                                                       'color': '#2196f3'}
                                            ),
                                            dmc.Drawer(
                                                title="Additional Resources",
                                                id="header-drawer",
                                                padding="md",
                                                zIndex=10000,
                                                children=_renderNavDrawer(
                                                    dropZone),
                                                overlayBlur=5,
                                            ),
                                        ],
                                    )
                                ]), style={'display': 'flex', 'alignItems': 'center'},),
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


def searchpageHeader() -> html.Div:
    return html.Div(
        [
            # html.A(
            #     DashIconify(
            #         icon="mingcute:back-fill",
            #         width=20),
            #     style={'float': 'left', 'color': 'white',
            #            'opacity': '0.3', 'position': 'absolute'},
            #     href='/search'),
            html.Img(src=get_asset_url('logo.png'), style={
                'width': '180px'}), #, 'filter': 'invert(1)'
            # html.Div(
            #     [
            #         html.H1(id="live-clock", children="Loading...",
            #                 style={'textAlign': 'center',
            #                        'color': '#fff',
            #                        'padding': '0px',
            #                        'position': 'sticky',
            #                        "fontSize": '10px',
            #                        "zIndex": '999',
            #                        }),
            #         dcc.Interval(id="header-interval",
            #                      interval=1*1000, n_intervals=0)
            #     ],
            #     style={
            #         'zIndex': '999',
            #     }
            # ),
            # dbc.Nav(
            #     [
            #         # dbc.NavLink(
            #         #     "Home", href=f"/home?id={dropZone.id}", active="exact"),
            #         # dbc.NavLink("Calendar",
            #         #             href=f"/calendar?id={dropZone.id}", active="exact"),
            #         # dbc.NavLink("Winds Aloft",
            #         #             href=f"/winds?id={dropZone.id}", active="exact"),
            #         # dbc.NavLink("Live Cameras",
            #         #             href=f"/cameras?id={dropZone.id}", active="exact"),
            #         # dbc.NavLink(
            #         #     [
            #         #         html.Div([
            #         #             html.Div("Live Manifest", style={
            #         #                 'display': 'block'
            #         #             }),
            #         #             html.Img(style={},
            #         #                      src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==',
            #         #                      className='external-link'),
            #         #         ], style={'alignItems': 'center', 'display': 'flex'}),
            #         #     ],
            #         #     href=dropZone.liveManifestUrl,
            #         #     target="_blank"),
            #         dbc.NavLink((
            #             [
            #                 # html.Div("More", style={
            #                 #          'display': 'inline-block', 'cursor': 'pointer'},
            #                 #          id="drawer-demo-label",
            #                 #          ),
            #                 # html.Div(
            #                 #     [
            #                 #         dmc.ActionIcon(
            #                 #             DashIconify(
            #                 #                 icon="clarity:menu-line", width=15),
            #                 #             size="sm",
            #                 #             variant="transparent",
            #                 #             id="drawer-demo-button",
            #                 #             style={'marginLeft': '5px',
            #                 #                    'color': '#2196f3'}
            #                 #         ),
            #                 #         # dmc.Drawer(
            #                 #         #     title="Additional Resources",
            #                 #         #     id="header-drawer",
            #                 #         #     padding="md",
            #                 #         #     zIndex=10000,
            #                 #         #     children=_renderNavDrawer(
            #                 #         #         dropZone),
            #                 #         #     overlayBlur=5,
            #                 #         # ),
            #                 #     ],
            #                 # )
            #             ]), style={'display': 'flex', 'alignItems': 'center'},),
            #     ],
            #     horizontal="center",
            #     pills=True,
            # )
        ],
        style={
            'backgroundColor': 'rgb(245, 245, 246)',
            'padding': '10px',
            'width':'100vw',
            # 'border-bottom': '1px solid rgba(0,0,0,0.1)',
            'box-shadow': '0 0 2px rgba(0,0,0,0.5)',
            'position':'absolute',
            'z-index':'99999'
        }
    )
