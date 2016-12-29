""" argsplit - splits a string in the style of sys.argv """

import sys

def process_string(string_to_process):
    """ Returns a list of flags and arguments from the string supplied """
    ESCAPE_TEXT = "$ESCAPE$"

    string_to_process = string_to_process.replace("\\"+" ", ESCAPE_TEXT)
    processed_list = string_to_process.split(" ")
    incrementer = 0

    while incrementer < len(processed_list):
        new_string = str(processed_list[incrementer]).replace(ESCAPE_TEXT, " ")
        processed_list[incrementer] = new_string
        incrementer += 1

    processed_list.pop(0)  # Remove the command name
    return processed_list

if __name__ == '__main__':
    try:
        if sys.argv[1] == "--test":
            test_string_to_process = input("The test string > ")
            test_processed_list = process_string(test_string_to_process)
            print("Here is the list returned by the function:")
            print(test_processed_list)
    except Exception:
        exit()
