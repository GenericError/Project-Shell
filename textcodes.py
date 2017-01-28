""" Text colour and formatting codes for the use of Project Shell """

MAN_DOC = """textcodes - UNIX terminal formatting codes
Usage: N/A

This file contains UNIX terminal formatting codes for the use of Project Shell."""

class TerminalColours(object):
    """ Class containing the colour codes for the terminal """
    def __init__(self):
        # Colour codes
        self._blue_colour = "\033[94m"
        self._cyan_colour = "\033[96m"
        self._darker_cyan_colour = "\033[36m"
        self._green_colour = "\033[92m"
        self._yellow_colour = "\033[93m"
        self._purple_colour = "\033[95m"
        self._red_colour = "\033[91m"

    def get_colour_code(self, colour_name):
        """ Fetches the colour code for the colour name passed """
        return getattr(self, "_"+colour_name+"_colour")

    def override_colour_code(self, colour_name, new_value):
        """ Overrides the colour code for the colour name passed """
        setattr(self, "_"+colour_name+"_colour", new_value)
        return


class TerminalFormatting(object):
    """ Class containing the formatting codes for the terminal """
    def __init__(self):
        # Formatting codes
        self._bold_formatting = "\033[1m"
        self._end_of_colours = "\033[0m"
        self._underline_formatting = "\033[4m"
        self._blink_formatting = "\033[5m"

    def get_formatting_code(self, formatting_code_name):
        """ Fetches the formatting code for the formmating code name passed """
        if formatting_code_name == "end":
            return getattr(self, "_end_of_colours")
        else:
            return getattr(self, "_"+formatting_code_name+"_formatting")

    def override_formatting_code(self, formatting_code_name, new_value):
        """ Overrides the formatting code for the colour name passed """
        if formatting_code_name == "end":
            return setattr(self, "_end_of_colours", new_value)
        else:
            setattr(self, "_"+formatting_code_name+"_formatting", new_value)
        return
