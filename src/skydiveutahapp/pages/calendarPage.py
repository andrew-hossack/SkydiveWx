from dash import html

from components.calendar import calenderComponents


def render() -> html.Div:
    return html.Div(
        id='calendar-page-container',
        children=calenderComponents.getAllComponents()
    )
