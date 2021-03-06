""" Module that runs the pwd command """

import os

MAN_DOC = """pwd - print working directory
Usage: pwd

Returns the full path of the current working directory of the terminal."""

def run_command(options, arguments):
    """ Function that runs the pwd command """
    return_code = 0
    print(os.path.abspath(os.getcwd()))
    return return_code  # Pretty redundant
