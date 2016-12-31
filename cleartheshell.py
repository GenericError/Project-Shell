""" The module that contains the clear command code """


def run_command(options, arguments):
    """ Clears the shell """
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
