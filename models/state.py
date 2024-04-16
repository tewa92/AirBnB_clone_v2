#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of CITY instances with STATE_ID
            equals the current STATE.ID
            FileStorage relationship between STATES AND CITY
            """
            related_cities = []
            cities = storage.all(city)
            for city in cities.value():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
