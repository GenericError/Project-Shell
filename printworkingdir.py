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
    except Exception as e:
        try:
            raise FlagOrArgumentNotGivenException
        except FlagOrArgumentNotGivenException as new_e:
            new_e.print_error()
            return None
    
    print(os.path.abspath(os.getcwd()))
