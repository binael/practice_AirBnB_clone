#!/usr/bin/python3
"""A base model module that contains the base model class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A BaseModel class that defines all common attributes/methods
    for other classes
    ARGUMENTS:
        id: unique id generated when an instance is created
        created_at: datetime for when instance is created
        updated_at: datetime for when update is applied
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes public instance variables
        ARGUMENTS:
            id: unique id generated
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value,
                                                           format)
                else:
                    self.__dict__[key] = value
        models.storage.new(self)

    def __str__(self):
        """
        returns the string representation of the class instance of
        name, the id and the instance dictionary
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the datetime attribute 'updated_at' to
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        my_dict = {}

        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value

        my_dict["__class__"] = self.__class__.__name__

        return my_dict
