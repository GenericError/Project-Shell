""" Checks for permissions for a path/file """

import os

def check_existence(path):
    return os.access(path, os.F_OK)
