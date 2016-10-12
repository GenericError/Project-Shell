try:
    import sys
    import os
    import pwd
    import datetime
    import platform
    import ls
except ImportError:
    print("Sorry, Project Shell can not run without this/these module/s!")
    exit()

NEWLINE = "\n"

current_user = pwd.getpwuid(os.getuid())[0]
current_hostname = platform.node()

if ".local" in current_hostname:
    current_hostname = current_hostname.split(".local")[0]


def exit_command():
    print("Exiting...")
    sys.exit()


def clear_command():
    print(chr(27) + "[2J")


def ls_command():
    ls.run_command()

command_dict = {
    'exit': exit_command,
    'clear': clear_command,
    'ls': ls_command,
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
    for command in command_dict.keys():
        if command == command_input:
            command_dict[command]()
            run_command_this_loop = True
        else:
            continue
    if not run_command_this_loop:
        if command_input == "":
            continue
        else:
            print("project-shell: command", command_input, "not found")
            continue
