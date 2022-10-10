#!/usr/bin/python3
"""Base class module"""

from uuid import uuid4
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        key_created_found = False
        key_updated_found = False
        datetime_format = '%Y-%d-%mT%H:%M:%S.%f'
        if kwargs:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(
                        kwargs[key], datetime_format)
                    key_created_found = True
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                        kwargs[key], datetime_format)
                    key_updated_found = True
                    continue
                self.key = kwargs[key]
        self.id = str(uuid4())
        if key_created_found is False:
            self.created_at = datetime.datetime.now()
        if key_updated_found is False:
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Prints string representation of class like this:
        [<class name>] (<self.id>) <self.__dict__>"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates instance of class"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        instance_dict = self.__dict__
        instance_dict['created_at'] = str(instance_dict.get(
            'created_at').isoformat())
        instance_dict['updated_at'] = str(instance_dict.get(
            'updated_at').isoformat())
        instance_dict['__class__'] = type(self).__name__
        return instance_dict