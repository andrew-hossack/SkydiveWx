from dash import html

from components.aircraft import aircraftComponents


def render() -> html.Div:
    return html.Div(
        id='aircraft-page-container',
        children=aircraftComponents.getAllComponents(),
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
