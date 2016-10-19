""" Module that executes the cd command """
import os  # Importing this module to do directory things


def run_command(arguments):
    """ Runs the cd command """
    extra_input = ""  # Set the dir to cd into to a blank string
    current_dir = os.getcwd()  # Current direcotry is fetched by the system
    try:  # Try to do the following
        # Get the extra input required. In this case,
        # it is the directory to cd into
        extra_input = arguments['extra_input']
    except KeyError:  # In case the extra data was not in the dictionary
        # Tell the user that they missed out the argument
        print("The location to change to is the required argument")
    # Get the path of the directory to change in to
    directory_to_go = os.path.join(current_dir, extra_input)
    if extra_input == "":  # If the user put in a blank directory
        print("Directoy can not be blank.")  # Tell the user
        return  # Go back to the prompt
    # If the argument does not give a valid directory
    elif not os.path.isdir(directory_to_go):
        print(extra_input, "is not a directory.")  # Tell the user
        return  # Go back to the prompt
    elif os.path.isdir(directory_to_go):  # If it is a valid directory
        os.chdir(directory_to_go)  # Change the current directory
    else:  # Otherwise
        print("Sorry, an error occured.")  # Tell the user there was an error
    return  # Go back to the prompt
