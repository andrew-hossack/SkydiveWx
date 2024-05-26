from enum import Enum

from .dropzoneUtils import (
    Calendars,
    Cameras,
    DropzoneType,
    Link,
    Socials,
    AircraftInfo,
    AirportAndWeatherIdentifiers,
    GeoLocation,
)


# List of all currently supported dropzones used the app
class Dropzones(DropzoneType, Enum):
    SKYDIVE_CHICAGO = (
        "sdc",
        "Chicagoland Skydiving Center",
        "LOT/26,75",
        AirportAndWeatherIdentifiers("KRPJ", "KRPJ"),
        GeoLocation("41.8926389", "-89.0796111"),
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
        AirportAndWeatherIdentifiers("KTVY", "KTVY"),
        GeoLocation("40.61318686", "-112.3481226"),
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
        AirportAndWeatherIdentifiers("KSPK", "KSPK"),
        GeoLocation("39.74", "-111.87"),
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
        AirportAndWeatherIdentifiers("KF70", "KF70"),
        GeoLocation("33.6329778", "-117.3015722"),
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
        AirportAndWeatherIdentifiers("KZPH", "KZPH"),
        GeoLocation("28.2266694", "-82.1556453"),
        Calendars(externalLink="https://www.skydivecity.com/events/"),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.41716531358273&lng=-112.38408068409743&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=53",
        "https://embed.windy.com/embed2.html?lat=28.2266694&lon=-82.1556453&detailLat=28.2266694&detailLon=-82.1556453&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(),
        AircraftInfo(),
    )

    SKYDIVE_COSTAL_CAROLINAS = (
        "scc",
        "Skydive Coastal Carolinas",
        "ILM/86,54",
        AirportAndWeatherIdentifiers("KSUT", "KSUT"),
        GeoLocation("33.9308156", "-78.0733636"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=33.9308156&lng=-78.0733636&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=2521",
        "https://embed.windy.com/embed2.html?lat=33.9308156&lon=-78.0733636&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Coastal Carolinas Website",
                url="https://www.skydivecoastalcarolinas.com",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_INDIANAPOLIS = (
        "sdi",
        # https://api.weather.gov/points/lat,long
        "Skydive Indianapolis",
        "IND/43,91",
        AirportAndWeatherIdentifiers("KFKR", "KFKR"),
        GeoLocation("40.2734308", "-86.5621703"),
        Calendars(
            # fullFrameUrl="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FDenver&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=1&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showTz=0",
            # dayFrameUrl=f"https://calendar.google.com/calendar/u/0/embed?height=110&wkst=1&bgcolor=%23ffffff&ctz=America/Boise&src=c2t5ZGl2ZXV0YWguY29tX28xbGE0NTcxMXQ0MHBkbzVsbGtvNTF1ajRnQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=c2t5ZGl2ZXV0YWguY29tX2ZjcWM2Zmk0M2pqZ2tzNzBna2t2dmxuY2tjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23E4C441&color=%232276b9&showTitle=0&showNav=0&showDate=0&showPrint=0&showTabs=0&showCalendars=0&showTz=0&mode=day",
        ),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.2734308&lng=-86.5621703&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=36",
        "https://embed.windy.com/embed2.html?lat=40.2734308&lon=-86.5621703&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Indianapolis Website",
                url="https://www.skydiveindianapolis.com/en/welcome",
            ),
        ),
        AircraftInfo(),
    )
    DES_MOINES_SKYDIVERS = (
        "dms",
        "Des Moines Skydivers",
        "DMX/91,36",
        AirportAndWeatherIdentifiers("KOXV", "KOXV"),
        GeoLocation("41.2990969", "-93.1137428"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.2990969&lng=-93.1137428&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=47",
        "https://embed.windy.com/embed2.html?lat=41.2990969&lon=-93.1137428&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Des Moines Skydivers Website",
                url="https://www.desmoinesskydivers.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_PHILADELPHIA = (
        "sdp",
        "Skydive Philadelphia",
        "PHI/43,95",
        AirportAndWeatherIdentifiers("KCKZ", "KCKZ"),
        GeoLocation("40.3891944", "-75.2904722"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=40.3891944&lng=-75.2904722&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=47",
        "https://embed.windy.com/embed2.html?lat=40.3891944&lon=-75.2904722&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Philadelphia Website",
                url="https://www.skydivephiladelphia.com/",
            ),
        ),
        AircraftInfo(),
    )
    JUMP_TN = (
        "jtn",
        "Jump TN",
        "MRX/110,65",
        AirportAndWeatherIdentifiers("KGCY", "KGCY"),
        GeoLocation("36.1957222", "-82.8113611"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=36.1957222&lng=-82.8113611&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=230",
        "https://embed.windy.com/embed2.html?lat=36.1957222&lon=-82.8113611&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Jump TN Website",
                url="https://jumptn.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_CAROLINAS = (
        "sca",
        "Skydive Carolina",
        "GSP/108,44",
        AirportAndWeatherIdentifiers("KDCM", "KDCM"),
        GeoLocation("34.7893333", "-81.1957778"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=34.7893333&lng=-81.1957778&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=256",
        "https://embed.windy.com/embed2.html?lat=34.7893333&lon=-81.1957778&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Carolina Website",
                url="https://www.skydivecarolina.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_MONROE = (
        "sdm",
        "Skydive Monroe",
        "FFC/76,90",
        AirportAndWeatherIdentifiers("KD73", "KD73"),
        GeoLocation("33.7825278", "-83.6928056"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=33.7825278&lng=-83.6928056&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=261",
        "https://embed.windy.com/embed2.html?lat=33.7825278&lon=-83.6928056&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Monroe Website",
                url="https://skydivemonroe.com/",
            ),
        ),
        AircraftInfo(aircraftRegistraionNumber="N9059S", aircraftIcao="AC8563"),
    )
    PIEDMONT_SKYDIVING = (
        "psd",
        "Piedmont Skydiving",
        "GSP/129,85",
        AirportAndWeatherIdentifiers("KRUQ", "KRUQ"),
        GeoLocation("35.6458833", "-80.5202917"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=35.6458833&lng=-80.5202917&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=292",
        "https://embed.windy.com/embed2.html?lat=35.6458833&lon=-80.5202917&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Piedmont Skydiving Website",
                url="https://piedmontskydiving.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_ORANGE = (
        "sdo",
        "Skydive Orange",
        "LWX/65,38",
        AirportAndWeatherIdentifiers("KOMH", "KOMH"),
        GeoLocation("38.2472028", "-78.0456211"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=38.2472028&lng=-78.0456211&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=390",
        "https://embed.windy.com/embed2.html?lat=38.2472028&lon=-78.0456211&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Orange Website",
                url="https://www.skydiveorange.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_WINDY_CITY_CHICAGO = (
        "swc",
        "Skydive Windy City Chicago",
        "IWX/10,63",
        AirportAndWeatherIdentifiers("KMGC", "KMGC"),
        GeoLocation("41.7033153", "-86.8212400"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.7033153&lng=-86.8212400&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=12691",
        "https://embed.windy.com/embed2.html?lat=41.7033153&lon=-86.8212400&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Windy City Chicago Website",
                url="https://skydivewindycitychicago.com/",
            ),
        ),
        AircraftInfo(),
    )
    SKYDIVE_CENTER_SAN_ANTONIO = (
        "csa",
        "Skydive Castroville",
        "EWX/113,51",
        AirportAndWeatherIdentifiers("KCVB", "KCVB"),
        GeoLocation("29.3423889", "-98.8512222"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=29.3423889&lng=-98.8512222&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=8681",
        "https://embed.windy.com/embed2.html?lat=29.3423889&lon=-98.8512222&detailedLat=29.3423889&detailedLon=-98.8512222&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Skydive Castroville Website",
                url="https://skydivecastroville.com/",
            ),
        ),
        AircraftInfo(),
    )

    # Andy Marcoux, GM: andy@skydivedanielson.com, 508-298-8504
    SKYDIVE_DANIELSON = (
        "skd",
        "Skydive Danielson",
        "BOX/47,61",
        AirportAndWeatherIdentifiers("KLZD", "KIJD"),
        GeoLocation("41.82", "-71.90"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.82&lng=-71.90&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=4661&display_menu=1",
        "https://embed.windy.com/embed2.html?lat=41.82&lon=-71.90&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(title="Website", url="https://www.skydivedanielson.com"),
            instagram=Link(
                title="Instagram", url="https://www.instagram.com/skydivedanielson/"
            ),
            facebook=Link(
                title="Facebook", url="https://www.facebook.com/SkydiveDanielson/"
            ),
        ),
        AircraftInfo(aircraftRegistraionNumber="N895SF", aircraftIcao="AC597D"),
    )

    # # arnett.daniel@gmail.com
    CLEVELAND_SKYDIVING_CENTER = (
        "csk",
        "Cleveland Skydiving Center",
        # https://api.weather.gov/points/lat,lng
        "CLE/104,61",
        # https://metar-taf.com/
        AirportAndWeatherIdentifiers("K7D8", "KPOV"),
        GeoLocation("41.3511658", "-81.0995414"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.3511658&lng=-81.0995414&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=3481&display_menu=1",
        "https://embed.windy.com/embed2.html?lat=41.3511658&lon=-81.0995414&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            instagram=Link(
                title="Instagram",
                url="https://www.instagram.com/clevelandskydivingcenter/",
            ),
        ),
        # https://globe.adsbexchange.com/
        AircraftInfo(),
    )

    # # events@skydivesuffolk.com
    SKYDIVE_SUFFOLK = (
        "sds",
        "Skydive Suffolk",
        # https://api.weather.gov/points/lat,lng
        "AKQ/80,43",
        # https://metar-taf.com/
        AirportAndWeatherIdentifiers("KSFQ", "KSFQ"),
        GeoLocation("36.6828884", "-76.5996232"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=36.6828884&lng=-76.5996232&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=1421&display_menu=1",
        "https://embed.windy.com/embed2.html?lat=36.6828884&lon=-76.5996232&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            web=Link(
                title="Website",
                url="https://skydivesuffolk.com/",
            ),
            facebook=Link(
                title="Facebook",
                url="https://www.facebook.com/groups/446324455546456/",
            ),
        ),
        # https://globe.adsbexchange.com/
        # TODO N893MM, N716MM, N750XL, NII28L
        AircraftInfo(),
    )

    # # brett.mickelson@gmail.com
    SKYDIVE_CONNECTICUT_PARACHUTISTS_INC = (
        "cpi",
        "Connecticut Parachutists, Inc.",
        "BOX/28,62",
        AirportAndWeatherIdentifiers("K7B9", "KBDL"),
        GeoLocation("41.922176", "-72.4582421"),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=41.922176&lng=-72.4582421&labels=true",
        # "https://displays.skydivect.net/manifest",  # TODO manifest link is not burble
        None,
        "https://embed.windy.com/embed2.html?lat=41.922176&lon=-72.4582421&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            instagram=Link(
                title="Instagram", url="https://www.instagram.com/skydivecpi/"
            )
        ),
        # TODO N6193B, N8097F, N90JF icao from https://globe.adsbexchange.com/
        AircraftInfo(),
    )

    # clarkeairsports@gmail.com
    NEW_ENGLAND = (
        "sne",
        "Skydive New England",
        "GYX/56,42",
        AirportAndWeatherIdentifiers("ME64", "KDAW"),
        GeoLocation("43.3750814", "-70.9292286"),
        # Calendars(
        #     # TODO LINKS
        #     dayFrameUrl="https://www.google.com/calendar/render?cid=webcal%3A%2F%2Fwww.skydivenewengland.com%2F%3Fpost_type%3Dtribe_events%26ical%3D1%26eventDisplay%3Dlist",
        #     fullFrameUrl="https://www.google.com/calendar/render?cid=webcal%3A%2F%2Fwww.skydivenewengland.com%2F%3Fpost_type%3Dtribe_events%26ical%3D1%26eventDisplay%3Dlist",
        # ),
        Calendars(),
        Cameras(),
        "https://www.radarbox.com/?widget=1&z=10&lat=43.3750814&lng=-70.9292286&labels=true",
        "https://dzm.burblesoft.com/jmp?dz_id=2921&_ga=2.27996732.1091037565.1715708886-605153076.1715708886&_gl=1*1djgtiv*_ga*NjA1MTUzMDc2LjE3MTU3MDg4ODY.*_ga_1W3J6BGX7Y*MTcxNTcwODg4NS4xLjEuMTcxNTcwOTA0Ny4wLjAuMA..",  # TODO manifest link is not burble
        "https://embed.windy.com/embed2.html?lat=43.3750814&lon=-70.9292286&width=650&height=450&zoom=9&level=surface&overlay=radar&product=radar&menu=&message=true&marker=&calendar=12&pressure=&type=map&location=coordinates&detail=true&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1",
        Socials(
            instagram=Link(
                title="Instagram", url="https://www.instagram.com/skydivenewengland/"
            ),
            web=Link(
                title="Skydive New England Homepage",
                url="https://www.skydivenewengland.com",
            ),
            facebook=Link(
                title="Funjumpers Facebook Group",
                url="https://www.facebook.com/groups/548448901928817",
            ),
        ),
        AircraftInfo(aircraftIcao="ABF580", aircraftRegistraionNumber="N87RM"),
    )
