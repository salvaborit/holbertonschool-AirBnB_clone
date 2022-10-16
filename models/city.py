#!/usr/bin/python3
"""City module"""


from models.base_model import BaseModel


class City(BaseModel):
    """class: city (inherits from BaseModel)"""

    state_id = ""  # it will be the State.id
    name = ""
