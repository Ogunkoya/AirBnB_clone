#!/usr/bin/python3
"""
This is the console base for the unit
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Holberton command prompt to access models data """
    prompt = '(hbnb) '
    use_rawinput = False

    def do_quit(self, arg):
        """ Close program and saves safely data """
        return True

    def do_EOF(self, arg):
        """ Close program and saves safely data, when user input is CTRL + D"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
