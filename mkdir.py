""" Module which contains the mkdir command """

import os  # Importing this for directory things
from shellexceptions import *

MAN_DOC = """mkdir - make a directory
Usage: mkdir [-v] new_directory

Running mkdir with the -v flag present will make the command verbose.
A new directory will be created in the current working directory with the name of new_directory.
If a path to a pre-existing directory precedes new_directory (ie Desktop/new_directory), the new directory will be created in the preceding path under the name of new_directory"""

def run_command(options, arguments):
    """ Function which executes the mkdir command """
    try:
        new_directory_name = arguments[0]
    except:
        print('No directory name was supplied!')
        return None

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
    except DirectoryNameNotSuppliedException as e:
        e.print_error()
    return None
