# Created in response to issue #32

""" Implements permission based functions for a path/file """

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

def permission_aware_open(path, mode):
    """ Returns a file object, checking for appropriate permissions before doing so """
    ok = False
    if check_existence(path):
        if mode == "r":
            if check_read_permission(path):
                ok = True
        elif mode == "w":
            if check_read_permission(path):
                if check_write_permission(path):
                    ok = True
    if ok:
        return open(path, mode=mode)
