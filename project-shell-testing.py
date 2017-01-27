""" The testing module for all of Project Shell """

try:
    import unittest
except ImportError:
    print("This script requires the unittest module. Please install it.")

import os
import cd
import cp

class TestCdCommand(unittest.TestCase):
    """ This module tests the cd command """

    def test_supplied_directory(self):
        """ cd /home """
        original_directory = os.getcwd()
        supplied_directory = "/home"
        cd.run_command([], [supplied_directory])
        directory_after_operation = os.getcwd()
        self.assertEqual(supplied_directory, directory_after_operation,
                         msg="cd did not change the directory")

    def test_blank_directory(self):
        """ cd """
        original_directory = os.getcwd()
        cd.run_command([], [])
        directory_after_operation = os.getcwd()
        path_wanted = os.path.expanduser('~')
        self.assertEqual(path_wanted, directory_after_operation,
                         msg="cd did not change the directory")


class TestClearCommand(unittest.TestCase):
    """ This module doesn't really 'test' anything -
    in fact it will only fail if there is a syntax error """

    def test_import(self):
        """ Tests the import of the module """
        import cleartheshell


if __name__ == '__main__':
    unittest.main()
