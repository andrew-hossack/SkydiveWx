from dash import html, dcc
from utils.timeUtils import get_current_date_yyyymmdd


def getTodaysEventsIFrame() -> html.Div():
    date = get_current_date_yyyymmdd()
    return html.Iframe(src=f"https://calendar.google.com/calendar/u/0/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America/Denver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=1&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day&dates={date}/{date}",
                       style={"border": "solid 1px #777", "width": "100%", "height": "300px"})


def calendarComponent() -> html.Div():
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
        html.H2('Skydive Utah Events', style={'color': 'white'}),
        html.P(content, style={'color': 'white'}, className='darker-link-color'),
        html.Iframe(src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
                        style={"border": "solid 1px #777", "width": "100%", "height": "600px"})
    ])


def getAllComponents() -> list[html.Div]:
    return calendarComponent()
