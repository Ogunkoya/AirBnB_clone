#!/usr/bin/python3
"""
This is the console base for the unit
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
import models
import json

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """ Holberton command prompt to access models data """
    prompt = "(hbnb)"


    def do_quit(self, arg):
        """ Close program and saves safely data """
        return True

    def do_EOF(self, arg):
        """ Close program and saves safely data, when user input is CTRL + D"""
        print("")
        return True

    def emptyline(self):
        " Does  not perform any action"
        pass

    def do_create(self, args):
        """
        create a new instance - Usage: create <Classname>\n
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            if args in classes:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        show the representative of an instance - Usage show <classname>\n
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            lin = args.split()
            if lin[0] in classes:
                if len(lin) < 2:
                    print("** instance id missing **")
                else:
                    obj = models.storage.all()
                    key = str(lin[0]) + "." + str(lin[1])
                    if key in obj:
                        print(obj[key])
                    else:
                        print("** no instance found **")
            else:
                    print("** class doesn't exist **")

    def do_destory(self, args):
        """
        Delete the instance of a given class - 
        usage: destory <classname> <id>\n
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            lin = args.split()
            if lin[0] in classes:
                if len(lin) < 2:
                    print("** instance id missing **")
                else:
                    obj = models.storage .all()
                    key = str(lin[0]) + "." + str(lin[1])
                    if key in obj:
                        del(obj[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        print all instance of a class - usage : all <classname>\n
        """
        obj = models.storage.all()
        objList = []
        if args is "":
            for key in obj:
                objList.append(str(obj[key]))
            print(objList)
        else:
            try:
                lin = args.split()
                eval(lin[0])
                for elem in obj:
                    aux = obj[elem].to_dict()
                    if aux['__class__'] == lin[0]:
                        objList.append(str(obj[elem]))
                print(objList)
            except:
                print("** class doesn't exist **")

    def do_update(self, args):
        """
        Update or set att in instance - 
        Usage: Update <classname> <id> <att_name> <att_value>\n
        """
        lin = shlex.split(args)
        if len(lin) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(lin[0]))
            except:
                print("** calls doesn't exist **")
                return
            if len(lin) == 1:
                print("** instance id missing **")
            else:
                obj = models.storage.all()
                key = str(lin[0]) + "." + str(lin[1])
                if key not in obj:
                    print("** no instance found **")
                else:
                    if len(lin) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(lin) == 2:
                            print("** value missing **")
                        else:
                            if len(lin) == 3:
                                print("** value missing **")
                            else:
                                setattr(obj[key], lin[2], lin[3])
                                models.storage.save()

if __name__ == '__main__':
    """ Main """
    HBNBCommand().cmdloop()
