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


class TestCpCommand(unittest.TestCase):
    """ This module tests the cp command
    A most of these just check that the code handles the exception properly"""

    def setUp(self):
        """ Sets up some things for the tests """
        self.TestFile = "/tmp/project-shell-cp.testfile"
        try:
            os.remove("/tmp/project-shell-cp/project-shell-cp.testfile")
            os.remove(self.TestFile)
        except:
            pass
        self.TestFileObject = open(file=self.TestFile, mode='w')
        self.ThingToWrite = "This is just a test"
        self.TestFileObject.write(self.ThingToWrite)
        self.TestFileObject.close()
        if not os.path.exists("/tmp/project-shell-cp"):
            os.mkdir("/tmp/project-shell-cp")


    def tearDown(self):
        """ Destroys things from previous tests """
        self.TestFileObject.close()


    def test_no_arguments(self):
        """ cp """
        cp.run_command([], [])

    def test_missing_argument(self):
        """ cp foobar """
        cp.run_command([], ['foobar'])

    def test_equal_source_and_directory(self):
        """ cp foobar foobar """
        cp.run_command([], ['foobar', 'foobar'])

    def test_source_is_a_directory(self):
        """ cp /home foobar """
        cp.run_command([], ['/home', 'foobar'])

    def test_destination_is_a_directory(self):
        """ cp /tmp/project-shell-cp.testfile /tmp """
        cp.run_command([], [self.TestFile, "/tmp/project-shell-cp"])

    def test_copy_file(self):
        """ cp /tmp/project-shell-cp.testfile /tmp/project-shell-cp/project-shell-cp.testfile """
        cp.run_command([], [self.TestFile, "/tmp/project-shell-cp/project-shell-cp.testfile"])
        new_file = open(file="/tmp/project-shell-cp/project-shell-cp.testfile", mode="r")
        new_file_contents = new_file.readlines()[0]
        self.assertEqual(new_file_contents, "This is just a test")
        new_file.close()

if __name__ == '__main__':
    unittest.main()
