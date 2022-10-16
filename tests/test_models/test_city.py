#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testing city"""
    def test_cityclass(self):
        my_model = City()
        self.assertTrue(type(my_model.name) is str)

if __name__ == "__main__":
    unittest.main()
