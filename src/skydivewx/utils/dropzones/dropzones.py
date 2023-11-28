from enum import Enum

from .dropzoneUtils import Calendars, Cameras, DropzoneType, Link, Socials, AircraftInfo


class Dropzones(DropzoneType, Enum):
    # List of all currently supported dropzones used the app
    SKYDIVE_CHICAGO = (
        "sdc",
        "Skydive Chicago",
        "LOT/26,75",
        "KRPJ",
        "41.8926389",
        "-89.0796111",
        Calendars(
            fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FChicago&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Chicago&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&src=bWJyYjltb2M5Yjdlb2dnZjRqcmo4dnIwYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras("Hangar", "https://webcam.skydivecsc.com/hangar_nw"),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=408&columns=5&display_menu=0&font_size=12",
        "https://embed.windy.com/embed2.html?lat=41.8926389&lon=-89.0796111&detailLat=41.8926389&detailLon=-89.0796111&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(),
        AircraftInfo(),
    )
    SKYDIVE_UTAH = (
        "sdu",
        "Skydive Utah",
        "SLC/85,170",
        "KTVY",
        "40.61318686",
        "-112.3481226",
        Calendars(
            fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            "Tooele Camera",
            "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=385",
        "https://embed.windy.com/embed2.html?lat=40.342&lon=-112.365&detailLat=40.530&detailLon=-112.300&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(title="Skydive Utah Website", url="https://skydiveutah.com/"),
            facebook=Link(url="http://www.facebook.com/skydiveutah"),
            tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            email=Link(url="mailto:fly@skydiveutah.com"),
            instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(aircraftRegistraionNumber="N13SU", aircraftIcao="a07a7b"),
    )
    SKYDIVE_WASATCH = (
        "sdw",
        "Skydive the Wasatch",
        "SLC/95,129",
        "KSPK",
        "39.74",
        "-111.87",
        Calendars(),
        Cameras(
            "Main St SR28 @ 100 N SR132 NPH (Local)",
            "http://udottraffic.utah.gov/1_devices/aux18052.jpeg",
        ).add(
            "I15 @ 100 N SR132 MP 225.26 NPH",
            "http://udottraffic.utah.gov/1_devices/aux18053.jpeg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=48",
        "https://embed.windy.com/embed2.html?lat=39.74&lon=-111.87&detailLat=39.74&detailLon=-111.87&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(),
        AircraftInfo(),
    )
    SKYDIVE_ELSINORE = (
        "sde",
        "Skydive Elsinore",
        "SGX/58,55",
        "KF70",
        "33.6329778",
        "-117.3015722",
        Calendars(
            fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America/Los_Angeles&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            dayFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America/Los_Angeles&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&src=jeup85v1iaj44m5j3iohb30hvo@group.calendar.google.com&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=189",
        "https://embed.windy.com/embed2.html?lat=33.6329778&lon=-117.3015722&detailLat=33.6329778&detailLon=-117.3015722&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(),
        AircraftInfo(),
    )
    SKYDIVE_ZHILLS = (
        "sdz",
        "Skydive City Zephyrhills",
        "TBW/82,111",
        "KZPH",
        "28.2266694",
        "-82.1556453",
        Calendars(externalLink="https://www.skydivecity.com/events/"),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=53",
        "https://embed.windy.com/embed2.html?lat=28.2266694&lon=-82.1556453&detailLat=28.2266694&detailLon=-82.1556453&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(),
        AircraftInfo(),
    )
    # SKYDIVE_DELAND = (
    #     "sdd",
    #     # https://api.weather.gov/points/lat,long
    #     "Skydive DeLand",
    #     "MLB/27,92",
    #     "KDED",
    #     "29.0670278",
    #     "-81.2837500",
    #     Calendars(
    #         # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
    #         # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
    #     ),
    #     Cameras(
    #         # "Tooele Camera",
    #         # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
    #     ),
    #     "https://www.radarbox.com/?widget=1&z=10&lat=29.0670278&lng=-81.2837500&labels=true",
    #      Cannot find burble id
    #      TODO no burble ID found
    #     "https://dzm.burblesoft.com/jmp?dz_id=<TODO>",
    #     "https://embed.windy.com/embed2.html?lat=40.342&lon=-112.365&detailLat=40.530&detailLon=-112.300&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
    #     Socials(
    #         # web=Link(title="Skydive Utah Website", url="https://skydiveutah.com/"),
    #         # facebook=Link(url="http://www.facebook.com/skydiveutah"),
    #         # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
    #         # email=Link(url="mailto:fly@skydiveutah.com"),
    #         # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
    #     ),
    #     AircraftInfo(),
    # )
    # SKYDIVE_PERRIS = (
    #     "sdp",
    #     # https://api.weather.gov/points/lat,long
    #     "Skydive Perris",
    #     "SGX/62,60",
    #     TODO no metar - needs to add option to use close metar
    #     "L65",
    #     "33.7646389",
    #     "-117.2190000",
    #     Calendars(
    #         # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
    #         # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
    #     ),
    #     Cameras(
    #         # "Tooele Camera",
    #         # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
    #     ),
    #     "https://www.radarbox.com/?widget=1&z=10&lat=33.7646389&lng=-117.2190000&labels=true",
    #     "https://dzm.burblesoft.com/jmp?dz_id=99",
    #     "https://embed.windy.com/embed2.html?lat=33.7646389&lon=-117.2190000&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
    #     Socials(
    #         web=Link(title="Skydive Perris Website", url="https://skydiveperris.com/"),
    #         facebook=Link(url="https://www.facebook.com/skydiveperris1"),
    #         # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
    #         # email=Link(url="mailto:fly@skydiveutah.com"),
    #         # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
    #     ),
    #     AircraftInfo(),
    # )
    SKYDIVE_COSTAL_CAROLINAS = (
        "scc",
        # https://api.weather.gov/points/lat,long
        "Skydive Coastal Carolinas",
        "ILM/86,54",
        "KSUT",
        "33.9308156",
        "-78.0733636",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=33.9308156&lng=-78.0733636&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=2521",
        "https://embed.windy.com/embed2.html?lat=33.9308156&lon=-78.0733636&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Coastal Carolinas Website",
                url="https://www.skydivecoastalcarolinas.com",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    # WISCONSIN_SKYDIVING_CENTER = (
    #     "wsc",
    #     # https://api.weather.gov/points/lat,long
    #     "Wisconsin Skydiving Center",
    #     "MKX/58,60",
    # TODO no metar at airport, use closest KRYV
    #     "61C",
    #     "42.9632028",
    #     "-88.8176281",
    #     Calendars(
    #         # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
    #         # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
    #     ),
    #     Cameras(
    #         # "Tooele Camera",
    #         # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
    #     ),
    #     "https://www.radarbox.com/?widget=1&z=10&lat=42.9632028&lng=-88.8176281&labels=true",
    #     "https://dzm.burblesoft.com/jmp?dz_id=43",
    #     "https://embed.windy.com/embed2.html?lat=42.9632028&lon=-88.8176281&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
    #     Socials(
    #         web=Link(
    #             title="Wisconsin Skydiving Center Website",
    #             url="https://wisconsinskydivingcenter.com/",
    #         ),
    #         # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
    #         # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
    #         # email=Link(url="mailto:fly@skydiveutah.com"),
    #         # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
    #     ),
    #     AircraftInfo(),
    # )
    SKYDIVE_INDIANAPOLIS = (
        "sdi",
        # https://api.weather.gov/points/lat,long
        "Skydive Indianapolis",
        "IND/43,91",
        "KFKR",
        "40.2734308",
        "-86.5621703",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.2734308&lng=-86.5621703&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=36",
        "https://embed.windy.com/embed2.html?lat=40.2734308&lon=-86.5621703&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Indianapolis Website",
                url="https://www.skydiveindianapolis.com/en/welcome",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    DES_MOINES_SKYDIVERS = (
        "dms",
        # https://api.weather.gov/points/lat,long
        "Des Moines Skydivers",
        "DMX/91,36",
        "KOXV",
        "41.2990969",
        "-93.1137428",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.2990969&lng=-93.1137428&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=47",
        "https://embed.windy.com/embed2.html?lat=41.2990969&lon=-93.1137428&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Des Moines Skydivers Website",
                url="https://www.desmoinesskydivers.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_PHILADELPHIA = (
        "sdp",
        # https://api.weather.gov/points/lat,long
        "Skydive Philadelphia",
        "PHI/43,95",
        "KCKZ",
        "40.3891944",
        "-75.2904722",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.3891944&lng=-75.2904722&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=47",
        "https://embed.windy.com/embed2.html?lat=40.3891944&lon=-75.2904722&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Philadelphia Website",
                url="https://www.skydivephiladelphia.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    JUMP_TN = (
        "jtn",
        # https://api.weather.gov/points/lat,long
        "Jump TN",
        "MRX/110,65",
        "KGCY",
        "36.1957222",
        "-82.8113611",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=36.1957222&lng=-82.8113611&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=230",
        "https://embed.windy.com/embed2.html?lat=36.1957222&lon=-82.8113611&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Jump TN Website",
                url="https://jumptn.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_CAROLINAS = (
        "sca",
        # https://api.weather.gov/points/lat,long
        "Skydive Carolina",
        "GSP/108,44",
        "KDCM",
        "34.7893333",
        "-81.1957778",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=34.7893333&lng=-81.1957778&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=256",
        "https://embed.windy.com/embed2.html?lat=34.7893333&lon=-81.1957778&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Carolina Website",
                url="https://www.skydivecarolina.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_MONROE = (
        "sdm",
        # https://api.weather.gov/points/lat,long
        "Skydive Monroe",
        "FFC/76,90",
        "KD73",
        "33.7825278",
        "-83.6928056",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=33.7825278&lng=-83.6928056&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=261",
        "https://embed.windy.com/embed2.html?lat=33.7825278&lon=-83.6928056&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Monroe Website",
                url="https://skydivemonroe.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(aircraftRegistraionNumber="N9059S", aircraftIcao="AC8563"),
    )
    PIEDMONT_SKYDIVING = (
        "psd",
        # https://api.weather.gov/points/lat,long
        "Piedmont Skydiving",
        "GSP/129,85",
        "KRUQ",
        "35.6458833",
        "-80.5202917",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=35.6458833&lng=-80.5202917&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=292",
        "https://embed.windy.com/embed2.html?lat=35.6458833&lon=-80.5202917&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Piedmont Skydiving Website",
                url="https://piedmontskydiving.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_ORANGE = (
        "sdo",
        # https://api.weather.gov/points/lat,long
        "Skydive Orange",
        "LWX/65,38",
        "KOMH",
        "38.2472028",
        "-78.0456211",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=38.2472028&lng=-78.0456211&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=390",
        "https://embed.windy.com/embed2.html?lat=38.2472028&lon=-78.0456211&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Orange Website",
                url="https://www.skydiveorange.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_WINDY_CITY_CHICAGO = (
        "swc",
        # https://api.weather.gov/points/lat,long
        "Skydive Windy City Chicago",
        "IWX/10,63",
        "KMGC",
        "41.7033153",
        "-86.8212400",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.7033153&lng=-86.8212400&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=12691",
        "https://embed.windy.com/embed2.html?lat=41.7033153&lon=-86.8212400&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Windy City Chicago Website",
                url="https://skydivewindycitychicago.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
    SKYDIVE_CENTER_SAN_ANTONIO = (
        "csa",
        # https://api.weather.gov/points/lat,long
        "Skydive Castroville",
        "EWX/113,51",
        "KCVB",
        "29.3423889",
        "-98.8512222",
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(
            # "Tooele Camera",
            # "https://www.wrh.noaa.gov/images/slc/camera/latest/tooele.latest.jpg",
        ),
        "https://www.radarbox.com/?widget=1&z=10&lat=29.3423889&lng=-98.8512222&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=8681",
        "https://embed.windy.com/embed2.html?lat=29.3423889&lon=-98.8512222&detailedLat=29.3423889&detailedLon=-98.8512222&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Castroville Website",
                url="https://skydivecastroville.com/",
            ),
            # facebook=Link(url="https://www.facebook.com/skydiveperris1"),
            # tiktok=Link(url="https://www.tiktok.com/@skydiveutah"),
            # email=Link(url="mailto:fly@skydiveutah.com"),
            # instagram=Link(url="https://www.instagram.com/skydiveutah/"),
        ),
        AircraftInfo(),
    )
