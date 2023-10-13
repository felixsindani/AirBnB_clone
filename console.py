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

    def do_eof(self, arg):
        """  Function do_EOF has a return value of True. Type Ctrl-D to drop out of the interpreter """
        print('')
        exit()

    def emptyline(self):
        """ creates new line after pressing enter when no command is passed as argument
        """
        pass
    
    def do_create(self, arg):
        """ Create new instance """
        if len(arg) == 0:
            # checks if argument is not supplied
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            # splits the string arguments into a list of words by checking whitespace
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    # checks if the single item in arg_list exists
                    # as a key in the self.classes dictionary
                    new = self.classes[arg]()
                    # creates an instance of the class associated with the key arg
                    # in the self.classes dictionary.
                    new.save()  # invoking save()
                    print(new.id)  # prints the id attribute of the newly created object
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance based on a given argument arg.
         ensure that the input is valid and that the requested class and instance exist """
        if len(arg) == 0:
            print('** class name missing **')  # error message when no class name(arg) is supplied
            return
        elif arg.split()[0] not in self.classes:
            # checks if the arg is not in the self.classes dictionary
            print("** class doesn't exist **")
            #  error message indicating that the provided class name is not recognized
            return
        elif len(arg.split()) > 1:
            # checks if there are more than one word in the split arg
            key = arg.split()[0] + '.' + arg.split()[1]  # creating key
            if key in storage.all():  # checks if the key exists in storage.all() data structure
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')
            
    def do_all(self, arg):
        """ Method to print all instances.
         Prints all string representation of all instances based or not on the class name """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])
            
    def do_update(self, arg):
        """ Method to update JSON file,based on the class name and id. Save the change into the JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            # no input from user
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            # checks if the first word in arg (the class name) is not in the self.classes dictionary
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            # checks if the length of arg is 1,user didn't provide an instance ID
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                # check if key is in dictionary
                if len(arg) > 2:  # checking if all arguments are supplied
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        # set attributes of the object
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')
                # error message if key is not found in dict

    def do_destroy(self, arg):
        """ Method to delete instance with class name and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except exception:
            # handles unrecognized class name provided by user
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            #  error message indicating that the user didn't provide an instance ID
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                # checks if key exists in storage.all()
                storage.all().pop(key)
                # If it does, it removes the object associated with key from the storage.all() dictionary
                storage.save()
                # using the pop method, and then it saves the updated storage back to a file
            else:
                print('** no instance found **')
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()