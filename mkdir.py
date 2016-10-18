""" Module which contains the mkdir command """

import os


def run_command(arguments):
    """ Function which executes the mkdir command """
    try:
        extra_input = arguments['extra_input']
    except KeyError:
        print("Error: no directory name supplied.")
        return

    if extra_input == "":
        print("Error: no directory name supplied.")
        return

    try:
        os.mkdir(path=extra_input)
    except FileExistsError:
        print("The directory", extra_input, "already exists.")
        return
    except Exception:
        print("Sorry, an error occured.")
        return
