#!/usr/bin/python3

"""contains the entry point of the command interpreter"""
import cmd
from models import
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""


    __classes = ["BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"
                 ]

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do not execute"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) != 2:
            print("** instance id missing **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()
