""" The module that contains the clear command code """

MAN_DOC = """clear - make the terminal blank
Usage: clear

The command will make the terminal blank, resulting in a single prompt being on the screen.
NOTE: The command is a bit buggy at the moment, resulting in the prompt being located at random vertical locations. If you have a fix, please fork us."""

def run_command(options, arguments):
    """ Clears the shell """
    return_code = 0
    if options == []:
        if arguments == []:
            print(chr(27) + "[2J")
        else:  # Otherwise
            print(chr(27) + "[2J")  # Clears the shell
            # Tells the user that they were ignored
            print("Arguments", arguments, "were ignored!")
    else:
        if arguments == []:
            print(chr(27) + "[2J")
            print("Options", options, "were ignored!")
        else:
            print(chr(27) + "[2J")
            print("Options", options, "were ignored!")
            print("Arguments", arguments, "were ignored!")
    return return_code
