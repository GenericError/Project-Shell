""" Module that performs the cp command """

import shutil  # Import this for copyying files with metadata
import os  # Import this for system things
from shellexceptions import *
from permission_awareness import check_existence

MAN_DOC = """cp - copy files
Usage: cp [-v] source_file destination_file

cp copies the source_file to the destination_file
cp can only copy files; folders are not supported

If the -v flag is present, cp will be verbose"""

def run_command(options, arguments):
    """ Function that runs the acutal command based on the user's input """
    return_code = 0
    try:
        source = os.path.abspath(arguments[0])
        destination = os.path.abspath(arguments[1])
    except IndexError:
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

    try:
        if check_existence(source):
            pass
        else:
            raise SourceDoesNotExistException
        if check_existence(destination):
            pass
        else:
            raise DestinationDoesNotExistException
    except SourceDoesNotExistException as e:
        e.print_error()
        return_code = 7
        return return_code
    except DestinationDoesNotExistException as e:
        e.print_error()
        return_code = 8
        return return_code

    try:
        if source == destination:  # If the source and the destination are the same
            raise SourceDestinationAreEqualException
        elif os.path.isdir(source):  # If the source argument is a directory
            raise SourceArgumentIsADirectoryException
        elif os.path.isfile(source):  # If the source is a file
            if not os.path.isdir(destination):
                if os.path.exists(destination):  # If the destination exists
                    override = input("Override "+destination+" with "+source+" ? [y/N] ")
                    if override.lower().startswith("y"):
                        try:  # Try to do the following
                            # Copy the source to the destination with metadata
                            shutil.copy2(source, destination)
                            if verbose:
                                print(source, "->", destination)
                        except OSError:  # In case an error occured
                            raise GenericException
                    else:
                        print(destination, "was not overwritten")
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
            else:
                raise DestinationArgumentIsADirectoryException
        else:  # In case the user tried to perform another operation
            print("It is a bug if the code gets here!")
        return return_code
    except UnsupportedOperationException as e:
        e.print_error()
        return_code = 2
    except GenericException as e:
        e.print_error()
        return_code = 3
    except SourceDestinationAreEqualException as e:
        e.print_error()
        return_code = 4
    except SourceArgumentIsADirectoryException as e:
        e.print_error()
        return_code = 5
    except DestinationArgumentIsADirectoryException as e:
        e.print_error()
        return_code = 6
    return return_code
