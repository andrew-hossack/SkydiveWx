from dash import html, dcc
from utils.dropzones.dropzoneUtils import DropzoneType
from utils.timeUtils import get_current_date_yyyymmdd


def getTodaysEventsIFrame(dropZone: DropzoneType) -> html.Div():
    date = get_current_date_yyyymmdd()
    return html.Iframe(src=f"{dropZone.calendars.dayFrameUrl}&dates={date}/{date}",
                       style={"border": "0", "width": "100%", "height": "210px"})


def calendarComponent(dropZone: DropzoneType) -> html.Div():
    content = dcc.Markdown('''
        This calendar contains:
        - Daily opening times
        - Closure notices due to bad weather
        - Organizers
        - Instructional Camps
        - Canopy Courses
        - Ratings Courses
        
        **Postings may change sometimes without notice. Check back for updates.**
        
        _If you are looking to make a tandem skydive reservation, please go to our [booking system](https://bookings.burblesoft.com/index/385/18)._
        ''')
    return html.Div([
        html.H2(f'{dropZone.friendlyName} Events', style={'color': 'white'}),
        html.P(content, style={'color': 'white'},
               className='darker-link-color'),
        html.Iframe(src=dropZone.calendars.fullFrameUrl,
                    style={"border": "solid 1px #777", "width": "100%", "height": "600px"})
    ])


def renderCalendarCurrentDay(dropZone: DropzoneType) -> html.Div:
    possibleCalendars = dropZone.calendars
    if (possibleCalendars.dayFrameUrl and possibleCalendars.fullFrameUrl):
        calendarPreviewDiv = getTodaysEventsIFrame(dropZone)
        return html.Div(
            style={
                'padding': '20px',
                'fontSize': '20px',
                'color': 'white',
                'margin': 'auto'
            },
            children=html.Div([
                html.H2("Today's Events",
                        style={
                            'textAlign': 'center',
                            'fontSize': '26px',
                            'color': '#3498db'
                        }),

                html.Div([
                    calendarPreviewDiv,
                ], style={
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                }),
            ], style={'maxWidth': '80vw',
                      'flex-direction': 'column',
                      'margin': '0 auto',
                      'maxWidth': '550px',
                      })
        )
    else:
        # Empty Div if external link, only link in tab
        calendarPreviewDiv = html.Div()
        return calendarPreviewDiv


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return calendarComponent(dropZone)
