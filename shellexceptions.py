""" All the exceptions for Project Shell """


def construct_error_message(supplied_information="", error_string="", default_error_string=""):
    if "$VAR$" in error_string:
        if supplied_information is not None:
            error_string = str(error_string).replace("$VAR$", str(supplied_information))
            return error_string
        else:
            return default_error_string
    else:
        return default_error_string


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
        self.error_message = construct_error_message(supplied_information, "$VAR$ is not a directory.", "Not a directory.")


class GenericException(CustomBaseException):
    """ Raise in the case of a generic exception """
    def __init__(self):
        super().__init__()
        self.error_message = "Sorry, an error occured."


class UnsupportedOperationException(CustomBaseException):
    """ Raise if the operation attempted is not currently supported """
    def __init__(self, command_name=None):
        super().__init__()
        self.error_message = construct_error_message(command_name, "That operation is not currently supported by $VAR$.", "That operation is not currently supported.")


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
        self.error_message = construct_error_message(directory_name, "The directory $VAR$ already exists.", "The directory already exists.")


class DirectoryNotEmptyException(CustomBaseException):
    """ Raise if a directory is not empty """
    def __init__(self):
        super().__init__()
        self.error_message = "Directory is not empty."


class InvalidOperationForDirectoriesException(CustomBaseException):
    """ Raise if an operation expects a file as an argument rather
    than a directory """
    def __init__(self):
        super().__init__()
        self.error_message = "You can only perform this operation on files"


class FileCouldNotBeDeletedException(CustomBaseException):
    """ Raise if a file could not be deleted if it should have been """
    def __init__(self, file_name=None):
        super().__init__()
        self.error_message = construct_error_message(file_name, "The file $VAR$ could not be deleted", "The file could not be deleted.")


class FlagOrArgumentNotGivenException(CustomBaseException):
    """ Raise if a flag or an argument was not given when it was required """
    def __init__(self):
        super().__init__()
        self.error_message = "One or more required flags or arguments were not given."


class ImportException(CustomBaseException):
    """ Raise if a module ould not be imported successfully """
    def __init__(self):
        super().__init__()
        self.error_message = "One or more modules could not be imported"
