import shutil
import textwrap

MAN_DOC = """man - display manual documentation
Usage: man [command]

man requires a command to display documentation. Lack of a command argument will result in an error message.
The documentation is auto discovered from the module of the specified command. Commands should always implement manual information in a format equivalent to other Project Shell commands."""

MAN_ALIASES = {'clear': 'cleartheshell',
               'exit': 'exittheshell',
               'pwd': 'printworking'}

def run_command(options, arguments):
    """ Runs the man command """
    return_code = 0
    HELP_INFORMATION = "man: The Project Shell manual application\nUsage: man [command]"
    terminal_width = int(shutil.get_terminal_size()[0])
    try:
        command_name = arguments[0]
    except Exception:
        for option in options:
            if option[0] == '-h':
                print(HELP_INFORMATION)
                return return_code
        print("man: I need a command to display information about")
        return_code = 1
        return return_code
    for argument in arguments:
        if argument == '-h':
            print(HELP_INFORMATION)
            return return_code

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
        return_code = 2
        return return_code

    try:
        help_text = the_import.MAN_DOC
    except:
        print("No manual documentation was found for this command")
        return_code = 3
        return return_code

    for line in help_text.split('\n'):
        if line == '':
            print()
        for sub_line in textwrap.wrap(text=line, width=terminal_width):
            print(sub_line)
    return return_code
