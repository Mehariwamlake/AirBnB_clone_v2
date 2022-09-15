#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
import string
from tkinter import CASCADE
from models import city
from models.base_model import BaseModel,Base
from sqlalchemy import column, String, Integer, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    name = column(string(128), nullable=False)
    cities = relationship("city", backref="state",
                            CASCADE="all, delete-orphan"
    )

    @property
    def cities(self):
        # getter attribute cities that retutns the list of city
        from models import storage
        my_list =[]
        extracted_cities = storage.all(City).values()
        for city in extracted_cities:
            if self.id == City.state_id:
                my_list.append(City)
        return my_list
=======
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
# from models import storage
# from models import City
import os


class State(BaseModel, Base):
    """This is the class for State"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='delete')

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def all_cities(self):
            """
            getter for cities
            """
            cities = []
            insta = storage.all(City)
            for value in insta.values():
                if value.state_id == self.id:
                    cities.append(value)
            return cities
>>>>>>> refs/remotes/origin/main
