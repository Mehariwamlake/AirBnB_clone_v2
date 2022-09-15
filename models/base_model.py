#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a base class for all models in our hbnb clone"""
from email.policy import default
from tkinter.tix import COLUMN
from tokenize import String
=======
"""This is the base model class for AirBnB"""
>>>>>>> refs/remotes/origin/main
import uuid
import models
import os
from datetime import datetime
<<<<<<< HEAD
from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

=======
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


>>>>>>> refs/remotes/origin/main
Base = declarative_base()


class BaseModel:
<<<<<<< HEAD
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
=======
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

>>>>>>> refs/remotes/origin/main
    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs and "id" not in self.__dict__:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        elif kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
<<<<<<< HEAD
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
=======
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
>>>>>>> refs/remotes/origin/main

            else:
                self.updated_at = datetime.now()
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            else:
                self.created_at = datetime.now()
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)
            
    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    def delete(self):
        #public instance method to delete the current instance from the storage
        from models import storage
        storage.delete(self)
=======
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """

        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Delete current instance of storage"""
        models.storage.delete(self)
>>>>>>> refs/remotes/origin/main
