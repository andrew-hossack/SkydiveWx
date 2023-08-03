from enum import Enum


class Calendars:
    def __init__(self, fullFrameUrl: str = None, dayFrameUrl: str = None, externalLink: str = None) -> None:
        #   Needs either fullFrameUrl and dayFrameUrl or externalLink
        self.fullFrameUrl = fullFrameUrl
        self.dayFrameUrl = dayFrameUrl
        self.externalLink = externalLink

    def get(self) -> dict:
        return {'fullFrameUrl': self.fullFrameUrl, 'dayFrameUrl': self.dayFrameUrl, 'externalLink': self.externalLink}


class Cameras:
    def __init__(self, friendly_title: str = None, url: str = None) -> None:
        if (friendly_title and url):
            self.camera_data = [{'friendly_title': friendly_title, 'url': url}]

    def add(self, friendly_title: str, url: str) -> 'Cameras':
        self.camera_data.append({'friendly_title': friendly_title, 'url': url})
        return self

    def get(self) -> (dict, None):
        try:
            self.camera_data
        except AttributeError:
            # No cameras loaded
            return None
        return self.camera_data


class DropzoneType:
    def __init__(self,
                 id: str,
                 friendlyName: str,
                 weatherGovGridpointLocation: str,
                 airportIdentifier: str,
                 latitude: str,
                 longitude: str,
                 #  calendarSrc: str,
                 #  calendarSrcDayPreview: str,
                 calendars: Calendars,
                 cameras: Cameras,
                 radarBoxUrl: str,
                 liveManifestUrl: str,
                 weatherRadariFrameUrl: str,
                 ) -> None:
        self.id = id
        self.friendlyName = friendlyName
        # If you do not know the grid that correlates to your location, you can use the /points endpoint to retrieve the exact grid endpoint by coordinates:
        # https://api.weather.gov/points/{latitude},{longitude}
        self.weatherGovGridpointLocation = weatherGovGridpointLocation
        self.airportIdentifier = airportIdentifier
        # See https://www.airnav.com/airport/<IDENTIFIER>
        self.lat = latitude
        self.long = longitude
        self.calendars = calendars
        self.cameras = cameras
        # https://www.radarbox.com
        self.radarBoxUrl = radarBoxUrl
        # https://dzm.burblesoft.com/jmp?dz_id=<ID> ; get id from utils/getBurbleIds.py file - should be listed there
        self.liveManifestUrl = liveManifestUrl
        # https://embed.windy.com/
        self.weatherRadariFrameUrl = weatherRadariFrameUrl
        # Todo drawer menue and weather pages


class Dropzones(DropzoneType, Enum):
    # List of all currently supported dropzones used the app
    SKYDIVE_CHICAGO = ('sdc',
                       'Skydive Chicago',
                       'LOT/26,75',
                       'KRPJ',
                       '41.8926389',
                       '-89.0796111',
                       Calendars(
                           fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FChicago&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
                           dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Chicago&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
                       ),
                       Cameras(
                           'Hangar',
                           'https://webcam.skydivecsc.com/hangar_nw'),
                       "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                       "https://dzm.burblesoft.com/jmp?dz_id=408&columns=5&display_menu=0&font_size=12",
                       "https://embed.windy.com/embed2.html?lat=41.8926389&lon=-89.0796111&detailLat=41.8926389&detailLon=-89.0796111&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1"
                       #    TODO radarbox
                       )
    SKYDIVE_UTAH = ('sdu',
                    'Skydive Utah',
                    'SLC/85,170',
                    'KTVY',
                    '40.61318686',
                    '-112.3481226',
                    Calendars(
                        fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
                        dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
                    ),
                    Cameras(
                        'Tooele North / Erda East Camera',
                        'https://www.wrh.noaa.gov/images/slc/camera/latest/TooeleN.latest.jpg').add(
                        'Tooele Camera',
                        'https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg'
                    ),
                    "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                    "https://dzm.burblesoft.com/jmp?dz_id=385",
                    "https://embed.windy.com/embed2.html?lat=40.342&lon=-112.365&detailLat=40.530&detailLon=-112.300&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1"
                    # TODO menu drawer
                    )
    SKYDIVE_WASATCH = ('sdw',
                       'Skydive the Wasatch',
                       'SLC/95,129',
                       'KSPK',
                       '39.74',
                       '-111.87',
                       Calendars(),
                       Cameras(
                           'Main St SR28 @ 100 N SR132 NPH (Local)',
                           'http://udottraffic.utah.gov/1_devices/aux18052.jpeg').add(
                           'I15 @ 100 N SR132 MP 225.26 NPH',
                           'http://udottraffic.utah.gov/1_devices/aux18053.jpeg'
                       ),
                       "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                       "https://dzm.burblesoft.com/jmp?dz_id=48",
                       "https://embed.windy.com/embed2.html?lat=39.74&lon=-111.87&detailLat=39.74&detailLon=-111.87&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1"
                       # TODO rararbox
                       )
    SKYDIVE_ELSINORE = ('sde',
                        'Skydive Elsinore',
                        'SGX/58,55',
                        'KF70',
                        '33.6329778',
                        '-117.3015722',
                        Calendars(
                            fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America/Los_Angeles&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
                            dayFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America/Los_Angeles&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0&mode=day",
                        ),
                        Cameras(),
                        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                        "https://dzm.burblesoft.com/jmp?dz_id=189",
                        "https://embed.windy.com/embed2.html?lat=33.6329778&lon=-117.3015722&detailLat=33.6329778&detailLon=-117.3015722&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1"
                        # TODO rararbox
                        )
    SKYDIVE_ZHILLS = ('sdz',
                      'Skydive City Zephyrhills',
                      'TBW/82,111',
                      'KZPH',
                      '28.2266694',
                      '-82.1556453',
                      Calendars(
                          externalLink="https://www.skydivecity.com/events/"),
                      Cameras(),
                      "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                      "https://dzm.burblesoft.com/jmp?dz_id=53",
                      "https://embed.windy.com/embed2.html?lat=28.2266694&lon=-82.1556453&detailLat=28.2266694&detailLon=-82.1556453&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1"
                      # TODO rararbox
                      )

    @classmethod
    def get_dropzone_by_id(self, dropzone_id: str) -> (DropzoneType, None):
        for dropzone in self:
            if dropzone.value[0] == dropzone_id:
                return dropzone
        return None
