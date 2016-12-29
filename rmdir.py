""" Module which includes the rmdir command """

import os  # Importing this for deletion and directory things
from shellexceptions import *

def run_command(argument_list):
    """ Function which runs the rmdir command"""
    amount_required = 1
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except Exception as e:
        try:
            raise FlagOrArgumentNotGivenException
        except FlagOrArgumentNotGivenException as new_e:
            new_e.print_error()
            return None

    directory_to_remove = ""
    for i in argument_list:
        if not i.startswith("-"):
            directory_to_remove = i
            break

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
