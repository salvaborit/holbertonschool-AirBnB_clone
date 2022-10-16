#!/usr/bin/python3
"""Module Test Extra Classes"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing state"""
    def test_stateclass(self):
        my_model = State()
        self.assertTrue(type(my_model.name) is str)

if __name__ == "__main__":
    unittest.main()
