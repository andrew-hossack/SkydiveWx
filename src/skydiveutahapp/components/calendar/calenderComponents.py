from dash import html, dcc
from utils.dropzones.dropzoneUtils import DropzoneType
from utils.timeUtils import get_current_date_yyyymmdd

def getExternalLinkCalendarDiv(calendarLink: str) -> html.Div:
    return html.Div()

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
        html.P(content, style={'color': 'white'}, className='darker-link-color'),
        html.Iframe(src=dropZone.calendars.fullFrameUrl,
                        style={"border": "solid 1px #777", "width": "100%", "height": "600px"})
    ])


def getAllComponents(dropZone: DropzoneType) -> list[html.Div]:
    return calendarComponent(dropZone)
