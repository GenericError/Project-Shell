import shutil

def run_command(arguments={}):
    try:
        current_dir = arguments['cwd']
    except:
        print("Sorry an error occured.")
        return

    print(arguments)
