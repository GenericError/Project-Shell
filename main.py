import os
import pwd
import platform
import sys
import datetime

NEWLINE = "\n"

current_user = pwd.getpwuid(os.getuid())[0]
current_hostname = platform.node()

if ".local" in current_hostname:
    current_hostname = current_hostname.split(".local")[0]

def exit():
    print("Exiting...")
    sys.exit()

def clear():
    print(chr(27) + "[2J")

command_dict = {
    'exit':exit,
    'clear':clear,
}

print("Welcome to Project Shell!")
print("Current time is: "+str(datetime.datetime.now()))
print("Current user is "+current_user)
print("Current host is "+current_hostname)

while 1:
    run_command_this_loop = False
    preceding_text = ""
    preceding_text += current_user
    preceding_text += "@"
    preceding_text += current_hostname
    preceding_text += os.curdir[:-1]
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
            print("project-shell: command",command_input,"not found")
            continue