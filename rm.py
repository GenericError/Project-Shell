import os

def run_command(arguments={}):
    print("Under construction")
    return
    try:
        current_directory = arguments['cwd']
    except:
        print("Sorry, an error occured.")

    try:
        delete_query = arguments['more_input'][0]
    except:
        print("The file to delete is the only required argument")
        return

    if not delete_query.startswith("*"):
        os.remove(os.path.join(arguments['cwd'], ['more_input'][0]))
    else:
        files_to_delete = os.walk(current_directory)
        for i in files_to_delete:
            pass
