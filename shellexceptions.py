""" shellexceptions - all the exceptions for Project Shell """


class CustomBaseException(Exception):
    """ A custom base exception from which all other exceptions will inherit """
    def __init__(self):
        super().__init__()
        self.error_message = None

    def print_error(self):
        try:
            if self.error_message:
                print(self.error_message)
            else:
                print("")
        except:
            print("")


class BlankDirectoryException(CustomBaseException):
    """ Raise if a directory supplied is blank """
    def __init__(self):
        super().__init__()
        self.error_message = "Directoy can not be blank."


class NotADirectoryException(CustomBaseException):
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


class GenericException(CustomBaseException):
    """ Raise in the case of a generic exception """
    def __init__(self):
        super().__init__()
        self.error_message = "Sorry, an error occured."


class UnsupportedOperationException(CustomBaseException):
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


class SourceDestinationAreEqualException(CustomBaseException):
    """ Raise if the source and destination arguments are the same """
    def __init__(self):
        super().__init__()
        self.error_message = "The source and destination arguments can not be the same."


class SourceArgumentIsADirectoryException(CustomBaseException):
    """ Raise if the source argument is a directory and should not be """
    def __init__(self):
        super().__init__()
        self.error_message = "The source argumnet can not be a directory."


class DirectoryNameNotSuppliedException(CustomBaseException):
    """ Raise if a directory argument was not supplied when it should have been """
    def __init__(self):
        super().__init__()
        self.error_message = "Directory name was not supplied."


class DirectoryAlreadyExistsException(CustomBaseException):
    """ Raise if a directory already exists """
    def __init__(self, directory_name=None):
        super().__init__()
        self.error_message = self.construct_error_message(directory_name)

    def construct_error_message(self, dir_name):
        """ Generate a logical error message """
        if dir_name is None:
            return "The directory already exists."
        else:
            msg = "The directory "
            msg += dir_name
            msg += " already exists."
            return msg


class DirectoryNotEmptyException(CustomBaseException):
    """ Raise if a directory is not empty """
    def __init__(self):
        super().__init__()
        self.error_message = "Directory is not empty."
