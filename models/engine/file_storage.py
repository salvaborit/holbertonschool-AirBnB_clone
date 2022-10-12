#!/usr/bin/python3
"""FileStorage module"""


import json
from models.base_model import BaseModel


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
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: __file_path)"""
        serializeable_objects = {}
        for key in self.__objects:
            if type(self.__objects[key]) is dict:
                serializeable_objects[key] = self.__objects[key]
            else:
                serializeable_objects[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serializeable_objects, file)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
        except Exception:
            pass
