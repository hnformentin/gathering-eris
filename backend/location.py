import json
from dataclasses import dataclass
from datetime import datetime

import requests

NOWCAST_URL = 'https://api.met.no/weatherapi/nowcast/2.0/complete?'


@dataclass
class NextHour:
    symbol_code: str = ""
    precipitation_amount: float = 0.0


@dataclass
class Location:
    location: str
    lat: float
    lon: float

    def met_nowcast(self):
        url = NOWCAST_URL + 'lat=' + str(self.lat) + '&lon=' + str(self.lon)
        return requests.get(url).content

    def nowcast(self):
        raw_nowcast = self.met_nowcast()
        decoded_nowcast = json.loads(raw_nowcast.decode())
        location_info = WeatherInfo(self, decoded_nowcast)
        return location_info


@dataclass
class WeatherInfo:
    location: str
    air_temperature: float
    precipitation_rate: float
    wind_speed: float
    time_until_rain: float = 0.0
    clothing: str = ""
    next_1_hour: NextHour = None

    def __init__(self, loc: Location, nowcast, timepoint=datetime.utcnow()):
        self.location = loc.location
        data_ = nowcast["properties"]["timeseries"][0]["data"]
        self.air_temperature = data_["instant"]["details"]["air_temperature"]
        self.precipitation_rate = data_["instant"]["details"][
            "precipitation_rate"]
        self.wind_speed = data_["instant"]["details"]["wind_speed"]
        next1hours = data_["next_1_hours"]
        self.next_1_hour = NextHour(next1hours["summary"]["symbol_code"], next1hours["details"]["precipitation_amount"])

        self.time_until_rain = self.minutes_until_rain(nowcast["properties"]["timeseries"], timepoint)

        self.clothing = self.wardrobe_lookup(rain=self.precipitation_rate, wind=self.wind_speed)

    def minutes_until_rain(self, ts_rain_rate, timepoint):
        for obj in ts_rain_rate:
            if datetime.fromisoformat(obj["time"].replace("Z", "")) > timepoint:
                if obj["data"]["instant"]["details"]["precipitation_rate"] > 0.0:
                    delta = datetime.fromisoformat(obj["time"].replace("Z", "")) - timepoint
                    return delta.seconds / 60
        return 90

    def wardrobe_lookup(self, rain: float, wind: float):
        # TODO: implement fancy algorithm
        return ("homeoffice")
