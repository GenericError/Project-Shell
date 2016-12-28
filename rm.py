""" Module which contains the rm command """

import os  # Importing this for system operations and directory things
from shellexceptions import *


def run_command(argument_list):
    """ Function which runs the rm command """
    amount_required = 1
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return

    delete_query = ""
    for i in argument_list:
        if not i.startswith("-"):
            delete_query = i
            break

    # If the user isn't trying to delete all files with
    # a certain extension (hence the wildcard)
    if not delete_query.startswith("*"):
        try:  # Try to do the following
            # Try to delete the directory
            os.remove(delete_query)
        # In case the user tried to complete this operation on folders
        except OSError as e:
            try:
                raise InvalidOperationForDirectoriesException
            except InvalidOperationForDirectoriesException as new_e:
                new_e.print_error()
                return None
        except Exception as e:  # If another error occured
            try:
                raise GenericException
            except GenericException as new_e:
                new_e.print_error()
                return None
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
                        print(thing, "deleted.")  # Tell the user it's gone
                        return None  # Go back to the prompt
                    else:  # Otherwise, if it is a directory
                        continue  # Move on to the next file/folder in the dir
                except Exception as e:  # If an error occured
                    try:
                        raise FileCouldNotBeDeletedException(thing)
                    except FileCouldNotBeDeletedException as new_e:
                        new_e.print_error()
                        return None
    return None  # Go back to the prompt
