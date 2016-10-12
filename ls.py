import os
import shutil

def run_command(arguments={}):
    try:
        current_dir = arguments['cwd']
    except:
        print("Sorry, an error occured.")
        return
    file_dir_list = os.listdir(current_dir)
    terminal_width = shutil.get_terminal_size()[0]
    longest_name = 0

    for thing in file_dir_list:
        if len(thing) > longest_name:
            longest_name = len(thing)
        else:
            continue

    columns_usable = int(terminal_width/longest_name)
    long_dirs = False
    terminal_buffer = 4
    list_index = 0

    lines = (str(" "*6).join(file_dir_list[i:i+columns_usable]) for i in range(0,len(file_dir_list),columns_usable))
    print('\n'.join(lines))
