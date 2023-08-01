from enum import Enum


class Cameras:
    def __init__(self, friendly_title: str, url: str) -> None:
        self.camera_data = [{'friendly_title': friendly_title, 'url': url}]

    def add(self, friendly_title: str, url: str) -> 'Cameras':
        self.camera_data.append({'friendly_title': friendly_title, 'url': url})
        return self
    
    def get(self) -> dict:
        return self.camera_data


class DropzoneType:
    def __init__(self,
                 id: str,
                 friendlyName: str,
                 weatherGovGridpointLocation: str,
                 airportIdentifier: str,
                 latitude: str,
                 longitude: str,
                 calendarSrc: str,
                 calendarSrcDayPreview: str,
                 cameras: Cameras,
                 radarBoxUrl: str,
                 liveManifestUrl: str,
                 ) -> None:
        self.id = id
        self.friendlyName = friendlyName
        self.weatherGovGridpointLocation = weatherGovGridpointLocation
        self.airportIdentifier = airportIdentifier
        self.lat = latitude
        self.long = longitude
        self.calendarSrc = calendarSrc
        self.calendarSrcDayPreview = calendarSrcDayPreview
        self.cameras = cameras
        self.radarBoxUrl = radarBoxUrl
        self.liveManifestUrl = liveManifestUrl


class Dropzones(DropzoneType, Enum):
    # List of all currently supported dropzones used the app
    SKYDIVE_UTAH = ('sdu',
                    'Skydive Utah',
                    'SLC/85,170',
                    'KTVY',
                    '40.61318686',
                    '-112.3481226',
                    "https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
                    f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
                    Cameras(
                        'Tooele North / Erda East Camera',
                        'https://www.wrh.noaa.gov/images/slc/camera/latest/TooeleN.latest.jpg').add(
                        'Tooele Camera',
                        'https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg'
                    ),
                    "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
                    "https://dzm.burblesoft.com/jmp?dz_id=385"
                    )
    # SKYDIVE_CHICAGO = ('sdc',
    #                    'Skydive Chicago',
    #                    'SLC/85,170',  # TODO
    #                    'KORD',        # TODO
    #                    '41.9802',
    #                    '-87.9090',
    #                    #    TODO src
    #                    "https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
    #                    f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
    #                    Cameras(
    #                        'Tooele North / Erda East Camera',
    #                        'https://www.wrh.noaa.gov/images/slc/camera/latest/TooeleN.latest.jpg').add(
    #                        'Tooele Camera',
    #                        'https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg'
    #                    ),
    #                    "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
    #                    "https://dzm.burblesoft.com/jmp?dz_id=385"
    #                    )

    @classmethod
    def get_dropzone_by_id(self, dropzone_id: str) -> (DropzoneType, None):
        for dropzone in self:
            if dropzone.value[0] == dropzone_id:
                return dropzone
        return None
