#!/usr/bin/python3

"""contains the entry point of the command interpreter"""
import cmd
from models import storage
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
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id
        """
        all_class_objects = storage.all()
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            given_class = arg_list[0] + "." + arg_list[1]
            for key in all_class_objects.keys():
                if given_class == key:
                    print(all_class_objects[key])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        all_class_objects = storage.all()
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg_list()
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            given_class = arg_list[0] + "." + arg_list[1]
            for key in all_class_objects.keys():
                if key == given_class:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name"""
        class_list = []
        check = False
        if not arg:
            for key in storage.all().keys():
                class_list.append("{}".format(storage.all()[key]))
        else:
            for key in storage.all().keys():
                class_name = key.split(".")[0]
                print(class_name, arg)
                if arg == class_name:
                    check = True
                    class_list.append("{}".format(storage.all()[key]))
            if check is False:
                print("** class doesn't exist **")
                return
        print(class_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        my_classes = storage.all()
        check = False
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        name_id = arg_list[0] + "." + arg_list[1]
        if name_id not in list(my_classes.keys()):
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[name_id], arg_list[2], arg_list[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
