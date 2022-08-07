#!/usr/bin/python3
"""Module to handle the flow of serialization-deserialization
<class 'BaseModel'> -> to_dict() -> <class 'dict'>
-> JSON dump -> <class 'str'> -> FILE -> <class 'str'>
-> JSON load -> <class 'dict'> -> <class 'BaseModel'>
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """class that effects storage and the flow of
    serialization-deserialization
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds obj (a dictionary element) to __objects"""
        class_name = obj.__class__.__name__
        class_id = obj.id
        key = class_name + "." + class_id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as myFile:
            json.dump(my_dict, myFile)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_to_dic = json.load(file)
                for val in json_to_dic.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))

        except FileNotFoundError:
            pass
