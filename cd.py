""" Module that executes the cd command """
import os


def run_command(arguments):
    """ Runs the cd command """
    try:
        current_dir = arguments['cwd']
    except KeyError:
        print("Sorry, an error occured")
    try:
        extra_input = arguments['extra_input']
    except KeyError:
        print("The location to change to is the required argument")
    directory_to_go = os.path.join(current_dir, extra_input)
    if extra_input == "":
        print("Directoy can not be blank.")
    elif not os.path.isdir(directory_to_go):
        print(extra_input, "is not a directory.")
    elif os.path.isdir(directory_to_go):
        os.chdir(directory_to_go)
    else:
        print("Sorry, an error occured.")
    return
