#!/usr/bin/python3
""" AirBnB clone - The console """
import cmd
import sys
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.review import review

class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class
    """
    intro = "Example of Simple command processor"
    prompt = '(hbnb): '
    doc_header = 'Documented Help Topics'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    ruler = '.'
    
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'review': review,
               'State': State}

    def do_quit(self, arg):
        """ Type quit to close/exit the session """
        exit()

    def do_EOF(self, arg):
        """  Function do_EOF has a return value of True. Type Ctrl-D to drop out of the interpreter """
        print('')
        exit()

    def emptyline(self):
        """ creates new line after pressing enter when no command is passed as argument
        """
        pass