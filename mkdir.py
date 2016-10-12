import os

def run_command(arguments={}):
    try:
        current_dir = arguments['cwd']
    except:
        print("Sorry an error occured.")
        return
    try:
        extra_input = arguments['extra_input']
    except:
        print("Error: no directory name supplied.")
        return
    try:
        os.mkdir(path=extra_input)
    except FileExistsError:
        print("The directory", extra_input, "already exists.")
        return
    except:
        print("Sorry, an error occured.")
        return
