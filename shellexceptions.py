""" shellexceptions - all the exceptions for Project Shell """


class BlankDirectoryException(Exception):
    """ Raise if a directory supplied is blank """
    def __init__(self):
        super().__init__()
        self.error_message = "Directoy can not be blank."


class NotADirectoryException(Exception):
    """ Raise if the supplied path is not a directory """
    def __init__(self, supplied_information=None):
        super().__init__()
        self.error_message = self.construct_error_message(supplied_information)

    def construct_error_message(self, supplied_information):
        """ Generate a logical error message """
        if supplied_information is None:
            return "Not a directory."
        else:
            msg = supplied_information
            msg += " is not a directory."
            return msg


class GenericException(Exception):
    """ A generic exception """
    def __init__(self):
        super().__init__()
        self.error_message = "Sorry, an error occured."
