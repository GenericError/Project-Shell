import os

def run_command(arguments={}):
    current_dir = arguments['cwd']
    extra_input = arguments['extra_input']
    directory_to_go = os.path.join(current_dir, extra_input)
    if extra_input == "":
        print("Directoy can not be blank.")
    elif not os.path.isdir(directory_to_go):
        print(extra_input, "is not a directory.")
    elif os.path.isdir(directory_to_go):
        os.chdir(directory_to_go)
    else:
        print("Sorry, an error occured.")
    return
