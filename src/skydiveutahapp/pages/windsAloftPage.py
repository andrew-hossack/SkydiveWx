from dash import html

from components.winds import windsComponents


def render() -> html.Div:
    return html.Div(
        id='winds-page-container',
        children=windsComponents.getAllComponents(),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'marginTop': '0',
            'backgroundColor': 'transparent',
        }
    )
