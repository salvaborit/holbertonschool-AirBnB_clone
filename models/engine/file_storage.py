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
        obj_type_str = str(type(obj))
        self.__objects[obj_type_str] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: __file_path)"""
        serializable = {}
        for key in self.__objects:
            if self.is_serializeable(self.__objects[key]):
                serializable[key] = self.__objects[key].to_dict()
            else:
                serializable[key] = self.__objects[key]

        with open(self.__file_path, 'w') as file:
            json.dump(serializable, file)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        try:
            with open(self.__file_path) as file:
                self.__objects = dict(json.load(file))
        except Exception:
            pass

    def is_serializeable(self, obj):
        """Checks if an obj is serializeable"""
        serializeable = False
        serializeable_types = [dict, list, tuple,
                               str, int, float, False, True, None]
        for type in serializeable_types:
            if type(obj) is type:
                serializeable = True
        return serializeable
