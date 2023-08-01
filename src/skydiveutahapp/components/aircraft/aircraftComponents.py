from dash import html, dcc


def iframeComponent() -> html.Div():
    return html.Div(
        html.Iframe(src="https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                       style={"frameborder":"0" ,"scrolling":"no" ,"marginheight":"0" ,"marginwidth":"0" ,"width":"1200px" ,"height":"1000px"})
    )


def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            iframeComponent(),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
        }),
    ]
