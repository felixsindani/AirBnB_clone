#!/usr/bin/python3
""" initialisation for class FileStorage
custom class responsible for handling data storage using files
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload() # method used to load data from the storage files into memory