""" The main module for Project Shell """
# Here are all our imports, most of them being commands
try:
    import sys
    import os
    import pwd
    import datetime
    import platform
    import ls
    import cd
    import mkdir
    import rmdir
    import cp
    import rm
except ImportError:  # If any module failed to be imported
    print("Sorry, Project Shell can not run without the required modules!")
    exit()  # Tell the user and exit the program

NEWLINE = "\n"  # Constant for the newline character (\n)

CURRENT_USER = pwd.getpwuid(os.getuid())[0]  # The username of the current user
CURRENT_HOSTNAME = platform.node()  # The hostname of the current computer

if ".local" in CURRENT_HOSTNAME:  # Some OSes append .local to the hostname
    CURRENT_HOSTNAME = CURRENT_HOSTNAME.split(".local")[0]  # We remove it here


def gen_more_input(the_input):
    """ Split the input into usable 'chunks' """
    the_list = the_input.split(' ')  # Split the input where there are spaces
    the_list.remove(the_list[0])  # Removes the command the user input
    return the_list  # Returns all the other arguments


def exit_command(args):
    """ Exits the shell """
    if args == {}:  # If the arguments dictionary is blank
        print("Exiting...")  # Tells the user that the program is closing
        sys.exit()  # Exits the program
    else:  # Otherwise, do the following
        # Tell the user that they were ignored
        print("Arguments", args, "were ignored!")
        print("Exiting...")  # Tells the user that the program is closing
        sys.exit()  # Exits the program


def clear_command(args):
    """ Clears the shell """
    if args == {}:  # If no arguments were provided
        print(chr(27) + "[2J")  # Clears the shell and returns to the prompt
    else:  # Otherwise
        print(chr(27) + "[2J")  # Clears the shell
        # Tells the user that they were ignored
        print("Arguments", args, "were ignored!")

# The following dictionary has the list of the commands, and the functions that
# are called when the command is searched for in the dictionary

COMMAND_DICT = {
    'exit': exit_command,
    'clear': clear_command,
    'ls': ls.run_command,
    'cd': cd.run_command,
    'mkdir': mkdir.run_command,
    'rmdir': rmdir.run_command,
    'cp': cp.run_command,
    'rm': rm.run_command,
}

# The following dictionary has the list the arguments that a function requires
# more_input or extra_input means extra arguments, both of which are plannning
# to be phased out in the near future
# NOTE: cwd is now depreciated

ARGS_DICT = {
    'exit': [],
    'clear': [],
    'ls': [],
    'cd': ['extra_input'],
    'mkdir': ['extra_input'],
    'rmdir': ['extra_input'],
    'cp': ['more_input'],
    'rm': ['more_input'],
}

print("Welcome to Project Shell!")  # Welcome statement
print("Current time:\t"+str(datetime.datetime.now()))  # Unformatted time
print("Current user:\t"+CURRENT_USER)  # Current username
print("Current host:\t"+CURRENT_HOSTNAME)  # Current computer hostname
print("Current directory:\t"+os.getcwd())  # Current working directory

while 1:  # Main event loop
    RUN_THIS_LOOP = False  # True when a command is executed in this loop
    PRECEDING_TEXT = ""  # We start with a blank string
    PRECEDING_TEXT += CURRENT_USER  # Append the username to the string
    PRECEDING_TEXT += "@"  # Append an 'at' symbol to the string
    PRECEDING_TEXT += CURRENT_HOSTNAME  # Append the hostname to the string
    # Append the innermost directory name of the current working directory
    PRECEDING_TEXT += " "+str(os.getcwd()).split("/")[-1]
    PRECEDING_TEXT += "$ "  # Append a dollar sign and a space
    COMMAND_INPUT = str(input(PRECEDING_TEXT))  # Get the input of the user
    # Split the command and its flags and aguments, splitting them at spaces
    JUST_COMMAND = COMMAND_INPUT.split(' ')[0].lower()
    try:
        # Try to see if there is more input other than just the command
        AFTER_COMMAND = COMMAND_INPUT.split(' ')[1]
    except IndexError:  # If the command is the only input
        AFTER_COMMAND = ""  # A blank string will be the extra input
    for command in COMMAND_DICT:  # For each command in the dictionary
        if command == JUST_COMMAND:  # If the command is equal to the input
            func = COMMAND_DICT[command]
            arguments = {}  # Initialise an empty dictionary for arguments
            # For each command in the argument dictionary
            for thing in ARGS_DICT:
                # For each argument in the arguments dictionary that is
                # required for the specific command
                for i in ARGS_DICT[command]:
                    if i == 'extra_input':  # If the argument is extra_input
                        arguments['extra_input'] = AFTER_COMMAND  # Add to dict
                    elif i == 'more_input':  # If the argument is more_input
                        # Generate that extra input and add it to the dict
                        arguments['more_input'] = gen_more_input(COMMAND_INPUT)
            # Run the command and capture its restlt
            func_result = func(arguments)
            # If the function returns None, then it has run successfully,
            # meaning we can return to the prompt and ask for the next command
            if func_result is None:
                continue  # Jump to the next iteration of the main loop
            else:  # Otherwise
                while 1:  # Repeat whilst the number one is True
                    try:  # Try to do the following
                        # If the command needs more input, it will return a
                        # dictionary with its requirements. We will then run
                        # the next step by calling the function that needs to
                        # be run. Yes, we are now dividing the commands into
                        # steps, with each step being when a function requires
                        # more input. An example dictionary is as follows:
                        # {'requirements': {'IO': 'I', prompt: 'Enter name:'}}
                        # Breaking it down, we want input with the prompt to
                        # the user saying 'Enter name:'
                        in_thing = None  # Set the input to None
                        out_thing = None  # Set the output to None
                        # Set the function requirements to None
                        requirements_for_func = None
                        # Set the variable to the requirements given by the
                        # function that was previously executed
                        requirements = func_result['requirements']
                        # If the input/output requirement (IO) is input (I)
                        if requirements['IO'] == 'I':
                            # Ask the user for input with the prompt given
                            # by the function (from the requirements dict)
                            in_thing = input(requirements['prompt'])
                            # Set the variable to be returned to the function
                            # to the input that the user gave
                            requirements_for_func = in_thing
                        # Get the name of the function to be executed next
                        # Which was given by the requirements dictioanry
                        next_func = func_result['next_func']
                        # Execute the function and capture the result in case
                        # we need to execute another function in the next loop
                        func_result = next_func(requirements_for_func)
                    except Exception:  # In case anything went wrong
                        print("Sorry, an error occured")  # Tell the user
                        break  # Break out of the loop and return to the prompt
            RUN_THIS_LOOP = True  # Yes, we have executed a command this loop
    if not RUN_THIS_LOOP:  # If a command was not executed this loop
        if JUST_COMMAND == "":  # If the user didn't give a command
            continue  # Do nothing and go back to the prompt
        else:  # Otherwise
            # Tell the user the command was not found
            print("project-shell: command", JUST_COMMAND, "not found")
            continue  # Go back to the prompt
