""" Module that executes the cd command """
import os  # Importing this module to do directory things
import argparse
import getopt
from shellexceptions import *

def run_command(options, arguments):
    """ Runs the cd command """
    return_code = 0
    try:
        new_directory = arguments[0]
    except Exception:
        new_directory = "~"
    directory_to_go = os.path.join(os.getcwd(), new_directory)
    try:
        if new_directory == "~":  # If the user wants to go to the home folder
            os.chdir(os.path.expanduser('~'))  # Goes to the folder
        # If the argument does not give a valid directory
        elif not os.path.isdir(directory_to_go):
            raise NotADirectoryException(new_directory)
    except GenericException as e:
        e.print_error()
        return_code = 1
    except BlankDirectoryException as e:
        e.print_error()
        return_code = 1
    except NotADirectoryException as e:
        e.print_error()
        return_code = 1
    if os.path.isdir(directory_to_go):  # If it is a valid directory
        os.chdir(directory_to_go)  # Change the current directory
    return return_code  # Go back to the prompt
