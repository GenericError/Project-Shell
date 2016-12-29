""" Module that runs the os command """

import os
import shutil
import textwrap
from shellexceptions import *


def run_command(argument_list):
    """ Function that runs the ls command """
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

    file_dir_list = os.listdir(os.getcwd())
    terminal_width = int(shutil.get_terminal_size()[0])
    constructed_string = ""
    for thing in file_dir_list:
        constructed_string += thing
        constructed_string += ' \t\t'
        done_first_thing = True
    lines = textwrap.fill(text=constructed_string, width=terminal_width)
    print(lines)
    return None
