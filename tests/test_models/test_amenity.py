#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing amenity"""
    def test_amenityclass(self):
        my_model = Amenity()
        self.assertTrue(type(my_model.name) is str)

if __name__ == "__main__":
    unittest.main()
