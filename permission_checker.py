""" Checks for permissions for a path/file """

import os

def check_existence(path):
    return os.access(path, os.F_OK)

def check_read_permission(path):
    return os.access(path, os.R_OK)
