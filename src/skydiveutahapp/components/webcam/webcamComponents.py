from dash import dcc, html
from utils.dropzones.dropzoneUtils import DropzoneType


def _generate_components(dropZone: DropzoneType) -> list[html.Div]:
    components = []
    for camera in dropZone.cameras.get():
        title = camera['friendly_title']
        url = camera['url']
        div = html.Div(
            children=title,
            style={'textAlign': 'center', 'color': 'white'}
        )
        link = dcc.Link(
            html.Img(
                src=url,
                width="100%",
                title=title,
                style={'paddingTop': '5px', 'paddingBottom': '20px'}
            ),
            href=url,
            target='_blank',
            title='Open in New Tab'
        )
        components.append(div)
        components.append(link)
    return components


def webcamComponent(dropZone: DropzoneType) -> html.Div():
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
            *_generate_components(dropZone),
            dcc.Markdown('''
            _*To view additional camera feeds, please visit [https://www.weather.gov/slc/Cameras](https://www.weather.gov/slc/Cameras) or [https://www.wrh.noaa.gov/slc/webcam_map_CSV](https://www.wrh.noaa.gov/slc/webcam_map_CSV)_
            ''', style={'color': 'white', 'font-size': '12px', 'margin-top': '10px', "overflow-wrap": "break-word"})
        ]
    )


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return [
        html.Div([
            webcamComponent(dropZone),
        ], style={
            'borderRadius': '15px',
            'backgroundColor': 'rgba(47, 62, 70, 0.5)',
            'width': '80vw',
            'maxWidth': '750px',
        }),
    ]
