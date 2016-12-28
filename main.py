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
    import argsplit
except ImportError:  # If any module failed to be imported
    print("Sorry, Project Shell can not run without the required modules!")
    print("This might have been a random error, perhaps try running")
    print("Project Shell again to see if it happens twice.")
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
    JUST_COMMAND = COMMAND_INPUT.split(' ')[0].lower()for command in COMMAND_DICT:  # For each command in the dictionary
        if command == JUST_COMMAND:  # If the command is equal to the input
            func = COMMAND_DICT[command]
            func(argsplit.process_string(COMMAND_INPUT))
            RUN_THIS_LOOP = True  # Yes, we have executed a command this loop
    if not RUN_THIS_LOOP:  # If a command was not executed this loop
        if JUST_COMMAND == "":  # If the user didn't give a command
            continue  # Do nothing and go back to the prompt
        else:  # Otherwise
            # Tell the user the command was not found
            print("project-shell: command", JUST_COMMAND, "not found")
            continue  # Go back to the prompt
