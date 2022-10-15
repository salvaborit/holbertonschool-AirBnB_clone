#!/usr/bin/python3
"""Console module"""


import cmd
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class: HBNBCommand"""

    prompt = "(hbnb) "

    def emptyline(self):
        """When input is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        exit()

    def do_create(self, arg):
        """Create command: saves an instance of a class to a JSON file"""
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except:
                print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Prints an instance's string representation
        based on class name and id"""
        argv = arg.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif len(argv) == 1:
            print('** instance id missing **')
        else:
            try:
                eval(argv[0])
                try:
                    storage_dict = storage.all()
                    instance = storage_dict[f'{argv[0]}.{argv[1]}']
                    print(instance)
                except:
                    print('** id doesn\'t exist **')
            except:
                print('** class doesn\'t exist **')

    def do_destroy(self, arg):
        """ """

    def do_all(self, arg):
        """ """

    def do_update(self, arg):
        """ """

    def inst_validator(self, arg):
        """Returns true if an ID corresponds to an existent
        instance in 'storage.__objects' exists"""
        arg

if __name__ == '__main__':
    HBNBCommand().cmdloop()
