""" Module which includes the rmdir command """
import os


def run_command(arguments):
    """ Function which runs the rmdir command"""
    try:
        extra_input = arguments['extra_input']
    except KeyError:
        print("Error: no directory name supplied.")
        return

    if extra_input == "":
        print("Error: no directory name supplied.")
        return

    try:
        os.rmdir(path=extra_input)
    except OSError:
        print("The directory", extra_input, "is not empty.")
        return
    except Exception:
        print("Sorry, an error occured.")
        return
