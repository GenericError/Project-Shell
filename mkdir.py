""" Module which contains the mkdir command """

import os  # Importing this for directory things
from shellexceptions import *


def run_command(options, arguments):
    """ Function which executes the mkdir command """
    return_code = 0
    try:
        new_directory_name = arguments[0]
    except:
        print('No directory name was supplied!')
        return_code = 1
        return return_code

    verbose = False
    for option in options:
        if option[0] in "-v":
            verbose = True

    try:
        os.mkdir(path=new_directory_name)
        if verbose:
            print("mkdir: created directory '"+new_directory_name+"'")
    except FileExistsError as e:
        new_e = DirectoryAlreadyExistsException(new_directory_name)
        new_e.print_error()
    except GenericException as e:
        e.print_error()
        return_code = 1
    except DirectoryNameNotSuppliedException as e:
        e.print_error()
        return_code = 1
    return return_code
