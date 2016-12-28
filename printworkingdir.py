""" Module that runs the pwd command """

import os

def run_command(processed_string):
    """ Function that runs the pwd command """
    print(os.path.abspath(os.getcwd()))
