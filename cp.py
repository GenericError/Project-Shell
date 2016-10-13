import shutil
import os

def run_command(arguments={}):
    try:
        current_dir = arguments['cwd']
    except:
        print("Sorry an error occured.")
        return

    if len(arguments['more_input']) < 2:
        print("Source and/or destination arguments are required")
        return
    elif len(arguments['more_input']) > 2:
        print("Source and destination are the only required arguments")
        return

    more_input = arguments['more_input']
    source = more_input[0]
    destination = more_input[1]

    if source == destination:
        print("The two given arguments can not be the same")
        return
    elif os.path.isdir(source):
        print("Error: the source argumnet is a directory!")
        return
    elif os.path.isfile(source):
        if os.exists(destination):
            print("That operation is not currently supported by cp")
        elif not os.exists(destination):
            try:
                shutil.copy2(source, destination)
            except:
                print("Sorry, and error occured.")
        else:
            print("Sorry an error occured.")
    else:
        print("That operation is not currently supported by cp")
