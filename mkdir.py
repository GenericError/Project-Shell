""" Module which contains the mkdir command """

import os  # Importing this for directory things


def run_command(arguments):
    """ Function which executes the mkdir command """
    try:  # Try to do the following
        # Get the user's extra input (in this case the name of
        #  the directory to be created)
        extra_input = arguments['extra_input']
    except KeyError:  # In case the user did not provide that
        print("Error: no directory name supplied.")  # Tell the user
        return  # Go back to the prompt

    if extra_input == "":  # In case the directory name was blank
        print("Error: no directory name supplied.")  # Tell the user
        return  # Go back to the prompt

    try:  # Try to do the following
        os.mkdir(path=extra_input)  # Make the directory
    except FileExistsError:  # If it already exists
        print("The directory", extra_input, "already exists.")  # Tell the user
        return  # Go back to the prompt
    except Exception:  # In case another error occured
        print("Sorry, an error occured.")  # Tell the user
        return  # Go back to the prompt
