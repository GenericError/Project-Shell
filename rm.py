import os

def run_command(arguments={}):
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
        try:
            os.remove(os.path.join(arguments['cwd'], delete_query))
        except OSError:
            print("You can only perform this command on files")
            return
        except:
            print("Sorry, an error occured.")
            return
    else:
        delete_query = delete_query.split("*.")[1]
        for file in os.listdir(current_directory):
            if file.endswith(delete_query):
                try:
                    os.remove(file)
                    print(file, "deleted.")
                except:
                    print("Sorry,", file, "could not be deleted.")
    return
