from dash import html


def radarComponent() -> html.Div():
    return html.Div([
        html.Iframe(src="https://embed.windy.com/embed2.html?lat=40.342&lon=-112.365&detailLat=40.530&detailLon=-112.300&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
                        style={"border": "0", "width": "100%", "height": "80vh"})
    ])

def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            radarComponent(),
        ], style={

            'width': '100%',
            'height': '100%',
        }),
    ]
