#!/usr/bin/python3
"""FileStorage module"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.amenity import Review


class FileStorage():
    """class: FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns '__objects' dict"""
        return self.__objects

    def new(self, obj):
        """Sets a new key(obj type)/pair(obj) value
        in '__objects' dict."""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: __file_path)"""
        serializeable_objects = {}
        for key in self.__objects:
            serializeable_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serializeable_objects, file)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except:
            pass
