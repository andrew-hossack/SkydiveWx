from dash import html

from components.webcam import webcamComponents


def render() -> html.Div:
    return html.Div(
        id='webcam-page-container',
        children=webcamComponents.getAllComponents(),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent',
            'marginBottom': '20px',
        }
    )
