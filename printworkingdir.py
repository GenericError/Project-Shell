""" Module that runs the pwd command """

import os

def run_command(options, arguments):
    """ Function that runs the pwd command """

    print(os.path.abspath(os.getcwd()))
