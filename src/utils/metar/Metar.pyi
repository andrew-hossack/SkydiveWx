from datetime import datetime, timedelta
from re import Match
from typing import Callable, List, Literal, Optional, Tuple, Union

from utils.metar.Datatypes import (
    direction,
    distance,
    precipitation,
    pressure,
    speed,
    temperature,
)

def xlate_loc(loc: str) -> str: ...
def _sanitize(code: str) -> str: ...
def _report_match(handler: Callable[[dict], None], match: Match) -> None: ...
def _unparsedGroup(self: "Metar", d: dict) -> None: ...

class ParserError(Exception): ...

class Metar:
    code: str
    type: Literal["METAR", "SPECI"]
    correction: Optional[str]
    mod: Literal["AUTO", "COR"]
    station_id: Optional[str]
    time: Optional[datetime]
    cycle: Optional[int]
    wind_dir: Optional[direction]
    wind_speed: Optional[speed]
    wind_gust: Optional[speed]
    wind_dir_from: Optional[direction]
    wind_dir_to: Optional[direction]
    vis: Optional[distance]
    vis_dir: Optional[direction]
    max_vis: Optional[distance]
    max_vis_dir: Optional[direction]
    temp: Optional[temperature]
    dewpt: Optional[temperature]
    press: Optional[pressure]
    runway: List[list]
    weather: List[Tuple[str, str, str, str, str]]
    recent: List[Tuple[str, str, str, str, str]]
    sky: List[Tuple[str, Optional[distance], str]]
    windshear: List[str]
    wind_speed_peak: Optional[speed]
    wind_dir_peak: Optional[direction]
    peak_wind_time: Optional[datetime]
    wind_shift_time: Optional[datetime]
    max_temp_6hr: Optional[temperature]
    min_temp_6hr: Optional[temperature]
    max_temp_24hr: Optional[temperature]
    min_temp_24hr: Optional[temperature]
    press_sea_level: Optional[pressure]
    precip_1hr: Optional[precipitation]
    precip_3hr: Optional[precipitation]
    precip_6hr: Optional[precipitation]
    precip_24hr: Optional[precipitation]
    snowdepth: Optional[distance]
    ice_accretion_1hr: Optional[precipitation]
    ice_accretion_3hr: Optional[precipitation]
    ice_accretion_6hr: Optional[precipitation]
    _trend: bool
    _trend_groups: List[str]
    _remarks: List[str]
    _unparsed_groups: List[str]
    _unparsed_remarks: List[str]
    _now: datetime
    month: int
    year: int

    def __init__(
        self,
        metarcode: str,
        month: Optional[int] = ...,
        year: Optional[int] = ...,
        utcdelta: Union[int, timedelta, None] = ...,
        strict: bool = ...,
    ): ...
    @property
    def decode_completed(self) -> bool: ...
    def _do_trend_handlers(self, code: str) -> str: ...
    def __str__(self) -> str: ...
    def _handleType(self, d: dict) -> None: ...
    def _handleCorrection(self, d: dict) -> None: ...
    def _handleStation(self, d: dict) -> None: ...
    def _handleModifier(self, d: dict) -> None: ...
    def _handleTime(self, d: dict) -> None: ...
    def _handleWind(self, d: dict) -> None: ...
    def _handleVisibility(self, d: dict) -> None: ...
    def _handleRunway(self, d: dict) -> None: ...
    def _handleWeather(self, d: dict) -> None: ...
    def _handleSky(self, d: dict) -> None: ...
    def _handleTemp(self, d: dict) -> None: ...
    def _handlePressure(self, d: dict) -> None: ...
    def _handleRecent(self, d: dict) -> None: ...
    def _handleWindShear(self, d: dict) -> None: ...
    def _handleColor(self, d: dict) -> None: ...
    def _handleRunwayState(self, d: dict) -> None: ...
    def _handleTrend(self, d: dict) -> None: ...
    def _startRemarks(self, d: dict) -> None: ...
    def _handleSealvlPressRemark(self, d: dict) -> None: ...
    def _handlePrecip24hrRemark(self, d: dict) -> None: ...
    def _handlePrecip1hrRemark(self, d: dict) -> None: ...
    def _handleTemp1hrRemark(self, d: dict) -> None: ...
    def _handleTemp6hrRemark(self, d: dict) -> None: ...
    def _handleTemp24hrRemark(self, d: dict) -> None: ...
    def _handlePress3hrRemark(self, d: dict) -> None: ...
    def _handlePeakWindRemark(self, d: dict) -> None: ...
    def _handleWindShiftRemark(self, d: dict) -> None: ...
    def _handleLightningRemark(self, d: dict) -> None: ...
    def _handleTSLocRemark(self, d: dict) -> None: ...
    def _handleAutoRemark(self, d: dict) -> None: ...
    def _handleSnowDepthRemark(self, d: dict) -> None: ...
    def _handleIceAccretionRemark(self, d: dict) -> None: ...
    def _unparsedRemark(self, d: dict) -> None: ...
    def string(self) -> str: ...
    def report_type(self) -> str: ...
    def wind(
        self,
        units: Literal["KT", "MPS", "KMH", "MPH", "kt", "mps", "kmh", "mph"] = ...,
    ) -> str: ...
    def peak_wind(
        self,
        units: Literal["KT", "MPS", "KMH", "MPH", "kt", "mps", "kmh", "mph"] = ...,
    ) -> str: ...
    def wind_shift(
        self,
        units: Literal["KT", "MPS", "KMH", "MPH", "kt", "mps", "kmh", "mph"] = ...,
    ) -> str: ...
    def visibility(
        self,
        units: Optional[
            Literal[
                "SM", "MI", "M", "KM", "FT", "IN", "sm", "mi", "m", "km", "ft", "in"
            ]
        ] = ...,
    ) -> str: ...
    def runway_visual_range(
        self,
        units: Optional[
            Literal[
                "SM", "MI", "M", "KM", "FT", "IN", "sm", "mi", "m", "km", "ft", "in"
            ]
        ] = ...,
    ) -> str: ...
    def present_weather(self) -> str: ...
    def recent_weather(self) -> str: ...
    def _weather(self, weather: list) -> str: ...
    def sky_conditions(self, sep: str = "; ") -> str: ...
    def trend(self) -> str: ...
    def remarks(self, sep: str = "; ") -> str: ...
