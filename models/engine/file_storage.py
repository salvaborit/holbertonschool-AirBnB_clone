#!/usr/bin/python3
"""FileStorage module"""


import json
import os.path


class FileStorage:
    """class: FileStorage"""

    def __init__(self):
        """Constructor"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns '__objects' dict"""
        return self.__objects

    def new(self, obj):
        """Sets a new key(obj type)/pair(obj) value
        in '__objects' dict."""
        obj_type_str = str(type(obj))
        self.__objects[obj_type_str] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
