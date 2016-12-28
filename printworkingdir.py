""" Module that runs the pwd command """

import os

def run_command(argument_list):
    """ Function that runs the pwd command """
    amount_required = 0
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return
    print(os.path.abspath(os.getcwd()))
