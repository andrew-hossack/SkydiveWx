import traceback
from dash import html, dcc
import dash_mantine_components as dmc


def render() -> html.Div:
    return html.Div(
        id='error-page-container',
        children=[
            dmc.Modal(
                title="Application Error",
                id="modal-simple",
                opened=True,
                centered=True,
                closeOnClickOutside=False,
                closeOnEscape=False,
                withCloseButton=False,
                zIndex=10000,
                children=[
                    dcc.Markdown(
                        f"Sorry! If you are seeing this, an error occurred. Please notify [admin@skydivewx.com](mailto:admin@skydivewx.com) to resolve the issue."),
                        html.Br(),
                        html.P(f'Error Information:'),
                        html.P(f'{traceback.format_exc()}', style={'font-size':'10px'})
                    ],
            ),
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent',
            'marginBottom': '20px',
            "padding": "2rem 1rem",
        }
    )
