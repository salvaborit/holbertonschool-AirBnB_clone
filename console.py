#!/usr/bin/python3
"""Console module"""


import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
