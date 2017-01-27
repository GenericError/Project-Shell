""" Module that runs the pwd command """

import os

def run_command(options, arguments):
    """ Function that runs the pwd command """
    return_code = 0
    print(os.path.abspath(os.getcwd()))
    return return_code  # Pretty redundant
