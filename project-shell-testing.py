""" The testing module for all of Project Shell """

try:
    import unittest
except ImportError:
    print("This script requires the unittest module. Please install it.")

import os
import cd
import cp
import ls


class TestCdCommand(unittest.TestCase):
    """ This module tests the cd command """

    def test_supplied_directory(self):
        """ cd /home """
        original_directory = os.getcwd()
        supplied_directory = "/home"
        exit_code = cd.run_command([], [supplied_directory])
        directory_after_operation = os.getcwd()
        self.assertEqual(supplied_directory, directory_after_operation,
                         msg="cd did not change the directory")
        self.assertEqual(exit_code, 0)

    def test_blank_directory(self):
        """ cd """
        original_directory = os.getcwd()
        exit_code = cd.run_command([], [])
        directory_after_operation = os.getcwd()
        path_wanted = os.path.expanduser('~')
        self.assertEqual(path_wanted, directory_after_operation,
                         msg="cd did not change the directory")
        self.assertEqual(exit_code, 0)

    def test_change_into_file(self):
        """ cd project-shell-test-file.txt"""
        os.chdir("/tmp")
        test_file_name = 'project-shell-test-cd-into-file.txt'
        test_file = open(test_file_name,'w')
        test_file.write('testing')
        test_file.close()
        exit_code = cd.run_command([], [test_file_name])
        self.assertEqual(exit_code, 2)



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
        exit_code = cp.run_command([], [])
        self.assertEqual(exit_code, 1)

    def test_missing_argument(self):
        """ cp foobar """
        exit_code = cp.run_command([], ['foobar'])
        self.assertEqual(exit_code, 1)

    def test_equal_source_and_directory(self):
        """ cp foobar foobar """
        exit_code = cp.run_command([], ['foobar', 'foobar'])
        self.assertEqual(exit_code, 4)

    def test_source_is_a_directory(self):
        """ cp /home foobar """
        exit_code = cp.run_command([], ['/home', 'foobar'])
        self.assertEqual(exit_code, 5)

    def test_destination_is_a_directory(self):
        """ cp /tmp/project-shell-cp.testfile /tmp """
        exit_code = cp.run_command([], [self.TestFile, "/tmp/project-shell-cp"])
        self.assertEqual(exit_code, 6)

    def test_copy_file(self):
        """ cp /tmp/project-shell-cp.testfile /tmp/project-shell-cp/project-shell-cp.testfile """
        exit_code = cp.run_command([], [self.TestFile, "/tmp/project-shell-cp/project-shell-cp.testfile"])
        new_file = open(file="/tmp/project-shell-cp/project-shell-cp.testfile", mode="r")
        new_file_contents = new_file.readlines()[0]
        self.assertEqual(new_file_contents, "This is just a test")
        self.assertEqual(exit_code, 0)
        new_file.close()


class TestExitCommand(unittest.TestCase):
    """ This module doesn't really 'test' anything -
    in fact it will only fail if there is a syntax error """

    def test_import(self):
        """ Tests the import of the module """
        import exittheshell


class TestLsCommand(unittest.TestCase):
    """ This module tests the ls command """

    def test_supplied_directory(self):
        """ ls /home """
        exit_code = ls.run_command([], ["/home"])
        self.assertEqual(exit_code, 0)

    def test_blank_directory(self):
        """ ls """
        exit_code = ls.run_command([], [])
        self.assertEqual(exit_code, 0)

if __name__ == '__main__':
    unittest.main()
