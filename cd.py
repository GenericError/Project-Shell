""" Module that executes the cd command """
import os  # Importing this module to do directory things
import argparse
from shellexceptions import *

def run_command(argument_list):
    """ Runs the cd command """
    amount_required = 1
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return
    new_directory = ""
    for i in argument_list:
        if not i.startswith("-"):
            new_directory = i
            break
    directory_to_go = os.path.join(os.getcwd(), new_directory)
    try:
        if new_directory == "":  # If the user put in a nothing or a space
            raise BlankDirectoryException
        elif new_directory == "~":  # If the user wants to go to the home folder
            os.chdir(os.path.expanduser('~'))  # Goes to the folder
        # If the argument does not give a valid directory
        elif not os.path.isdir(directory_to_go):
            raise NotADirectoryException(new_directory)
    except GenericException as e:
        e.print_error()
    except BlankDirectoryException as e:
        e.print_error()
    except NotADirectoryException as e:
        e.print_error()
    if os.path.isdir(directory_to_go):  # If it is a valid directory
        os.chdir(directory_to_go)  # Change the current directory
    return None  # Go back to the prompt
