#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.base_model import BaseModel


class TestIstantiation(unittest.TestCase):
    """Tests for regular instantiation"""

    def setUp(self):
        self.b = BaseModel()

    def test_save(self):
        """tests save() method"""
        init_timestamp = self.b.updated_at
        self.b.save()
        self.assertFalse(init_timestamp == self.b.updated_at)

    def test_dict(self):
        """tests to_dict() method"""
        self.assertTrue(type(self.b) is dict)

    def test_id(self):
        """tests id attribute"""
        self.assertTrue()


self.id
self.created_at
__str__
