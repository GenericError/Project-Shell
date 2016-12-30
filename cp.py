""" Module that performs the cp command """

import shutil  # Import this for copyying files with metadata
import os  # Import this for system things
from shellexceptions import *


def run_command(options, arguments):
    """ Function that runs the acutal command based on the user's input """
    try:
        source = os.path.abspath(arguments[0])
        destination = os.path.abspath(arguments[1])
    except IndexError:
        try:
            raise FlagOrArgumentNotGivenException
        except FlagOrArgumentNotGivenException as e:
            e.print_error()
            return None
    verbose = False
    for option in options:
        if option[0] in "-v":
            verbose = True
    try:
        if source == destination:  # If the source and the destination are the same
            raise SourceDestinationAreEqualException
        elif os.path.isdir(source):  # If the source argument is a directory
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
                    if verbose:
                        print(source, "->", destination)
                except OSError:  # In case an error occured
                    raise GenericException
            else:  # In case something went wrong
                raise GenericException
        else:  # In case the user tried to perform another operation
            # TODO: Implement the appropriate actions here
            raise UnsupportedOperationException("cp")
        return None
    except UnsupportedOperationException as e:
        e.print_error()
    except GenericException as e:
        e.print_error()
    except SourceDestinationAreEqualException as e:
        e.print_error()
    except SourceArgumentIsADirectoryException as e:
        e.print_error()
    return None