#!/usr/bin/python3
"""Console module"""


import cmd
from models import BaseModel, storage


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
        """"""
        if arg[0] == 'BaseModel':
            storage.__objects.append(BaseModel().to_dict())

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
