from dash import html, dcc


def webcamComponent() -> html.Div():
    return html.Div(
        style={
            'margin': '20px',
            'fontSize': '20px',
            'color': 'white',
        },
        children=[
            html.H2('Live Cameras',
                    style={
                        'textAlign': 'center',
                        'fontSize': '26px',
                        'color': '#3498db',
                        'paddingBottom': '15px',
                    }),
            html.Div(children='Tooele North / Erda East Camera',
                     style={
                         'textAlign': 'center', 'color': 'white'}),
            dcc.Link(
                html.Img(
                    src="https://www.wrh.noaa.gov/images/slc/camera/latest/TooeleN.latest.jpg",
                    width="100%",
                    title="Tooele North	/ Erda East",
                    style={'paddingTop': '5px', 'paddingBottom': '20px'}
                ),
                href='https://www.wrh.noaa.gov/images/slc/camera/latest/TooeleN.latest.jpg',
                target='_blank',
                title='Open in New Tab'
            ),
            html.Div(children='Tooele Camera',
                     style={
                         'textAlign': 'center', 'color': 'white'}),
            dcc.Link(
                html.Img(
                    src="https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
                    width="100%",
                    title="Tooele",
                    style={'paddingTop': '5px', 'paddingBottom': '20px'}
                ),
                href='https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg',
                target='_blank',
                title='Open in New Tab'
            ),
            dcc.Markdown('''
            _*To view additional camera feeds, please visit [https://www.weather.gov/slc/Cameras](https://www.weather.gov/slc/Cameras) or [https://www.wrh.noaa.gov/slc/webcam_map_CSV](https://www.wrh.noaa.gov/slc/webcam_map_CSV)_
            ''', style={'color': 'white', 'font-size': '12px', 'margin-top': '10px', "overflow-wrap": "break-word"})
        ]
    )


def getAllComponents() -> list[html.Div]:
    return [
        html.Div([
            webcamComponent(),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'width': '80vw',
            'maxWidth': '750px',
        }),
    ]
