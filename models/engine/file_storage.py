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
        
    def save(self):
        """ serializes objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            #  opens the JSON file specified by the __file_path class variable
            #  in write mode ('w') with UTF-8 encoding
            #  with statement ensures that the file is properly closed after writing
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            # creates a new dictionary- new_dict
            # by iterating over the items in the __objects dictionary
            # calls a to_dict method on each object
            # convert objects to dictionaries before serializing them.
            json.dump(new_dict, fname)
            # uses the json.dump method to serialize the new_dict dictionary
            # write it to the JSON file specified by name