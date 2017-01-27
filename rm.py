""" Module which contains the rm command """

import os  # Importing this for system operations and directory things
from shellexceptions import *


def run_command(options, arguments):
    """ Function which runs the rm command """
    return_code = 0
    try:
        delete_query = arguments[0]
    except:
        try:
            raise FlagOrArgumentNotGivenException
        except FlagOrArgumentNotGivenException as e:
            e.print_error()
            return_code = 1
            return return_code
    verbose = False
    for option in options:
        if option[0] in "-v":
            verbose = True
    # If the user isn't trying to delete all files with
    # a certain extension (hence the wildcard)
    if not delete_query.startswith("*"):
        try:  # Try to do the following
            # Try to delete the file
            os.remove(delete_query)
            if verbose:
                print(str(os.path.abspath(delete_query)))
        # In case the user tried to complete this operation on folders
        except OSError as e:
            try:
                raise InvalidOperationForDirectoriesException
            except InvalidOperationForDirectoriesException as new_e:
                new_e.print_error()
                return_code = 1
                return return_code
        except Exception as e:  # If another error occured
            try:
                raise GenericException
            except GenericException as new_e:
                new_e.print_error()
                return_code = 1
                return return_code
    # If the user is trying to delete all files with a certain extension
    else:
        # Create a variable to hold the name of the extension
        # EG: If delete_query was "*.txt", then the variable
        # would now be reassigned to "txt"
        delete_query = delete_query.split("*.")[1]
        # For each file and folder in the current directory
        for thing in os.listdir(os.getcwd()):
            # If the thing ends with the file extension
            if thing.endswith(delete_query):
                try:  # Try to do the following
                    # If the thing is not a directory
                    if not os.path.isdir(thing):
                        os.remove(thing)  # Remove the file
                        if verbose:
                            print(str(os.path.abspath(thing)))
                    else:  # Otherwise, if it is a directory
                        continue  # Move on to the next file/folder in the dir
                except Exception as e:  # If an error occured
                    try:
                        raise FileCouldNotBeDeletedException(thing)
                    except FileCouldNotBeDeletedException as new_e:
                        new_e.print_error()
                        return_code = 1
                        return return_code
    return return_code  # Go back to the prompt
