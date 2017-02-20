# Created in response to issue #32

""" Checks for permissions for a path/file """

import os

def check_existence(path):
    """ Returns True if the path exists """
    return os.access(path, os.F_OK)

def check_read_permission(path):
    """ Returns True if the user/group can read the path """
    return os.access(path, os.R_OK)

def check_write_permission(path):
    """ Returns True if the user/group can write to the path """
    return os.access(path, os.W_OK)

def check_execute_permission(path):
    """ Returns True if the user/group can execute the path """
    return os.access(path, os.X_OK)
