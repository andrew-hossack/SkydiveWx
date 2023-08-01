from dash import html

from components.search import searchComponents


def render() -> html.Div:
    return html.Div(
        id='search-page-container',
        children=searchComponents.getAllComponents(),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'flex-direction': 'column',
            'margin': '0',
            'height':'100vh',
            'width':'100vw',
            "background": "url('/assets/storm.png')",
        },
    )
