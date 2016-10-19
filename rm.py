""" Module which contains the rm command """

import os  # Importing this for system operations and directory things


def run_command(arguments):
    """ Function which runs the rm command """

    try:  # Try to do the following
        # Get the user's extra input (in this case the name of the file
        # to be removed by the command)
        delete_query = arguments['more_input'][0]
    # In case it wasn't passed to the function or
    # the user didn't provide any name
    except KeyError:
        print("Error: No file name was supplied")  # Tell the user
        return  # Go back to the prompt

    # If the user isn't trying to delete all files with
    # a certain extension (hence the wildcard)
    if not delete_query.startswith("*"):
        try:  # Try to do the following
            # Try to delete the directory
            os.remove(delete_query)
        # In case the user tried to complete this operation on folders
        except OSError:
            # Tell the user you aren't allowed to do this
            print("You can only perform this command on files")
            return  # Go back to the prompt
        except Exception:  # If another error occured
            print("Sorry, an error occured.")  # Tell the user
            return  # Go back to the prompt
    # If the user is trying to delete all files with a certain extension
    else:
        # Create a variable to hold the name of the extension
        # EG: If delete_query was "*.txt", then the variable
        # would now be reassigned to "txt"
        delete_query = delete_query.split("*.")[1]
        # For each file and folder in the current directory
        for thing in os.listdir(os.getcwd()):
            # If the thing ends with the file extension
            if thing.endswith(delete_query):
                try:  # Try to do the following
                    # If the thing is not a directory
                    if not os.path.isdir(thing):
                        os.remove(thing)  # Remove the file
                        print(thing, "deleted.")  # Tell the user it's gone
                    else:  # Otherwise, if it is a directory
                        continue  # Move on to the next file/folder in the dir
                except Exception:  # If an error occured
                    # Tell the user that the thing could not be deleted
                    print("Sorry,", thing, "could not be deleted.")
    return  # Go back to the prompt
