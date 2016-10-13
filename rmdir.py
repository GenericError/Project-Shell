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

    if extra_input == "":
        print("Error: no directory name supplied.")
        return

    try:
        os.rmdir(path=extra_input)
    except OSError:
        print("The directory", extra_input, "is not empty.")
        return
    except Exception:
        print("Sorry, an error occured.")
        return
