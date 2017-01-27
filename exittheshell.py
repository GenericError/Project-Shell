""" The module that contains the exit command code """

import sys

def run_command(options, arguments):
    """ Exits the shell """
    return_code = 0
    if options == []:
        if arguments == []:  # If the arguments dictionary is blank
            print("Exiting...")  # Tells the user that the program is closing
            sys.exit(return_code)  # Exits the program
        else:  # Otherwise, do the following
            # Tell the user that they were ignored
            print("Arguments", arguments, "were ignored!")
            print("Exiting...")  # Tells the user that the program is closing
            sys.exit(return_code)  # Exits the program
    else:
        if arguments == []:
            print("Options", options, "were ignored!")
            print("Exiting...")
            sys.exit(return_code)
        else:
            print("Options", options, "were ignored!")
            print("Arguments", arguments, "were ignored!")
            print("Exiting...")
            sys.exit()return_code
