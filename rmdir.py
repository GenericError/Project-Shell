""" Module which includes the rmdir command """
import os  # Importing this for deletion and directory things


def run_command(arguments):
    """ Function which runs the rmdir command"""
    try:  # Try to do the following
        # Get the name of the directory to delete
        extra_input = arguments['extra_input']
    except KeyError:  # If a name wasn't supplied
        print("Error: no directory name supplied.")  # Tell the user
        return None  # Go back to the prompt

    if extra_input == "":  # If the name supplied is blank
        print("Error: no directory name supplied.")  # Tell the user
        return None  # Go back to the prompt

    try:  # Try to do the follwing
        os.rmdir(path=extra_input)  # Remove the directory
    except OSError:  # If the directory isn't empty
        print("The directory", extra_input, "is not empty.")  # Tell the user
        return None  # Go back to the prompt
    except Exception:  # If another error occured
        print("Sorry, an error occured.")  # Tell the user
        return None  # Go back to the prompt
