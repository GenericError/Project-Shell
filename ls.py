""" Module that runs the ls command """

import os
import shutil


def run_command(arguments):
    """ Function that runs the ls command """
    file_dir_list = os.listdir(os.getcwd())
    terminal_width = shutil.get_terminal_size()[0]
    longest_name = 0

    for thing in file_dir_list:
        if len(thing) > longest_name:
            longest_name = len(thing)
        else:
            continue

    columns_usable = int(terminal_width/longest_name)

    lines = (
        str(" "*6).join(file_dir_list[i:i+columns_usable])
        for i in range(0, len(file_dir_list), columns_usable)
    )
    print('\n'.join(lines))  # Print the result of the ls command
    return None  # Go back to the prompt
