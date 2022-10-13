#!/usr/bin/python3
"""Base class module"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == '__class__':
                    continue
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Prints string representation of class like this:
        [<class name>] (<self.id>) <self.__dict__>"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates instance of class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        instance_dict = dict(self.__dict__)
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = type(self).__name__
        return instance_dict
