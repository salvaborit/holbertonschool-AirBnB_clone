#!/usr/bin/python3
"""Console module"""


import cmd
from sys import argv
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
                    storage_d = storage.all()
                    instance = storage_d[f'{argv[0]}.{argv[1]}']
                    print(instance)
                except:
                    print('** no instance found **')
                    return
            except:
                print('** class doesn\'t exist **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        argv = arg.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif len(argv) == 1:
            print('** instance id missing **')
        else:
            try:
                eval(argv[0])()
                try:
                    del storage.all()[f'{argv[0]}.{argv[1]}']
                    storage.save()
                except:
                    print('** no instance found **')
                    return
            except:
                print('** class doesn\'t exist **')

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        argv = arg.split()
        instance_l = []
        if len(argv) == 0:
            print(storage.all())
        else:
            try:
                eval(argv[0])
                for key in storage.all():
                    key_d = key.split('.')
                    if key_d[0] == str(argv[0]):
                        instance_l.append(str(storage.all()[key]))
                print(instance_l)
            except:
                print('** class doesn\'t exist **')

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        argv = arg.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif len(argv) == 1:
            print('** instance id missing **')
        elif len(argv) == 2:
            print('** attribute name missing **')
        elif len(argv) == 3:
            print('** value missing **')
        else:
            try:
                eval(argv[0])
            except:
                print('** class doesn\'t exist **')
                return
            inst_found = False
            for obj_id, obj in storage.all().items():
                if obj_id == f'{argv[0]}.{argv[1]}':
                    setattr(obj, argv[2], argv[3])
                    inst_found = True
            if inst_found is False:
                print('** no instance found **')

    def inst_validator(self, inst_name, inst_id):
        """Checks if an instance/id pair exists and logs in a dict"""
        dict = {}
        try:
            eval(inst_name)
            dict['class'] = True
            try:
                storage_dict = storage.all()
                instance = storage_dict[f'{inst_name}.{inst_id}']
                dict['id'] = True
            except:
                dict['id'] = False
        except:
            dict['class'] = False
        return dict

if __name__ == '__main__':
    HBNBCommand().cmdloop()
