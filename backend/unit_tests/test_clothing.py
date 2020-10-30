import unittest
from backend.location import wardrobe_lookup


class TestClothing(unittest.TestCase):

    def test_when_windy_and_raining_stay_home(self):
        clothing = wardrobe_lookup(rain=6, wind=11, temp=10)
        self.assertGreaterEqual(clothing.find("homeoffice"), 0)
