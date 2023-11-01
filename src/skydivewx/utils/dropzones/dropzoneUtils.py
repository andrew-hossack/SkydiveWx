class Calendars:
    def __init__(
        self,
        fullFrameUrl: str = None,
        dayFrameUrl: str = None,
        externalLink: str = None,
    ) -> None:
        if not (
            (((fullFrameUrl and dayFrameUrl) or externalLink))
            or ((not fullFrameUrl) and (not dayFrameUrl) and (not externalLink))
        ):
            raise TypeError(
                "Calendars needs either fullFrameUrl and dayFrameUrl or externalLink or all none"
            )
        self.fullFrameUrl = fullFrameUrl
        self.dayFrameUrl = dayFrameUrl
        self.externalLink = externalLink

    def get(self) -> dict:
        return {
            "fullFrameUrl": self.fullFrameUrl,
            "dayFrameUrl": self.dayFrameUrl,
            "externalLink": self.externalLink,
        }


class Cameras:
    def __init__(self, friendly_title: str = None, url: str = None) -> None:
        if friendly_title and url:
            self.camera_data = [{"friendly_title": friendly_title, "url": url}]

    def add(self, friendly_title: str, url: str) -> "Cameras":
        self.camera_data.append({"friendly_title": friendly_title, "url": url})
        return self

    def get(self) -> (dict, None):
        try:
            self.camera_data
        except AttributeError:
            # No cameras loaded
            return None
        return self.camera_data


class Link:
    def __init__(self, title: str = None, url: str = None, icon: str = None):
        self.url = url
        self.title = title
        self.icon = icon

    def get(self) -> dict:
        return {"title": self.title, "url": self.url, "icon": self.icon}


class Socials:
    def __init__(
        self,
        web: Link = None,
        twitter: Link = None,
        facebook: Link = None,
        youTube: Link = None,
        tiktok: Link = None,
        instagram: Link = None,
        email: Link = None,
    ):
        self.web = web
        self.twitter = twitter
        self.facebook = facebook
        self.youTube = youTube
        self.tikTok = tiktok
        self.instagram = instagram
        self.email = email

    def get(self) -> list[Link]:
        # Add default icons and titles
        if self.web:
            self.web.icon = "mdi:web"
            if not self.web.title:
                self.web.title = "Website"
        if self.twitter:
            raise NotImplementedError("todo icon")
            self.twitter.icon = None
            if not self.twitter.title:
                self.twitter.title = "Twitter"
        if self.facebook:
            self.facebook.icon = "ic:baseline-facebook"
            if not self.facebook.title:
                self.facebook.title = "Facebook"
        if self.youTube:
            self.youTube.icon = "mdi:youTube"
            if not self.youTube.title:
                self.youTube.title = "YouTube"
        if self.instagram:
            self.instagram.icon = "mdi:instagram"
            if not self.instagram.title:
                self.instagram.title = "Instagram"
        if self.email:
            self.email.icon = "fontisto:email"
            if not self.email.title:
                self.email.title = "Email"
        if self.tikTok:
            self.tikTok.icon = "ic:baseline-tiktok"
            if not self.tikTok.title:
                self.tikTok.title = "TikTok"
        return [
            self.web,
            self.twitter,
            self.facebook,
            self.youTube,
            self.tikTok,
            self.instagram,
            self.email,
        ]


class DropzoneType:
    def __init__(
        self,
        id: str,
        friendlyName: str,
        weatherGovGridpointLocation: str,
        airportIdentifier: str,
        latitude: str,
        longitude: str,
        calendars: Calendars,
        cameras: Cameras,
        radarBoxUrl: str,
        liveManifestUrl: str,
        weatherRadariFrameUrl: str,
        socials: Socials,
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
        self.socials = socials

    @classmethod
    def get_dropzone_by_id(self, dropzone_id: str) -> ("DropzoneType", None):
        for dropzone in self:
            if dropzone.value[0] == dropzone_id:
                return dropzone
        return None
