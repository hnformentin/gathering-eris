import unittest
import json
from datetime import datetime

from location import WeatherInfo, Location


class TestWeatherInfo(unittest.TestCase):

    def load(self, fn):
        with open(fn) as json_file:
            data = json.load(json_file)
            return data

    def setUp(self) -> None:
        self.location = Location(location='Rotvoll', lat=63.4308, lon=10.4034)
        self.dry_case = self.load('dry.json')
        self.wet_case = self.load('wet.json')
        self.timepoint = datetime(2020, 10, 29, 15, 59, 0)

    def test_when_wet_10_minutes(self):
        info = WeatherInfo(self.location, self.wet_case, timepoint=self.timepoint)
        self.assertEqual(6, info.time_until_rain)

    def test_when_dry_90_minutes(self):
        info = WeatherInfo(self.location, self.dry_case, timepoint=self.timepoint)
        self.assertEqual(90, info.time_until_rain)
