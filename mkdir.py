""" Module which contains the mkdir command """

import os  # Importing this for directory things
from shellexceptions import *


def run_command(argument_list):
    """ Function which executes the mkdir command """
    amount_required = 1
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return

    new_directory_name = None
    for i in argument_list:
        if not i.startswith("-"):
            new_directory_name = i
            break

    try:
        os.mkdir(path=new_directory_name)
    except FileExistsError as e:
        new_e = DirectoryAlreadyExistsException(new_directory_name)
        new_e.print_error()
    except GenericException as e:
        e.print_error()
    except DirectoryNameNotSuppliedException as e:
        e.print_error()
    return None
