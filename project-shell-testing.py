""" The testing module for all of Project Shell """

try:
    import unittest
except ImportError:
    print("This script requires the unittest module. Please install it.")

import os
import cd

class TestCdCommand(unittest.TestCase):
    """ This module tests the cd command """

    def test_with_supplied_directory(self):
        """ cd /home """
        original_directory = os.getcwd()
        supplied_directory = "/home"
        cd.run_command([], [supplied_directory])
        directory_after_operation = os.getcwd()
        self.assertEqual(supplied_directory, directory_after_operation,
                         msg="cd did not change the directory")

    def test_with_blank_directory(self):
        """ cd """
        original_directory = os.getcwd()
        cd.run_command([], [])
        directory_after_operation = os.getcwd()
        path_wanted = os.path.expanduser('~')
        self.assertEqual(path_wanted, directory_after_operation,
                         msg="cd did not change the directory")



if __name__ == '__main__':
    unittest.main()
