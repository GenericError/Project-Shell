""" Module which contains the rm command """

import os


def run_command(arguments):
    """ Function which runs the rm command """
    try:
        current_directory = arguments['cwd']
    except KeyError:
        print("Sorry, an error occured.")

    try:
        delete_query = arguments['more_input'][0]
    except KeyError:
        print("The file to delete is the only required argument")
        return

    if not delete_query.startswith("*"):
        try:
            os.remove(os.path.join(arguments['cwd'], delete_query))
        except OSError:
            print("You can only perform this command on files")
            return
        except Exception:
            print("Sorry, an error occured.")
            return
    else:
        delete_query = delete_query.split("*.")[1]
        for file in os.listdir(current_directory):
            if file.endswith(delete_query):
                try:
                    os.remove(file)
                    print(file, "deleted.")
                except Exception:
                    print("Sorry,", file, "could not be deleted.")
    return
