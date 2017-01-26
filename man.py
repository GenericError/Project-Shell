import shutil
import textwrap

MAN_ALIASES = {'clear': 'cleartheshell',
               'exit': 'exittheshell',
               'pwd': 'printworking'}

def run_command(options, arguments):
    """ Runs the man command """
    HELP_INFORMATION = "man: The Project Shell manual application\nUsage: man [command]"
    terminal_width = int(shutil.get_terminal_size()[0])
    try:
        command_name = arguments[0]
    except Exception:
        for option in options:
            if option[0] == '-h':
                print(HELP_INFORMATION)
                return
        print("man: I need a command to display information about")
        return
    for argument in arguments:
        if argument == '-h':
            print(HELP_INFORMATION)
            return

    the_command = arguments[0].lower()
    help_text = ""

    try:
        the_command = MAN_ALIASES[the_command]
    except:
        pass  # It just means we didn't find an alias, that's OK
    try:
        # TODO: Find a way to do this without using __import__()
        the_import = __import__(the_command, globals(), locals(), [], 0)
    except:
        print("Sorry, that command could not be found")
        return

    try:
        help_text = the_import.MAN_DOC
    except:
        print("No manual documentation was found for this command")
        return

    for line in help_text.split('\n'):
        if line == '':
            print()
        for sub_line in textwrap.wrap(text=line, width=terminal_width):
            print(sub_line)
    return
