""" Module that runs the os command """

import os
import shutil
import textwrap


def run_command(options, arguments):
    """ Function that runs the ls command """
    try:
        dir_to_scan = arguments[0]
    except:
        dir_to_scan = '.'

    file_dir_list = os.listdir(os.path.abspath(dir_to_scan))
    terminal_width = int(shutil.get_terminal_size()[0])
    constructed_string = ""
    for thing in file_dir_list:
        constructed_string += thing
        constructed_string += ' \t\t'
        done_first_thing = True
    lines = textwrap.fill(text=constructed_string, width=terminal_width)
    print(lines)
    return None
