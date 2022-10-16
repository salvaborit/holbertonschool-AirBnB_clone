#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing user"""
    def test_userclass(self):
        my_model = User()
        self.assertTrue(type(my_model.email) is str)
        self.assertTrue(type(my_model.password) is str)
        self.assertTrue(type(my_model.first_name) is str)
        self.assertTrue(type(my_model.last_name) is str)

if __name__ == "__main__":
    unittest.main()
