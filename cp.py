""" Module that performs the cp command """

import shutil  # Import this for copyying files with metadata
import os  # Import this for system things


def run_command(arguments):
    """ Function that runs the acutal command based on the user's input """

    # If the user supplied less than two arguments
    if len(arguments['more_input']) < 2:
        # Tell the user that they did so
        print("Source and/or destination arguments are required")
        return None  # Go back to the prompt
    # If the user supplied more than two arguments
    elif len(arguments['more_input']) > 2:
        # Tell the user that they did so
        print("Source and destination are the only required arguments")
        return None  # Go back to the prompt

    more_input = arguments['more_input']  # Grab the names of the directories
    source = more_input[0]  # Grab the source file name
    destination = more_input[1]  # Grab the destination file name

    if source == destination:  # If the source and the destination are the same
        print("The two given arguments can not be the same")  # Tell the user
        return None  # Go back to the prompt
    elif os.path.isdir(source):  # Im the source argument is a directory
        print("Error: the source argumnet is a directory!")  # Tell the user
        return None  # Go back to the prompt
    elif os.path.isfile(source):  # If the source is a file
        if os.path.exists(destination):  # If the destination exists
            # TODO: Implement the appropriate actions here
            # Tell the user that this function is not currently supported
            print("That operation is not currently supported by cp")
            return None  # Go back to the prompt
        # If the destination does not exist
        elif not os.path.exists(destination):
            try:  # Try to do the following
                # Copy the source to the destination with metadata
                shutil.copy2(source, destination)
            except OSError:  # In case an error occured
                print("Sorry, and error occured.")  # Tell the user
                return None  # Go back to the prompt
        else:  # In case something went wrong
            print("Sorry an error occured.")  # Tell the user
            return None  # Go back to the prompt
    else:  # In case the user tried to perform another operation
        # TODO: Implement the appropriate actions here
        # Tell the user the operation is not supported
        print("That operation is not currently supported by cp")
        return None  # Go back to the prompt
