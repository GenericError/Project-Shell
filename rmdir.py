""" Module which includes the rmdir command """

import os  # Importing this for deletion and directory things
from shellexceptions import *

def run_command(options, arguments):
    """ Function which runs the rmdir command"""
    try:
        directory_to_remove = arguments[0]
    except Exception:
        print('No directory was supplied!')
        return None
    directory_to_remove = os.path.join(os.getcwd(), directory_to_remove)
    try:  # Try to do the follwing
        os.rmdir(path=directory_to_remove)  # Remove the directory
    except OSError as e:
        try:
            raise DirectoryNotEmptyException
        except DirectoryNotEmptyException as new_e:
            new_e.print_error()
    except DirectoryNotEmptyException as e:
        e.print_error()
    except Exception as e:
        print("Hmmm, something went wrong?")
    return None
