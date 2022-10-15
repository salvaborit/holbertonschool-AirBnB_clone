#!/usr/bin/python3
"""Console module"""


import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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
        """"""

    def do_destroy(self, arg):
        """"""

    def do_all(self, arg):
        """"""

    def do_update(self, arg):
        """"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
