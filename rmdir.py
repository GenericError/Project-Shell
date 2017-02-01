""" Module which includes the rmdir command """

import os  # Importing this for deletion and directory things
from shellexceptions import *

MAN_DOC = """rmdir - remove directories
Usage: rmdir directory

rmdir deletes an empty directory with the name of the directory specified.
Attempting to remove a non-empty directory will result in an error.
It is automatically assumed that the directory for deletion exists in the current working directory. If not, supply a full or relative path to the directory for removal."""

def run_command(options, arguments):
    """ Function which runs the rmdir command"""
    return_code = 0
    try:
        directory_to_remove = arguments[0]
    except Exception:
        print('No directory was supplied!')
        return_code = 1
        return return_code
    directory_to_remove = os.path.join(os.getcwd(), directory_to_remove)
    try:  # Try to do the follwing
        os.rmdir(path=directory_to_remove)  # Remove the directory
    except OSError as e:
        try:
            raise DirectoryNotEmptyException
        except DirectoryNotEmptyException as new_e:
            new_e.print_error()
            return_code = 1
    except DirectoryNotEmptyException as e:
        e.print_error()
        return_code = 1
    except Exception as e:
        print("Hmmm, something went wrong?")
        return_code = 1
    return return_code
