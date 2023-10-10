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