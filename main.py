""" The main module for Project Shell """
# Here are all our imports, most of them being commands

try:
    from shellexceptions import GenericException, ImportException
    import os, pwd, datetime, platform, getopt, textcodes
    import ls, cd, mkdir, rmdir, cp, rm, printworkingdir
    import exittheshell, cleartheshell
except ImportError as e:  # If any module failed to be imported
    try:
        try:
            raise ImportException
        except ImportException as new_e:
            new_e.print_error()
            extra_info_q = input("Display extra debug info? [Y/n] > ")
            if extra_info_q.lower().startswith("y"):
                print("\n[BEGIN]\tINFO")
                print("\n[INFO]\t"+str(e))
                print("\n[END]\tINFO")
                input("\nPress enter to exit Project Shell ")
                exit()
            else:
                exit()
    except Exception:
        exit_from_exception()


TerminalColourInstance = textcodes.TerminalColours()
TerminalFormattingInstance = textcodes.TerminalFormatting()
red_warning_text = TerminalColourInstance.get_colour_code("red")
red_warning_text += TerminalFormattingInstance.get_formatting_code("bold")
red_warning_text += TerminalFormattingInstance.get_formatting_code("blink")
red_warning_text += "WARNING!"
red_warning_text += TerminalFormattingInstance.get_formatting_code("end")


def get_current_user():
    user = pwd.getpwuid(os.getuid())[0]
    return user

def get_current_hostname():
    hostname = platform.node()
    if hostname.endswith(".local"):
        hostname = hostname.split(".local")[0]  # We remove it here
    return hostname


CURRENT_USER = get_current_user()  # The username of the current user
CURRENT_HOSTNAME =  get_current_hostname # The hostname of the current computer
NEWLINE = "\n"  # Constant for the newline character (\n)


def exit_from_exception():
    """ Call if the user interrupted the shell at input """
    print('\n')
    exit()


def generate_welcome_message():
    generated_message = ""
    generated_message += "Welcome to Project Shell!"
    generated_message += "Current time:\t"+str(datetime.datetime.now())
    generated_message += "Current user:\t"+CURRENT_USER
    generated_message += "Current host:\t"+CURRENT_HOSTNAME
    generated_message += "Current directory:\t"+os.getcwd()
    return generated_message


def generate_root_warning(executing_command=True, command_name=None):
    generated_message = ""
    generated_message += "\n"+red_warning_text+" You are running Project Shell as root."
    if not executing_command:
        generated_message += "Please exercise extra caution when issuing commands.\n"
    else:
        generated_message += "You entered '"+command_name, "'. Confirm it is correct"

# The following dictionary has the list of the commands, and the functions that
# are called when the command is searched for in the dictionary

COMMAND_DICT = {
    'exit': exittheshell.run_command,
    'clear': cleartheshell.run_command,
    'ls': ls.run_command,
    'cd': cd.run_command,
    'mkdir': mkdir.run_command,
    'rmdir': rmdir.run_command,
    'cp': cp.run_command,
    'rm': rm.run_command,
    'pwd': printworkingdir.run_command,
}

# 'command name': ['short options', [long, options]]
OPTIONS_DICT = {
    'cd': ['', []],
    'cp': ['v ::', []],
    'ls': [':', []],
    'mkdir': ['v :', []],
    'rm': ['v :', []],
    'rmdir': [':', []],
    'exit': ['', []],
    'clear': ['', []],
    'pwd': ['', []],
}


print(generate_welcome_message())

if CURRENT_USER == "root":
    print(generate_root_warning(executing_command=False))

while 1:  # Main loop
    CURRENT_DIRECTORY = os.getcwd()
    in_home = bool(str(os.getcwd()) == str(os.path.expanduser('~')))
    in_root = bool(str(os.getcwd()) == str('/'))
    RUN_THIS_LOOP = False  # True when a command is executed in this loop
    PRECEDING_TEXT = ""  # We start with a blank string
    PRECEDING_TEXT += CURRENT_USER  # Append the username to the string
    PRECEDING_TEXT += "@"  # Append an 'at' symbol to the string
    PRECEDING_TEXT += CURRENT_HOSTNAME  # Append the hostname to the string
    # Append the innermost directory name of the current working directory
    if in_home:
        PRECEDING_TEXT += " ~"
    elif in_root:
        PRECEDING_TEXT += " /"
    else:
        PRECEDING_TEXT += " "+str(CURRENT_DIRECTORY).split("/")[-1]
    PRECEDING_TEXT += "$ "  # Append a dollar sign and a space
    try:
        COMMAND_INPUT = str(input(PRECEDING_TEXT))  # Get the input of the user
        COMMAND_INPUT = COMMAND_INPUT.strip()
    except EOFError:
        exit_from_exception()
    except KeyboardInterrupt:
        exit_from_exception()
    try:
        JUST_COMMAND = COMMAND_INPUT.split(' ')[0].lower()
        everything_but_command = COMMAND_INPUT.split()
        everything_but_command.pop(0)
    except Exception as e:
        try:
            raise GenericException
        except GenericException as new_e:
            new_e.print_error()
            continue
    try:
        try:
            short_options = OPTIONS_DICT[JUST_COMMAND][0]
            long_options = OPTIONS_DICT[JUST_COMMAND][1]

            options, arguments = getopt.getopt(everything_but_command,
                                               shortopts=short_options,
                                               longopts=long_options)
        except getopt.GetoptError as error:
            print(error)
            continue
    except Exception as e:
        try:
            raise GenericException
        except GenericException as new_e:
            new_e.print_error()
            continue
    for command in COMMAND_DICT:  # For each command in the dictionary
        if command == JUST_COMMAND:  # If the command is equal to the input
            func = COMMAND_DICT[command]
            func(options, arguments)
            RUN_THIS_LOOP = True  # Yes, we have executed a command this loop
    if not RUN_THIS_LOOP:  # If a command was not executed this loop
        if JUST_COMMAND == "":  # If the user didn't give a command
            continue  # Do nothing and go back to the prompt
        else:  # Otherwise
            # Tell the user the command was not found
            print("project-shell: command", JUST_COMMAND, "not found")
            continue  # Go back to the prompt
