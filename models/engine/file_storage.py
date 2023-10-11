#!/usr/bin/python3
""" creates a class FileStorage.
    Serialize instances to a JSON file,
    and deserializes from a JSON file to instances
"""
import json
import os
import uuid
from datetime import datetime


class FileStorage:
    """ class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"  # string - that stores path to the JSON file
    __objects = {}  # empty dictionary - that will store all objects by <class name>.id.

    def all(self):
        """ defines a method named 'all'.Retrieves the dictionary of objects/data stored in the FileStorage class """
        return FileStorage.__objects
    
    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        # allows us to add objects to the __objects dictionary with keys that are easy to identify and retrieve later
        # adds the obj to the __objects dictionary with a key that combines the object's class name
        # (retrieved using obj.__class__.__name__)
        # and its id attribute (converted to a string using str(obj.id)).
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj