""" Module that performs the cp command """

import shutil  # Import this for copyying files with metadata
import os  # Import this for system things
from shellexceptions import *


def run_command(argument_list):
    """ Function that runs the acutal command based on the user's input """
    amount_required = 2

    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return

    source = None
    destination = None
    for i in argument_list:
        if not i.startswith("-"):
            if source is None:
                source = i
            else:
                destination = i

    try:
        if source == destination:  # If the source and the destination are the same
            raise SourceDestinationAreEqualException
        elif os.path.isdir(source):  # Im the source argument is a directory
            raise SourceArgumentIsADirectoryException
        elif os.path.isfile(source):  # If the source is a file
            if os.path.exists(destination):  # If the destination exists
                # TODO: Implement the appropriate actions here
                raise UnsupportedOperationException("cp")
            # If the destination does not exist
            elif not os.path.exists(destination):
                try:  # Try to do the following
                    # Copy the source to the destination with metadata
                    shutil.copy2(source, destination)
                except OSError:  # In case an error occured
                    raise GenericException
            else:  # In case something went wrong
                raise GenericException
        else:  # In case the user tried to perform another operation
            # TODO: Implement the appropriate actions here
            raise UnsupportedOperationException("cp")
        return None
    except UnsupportedOperationException as e:
        print(e.error_message)
    except GenericException as e:
        print(e.error_message)
    except SourceDestinationAreEqualException as e:
        print(e.error_message)
    except SourceArgumentIsADirectoryException as e:
        print(e.error_message)
    return None
