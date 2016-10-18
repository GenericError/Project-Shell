""" The main module for Project Shell """
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
except ImportError:
    print("Sorry, Project Shell can not run without the required modules!")
    exit()

NEWLINE = "\n"

CURRENT_USER = pwd.getpwuid(os.getuid())[0]
CURRENT_HOSTNAME = platform.node()

if ".local" in CURRENT_HOSTNAME:
    CURRENT_HOSTNAME = CURRENT_HOSTNAME.split(".local")[0]


def gen_more_input(the_input):
    """ Split the input into usable 'chunks' """
    the_list = the_input.split(' ')
    the_list.remove(the_list[0])
    return the_list


def exit_command(arguments):
    """ Exits the shell """
    print("Exiting...")
    sys.exit()


def clear_command(arguments):
    """ Clears the shell """
    print(chr(27) + "[2J")


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

ARGS_DICT = {
    'exit': [],
    'clear': [],
    'ls': ['cwd'],
    'cd': ['cwd', 'extra_input'],
    'mkdir': ['cwd', 'extra_input'],
    'rmdir': ['cwd', 'extra_input'],
    'cp': ['cwd', 'more_input'],
    'rm': ['cwd', 'more_input'],
}

print("Welcome to Project Shell!")
print("Current time is: "+str(datetime.datetime.now()))
print("Current user is "+CURRENT_USER)
print("Current host is "+CURRENT_HOSTNAME)
print("Current dir is "+os.getcwd())

while 1:
    RUN_COMMAND_THIS_LOOP = False
    PRECEDING_TEXT = ""
    PRECEDING_TEXT += CURRENT_USER
    PRECEDING_TEXT += "@"
    PRECEDING_TEXT += CURRENT_HOSTNAME
    PRECEDING_TEXT += " "+str(os.getcwd()).split("/")[-1]
    PRECEDING_TEXT += "$ "
    COMMAND_INPUT = str(input(PRECEDING_TEXT))
    JUST_COMMAND = COMMAND_INPUT.split(' ')[0]
    try:
        AFTER_COMMAND = COMMAND_INPUT.split(' ')[1]
    except IndexError:
        AFTER_COMMAND = ""
    for command, func in COMMAND_DICT:
        if command == JUST_COMMAND:
            arguments = {}
            for argumnet in ARGS_DICT:
                for i in ARGS_DICT[command]:
                    if i == 'cwd':
                        arguments['cwd'] = os.getcwd()
                    elif i == 'extra_input':
                        arguments['extra_input'] = AFTER_COMMAND
                    elif i == 'more_input':
                        arguments['more_input'] = gen_more_input(COMMAND_INPUT)
            func(arguments)
            RUN_COMMAND_THIS_LOOP = True
        else:
            continue
    if not RUN_COMMAND_THIS_LOOP:
        if JUST_COMMAND == "":
            continue
        else:
            print("project-shell: command", JUST_COMMAND, "not found")
            continue
