from dash import html, dcc


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

        _If you are looking to make a tandem skydive reservation, please go to our booking system._
        ''')
    return html.Div([
        html.H2('Skydive Utah Events', style={'color': 'white'}),
        html.P(content, style={'color': 'white'}),
        html.Iframe(src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FDenver&amp;src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&amp;src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&amp;color=%23E4C441&amp;color=%232276b9&amp;showTitle=0&amp;showNav=1&amp;showDate=1&amp;showPrint=0&amp;showTabs=1&amp;showCalendars=0&amp;showTz=0",
                        style={"border": "solid 1px #777", "width": "100%", "height": "600px"})
    ])


def getAllComponents() -> list[html.Div]:
    return calendarComponent()
