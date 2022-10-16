#!/usr/bin/python3
"""Review module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class: Review (inherits from 'BaseModel')"""

    place_id = 0 # it will be the Place.id
    user_id = 0 # it will be the User.id
    text = ""
