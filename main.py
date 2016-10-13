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
except ImportError:
    print("Sorry, Project Shell can not run without the required modules!")
    exit()

NEWLINE = "\n"

current_user = pwd.getpwuid(os.getuid())[0]
current_hostname = platform.node()

if ".local" in current_hostname:
    current_hostname = current_hostname.split(".local")[0]


def generate_more_input(command_input):
    command_input_list = command_input.split(' ')
    command_input_list.remove(command_input_list[0])
    return command_input_list


def exit_command(arguments={}):
    print("Exiting...")
    sys.exit()


def clear_command(arguments={}):
    print(chr(27) + "[2J")


def ls_command(arguments={}):
    ls.run_command(arguments)


def cd_command(arguments={}):
    cd.run_command(arguments)


def mkdir_command(arguments={}):
    mkdir.run_command(arguments)


def rmdir_command(arguments={}):
    rmdir.run_command(arguments)


def cp_command(arguments={}):
    cp.run_command(arguments)


command_dict = {
    'exit': exit_command,
    'clear': clear_command,
    'ls': ls_command,
    'cd': cd_command,
    'mkdir': mkdir_command,
    'rmdir': rmdir_command,
    'cp': cp_command,
}

args_dict = {
    'exit': [],
    'clear': [],
    'ls': ['cwd'],
    'cd': ['cwd', 'extra_input'],
    'mkdir': ['cwd', 'extra_input'],
    'rmdir': ['cwd', 'extra_input'],
    'cp': ['cwd', 'more_input']
}

print("Welcome to Project Shell!")
print("Current time is: "+str(datetime.datetime.now()))
print("Current user is "+current_user)
print("Current host is "+current_hostname)
print("Current dir is "+os.getcwd())

while 1:
    run_command_this_loop = False
    preceding_text = ""
    preceding_text += current_user
    preceding_text += "@"
    preceding_text += current_hostname
    preceding_text += " "+str(os.getcwd()).split("/")[-1]
    preceding_text += "$ "
    command_input = str(input(preceding_text))
    just_command = command_input.split(' ')[0]
    try:
        after_command = command_input.split(' ')[1]
    except IndexError:
        after_command = ""
    for command in command_dict.keys():
        if command == just_command:
            arguments = {}
            for argumnet in args_dict:
                for i in args_dict[command]:
                    if i == 'cwd':
                        arguments['cwd'] = os.getcwd()
                    elif i == 'extra_input':
                        arguments['extra_input'] = after_command
                    elif i == 'more_input':
                        arguments['more_input'] = generate_more_input(command_input)
            command_dict[command](arguments)
            run_command_this_loop = True
        else:
            continue
    if not run_command_this_loop:
        if just_command == "":
            continue
        else:
            print("project-shell: command", just_command, "not found")
            continue
