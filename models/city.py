#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import relationship


class City(BaseModel, Base):
    """ The CITY class, contains STATE ID and NAME """
    __table__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('place', backref='cities', cascade = 'all, delete, delete-orphan')
    else:
        name = ''
        states_id = ''
