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
    """ Raise in the case of a generic exception """
    def __init__(self):
        super().__init__()
        self.error_message = "Sorry, an error occured."


class UnsupportedOperationException(Exception):
    """ Raise if the operation attempted is not currently supported """
    def __init__(self, command_name=None):
        super().__init__()
        self.error_message = self.construct_error_message(command_name)

    def construct_error_message(self, command_name):
        """ Generate a logical error message """
        if command_name is None:
            return "That operation is not currently supported."
        else:
            msg = "That operation is not currently supported by "
            msg += command_name
            msg += "."
            return msg


class SourceDestinationAreEqualException(Exception):
    """ Raise if the source and destination arguments are the same """
    def __init__(self):
        super().__init__()
        self.error_message = "The source and destination arguments can not be the same."


class SourceArgumentIsADirectoryException(Exception):
    """ Raise if the source argument is a directory and should not be """
    def __init__(self):
        super().__init__()
        self.error_message = "The source argumnet can not be a directory."
