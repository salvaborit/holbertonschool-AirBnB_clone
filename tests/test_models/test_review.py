#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing review"""
    def test_reviewclass(self):
        my_model = Review()
        self.assertTrue(type(my_model.text) is str)

if __name__ == "__main__":
    unittest.main()
