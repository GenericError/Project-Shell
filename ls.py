""" Module that runs the os command """

import os
import shutil


def run_command(argument_list):
    """ Function that runs the ls command """
    amount_required = 0
    try:
        if len(argument_list) >= amount_required:
            pass
        else:
            raise Exception
    except:
        print("error: a required flag or argument was missing")
        return
    
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
