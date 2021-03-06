""" The testing module for Project Shell """

try:
    import unittest
except ImportError:
    print("This script requires the unittest module. Please install it.")

import os
import sys

import cd
import cp
import ls
import man
import mkdir
import printworkingdir
import rm
import rmdir


CURRENT_PYTHON_VERSION = sys.version_info
REQUIRED_PYTHON_VERSION = (3, 3)


class TestCdCommand(unittest.TestCase):
    """ This class tests the cd command """

    def test_supplied_directory(self):
        """ cd /home """
        supplied_directory = "/home"
        exit_code = cd.run_command([], [supplied_directory])
        directory_after_operation = os.getcwd()
        self.assertEqual(supplied_directory, directory_after_operation,
                         msg="cd did not change the directory")
        self.assertEqual(exit_code, 0)

    def test_blank_directory(self):
        """ cd """
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
        test_file = open(test_file_name, 'w')
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
    """ This class tests the cp command
    Most of these just check that the code handles the exception properly"""

    def setUp(self):
        """ Sets up some things for the tests """
        self.testFile = "/tmp/project-shell-cp.testfile"
        try:
            os.remove("/tmp/project-shell-cp/project-shell-cp.testfile")
            os.remove(self.testFile)
        except:
            pass
        self.testFileObject = open(file=self.testFile, mode='w')
        self.thingToWrite = "This is just a test"
        self.testFileObject.write(self.thingToWrite)
        self.testFileObject.close()
        if not os.path.exists("/tmp/project-shell-cp"):
            os.mkdir("/tmp/project-shell-cp")

    def tearDown(self):
        """ Destroys things from previous tests """
        self.testFileObject.close()

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
        exit_code = cp.run_command([], [self.testFile, "/tmp/project-shell-cp"])
        self.assertEqual(exit_code, 6)

    def test_copy_file(self):
        """ cp /tmp/project-shell-cp.testfile /tmp/project-shell-cp/project-shell-cp.testfile """
        exit_code = cp.run_command([], [self.testFile, "/tmp/project-shell-cp/project-shell-cp.testfile"])
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
    """ This class tests the ls command """

    def test_supplied_directory(self):
        """ ls /home """
        exit_code = ls.run_command([], ["/home"])
        self.assertEqual(exit_code, 0)

    def test_blank_directory(self):
        """ ls """
        exit_code = ls.run_command([], [])
        self.assertEqual(exit_code, 0)


class TestManCommand(unittest.TestCase):
    """ This class tests the man command """

    def test_no_input(self):
        """ man """
        exit_code = man.run_command([], [])
        self.assertEqual(exit_code, 1)

    def test_show_help(self):
        """ man -h """
        exit_code = man.run_command([], ['-h'])
        self.assertEqual(exit_code, 0)

    def test_real_command(self):
        """ man cd """
        exit_code = man.run_command([], ['cd'])
        self.assertEqual(exit_code, 0)

    def test_fake_module(self):
        """ man doesnotexist """
        exit_code = man.run_command([], ['doesnotexist'])
        self.assertEqual(exit_code, 2)

    def test_no_documentation(self):
        """ man blank """
        exit_code = man.run_command([], ['blank'])
        self.assertEqual(exit_code, 3)

    def test_command_with_alias(self):
        """ man clear """
        exit_code = man.run_command([], ['exit'])
        self.assertEqual(exit_code, 0)


class TestMkdirCommand(unittest.TestCase):
    """ This class tests the mkdir command """

    def test_create_a_directory(self):
        """ mkdir /tmp/project-shell-mkdir-001 """
        try:
            os.rmdir("/tmp/project-shell-mkdir-001")
        except:
            pass
        exit_code = mkdir.run_command([], ['/tmp/project-shell-mkdir-001'])
        self.assertEqual(exit_code, 0)

    def test_create_a_directory_with_verbose(self):
        """ mkdir -v /tmp/project-shell-mkdir-002 """
        try:
            os.rmdir("/tmp/project-shell-mkdir-002")
        except:
            pass
        exit_code = mkdir.run_command(['-v'], ['/tmp/project-shell-mkdir-002'])
        self.assertEqual(exit_code, 0)

    def test_no_input(self):
        """ mkdir """
        exit_code = mkdir.run_command([], [])
        self.assertEqual(exit_code, 1)

    def test_existing_directory(self):
        """ man /tmp/project-shell-mkdir-already-exists """
        try:
            os.mkdir("/tmp/project-shell-mkdir-already-exists")
        except:
            # Directory is already there
            pass
        exit_code = mkdir.run_command([], ['/tmp/project-shell-mkdir-already-exists'])
        self.assertEqual(exit_code, 2)


class TestPrintWorkingDirectoryCommand(unittest.TestCase):
    """ This class tests the pwd command """

    def test_run_command(self):
        exit_code = printworkingdir.run_command([], [])
        self.assertEqual(exit_code, 0)


class TestRmCommand(unittest.TestCase):
    """ This class tests the rm command
    Most of these just check that the code handles the exception properly"""

    def setUp(self):
        """ Sets up some things for the tests """
        self.testFile = "/tmp/project-shell-rm/project-shell-rm.testfile"
        try:
            os.remove("/tmp/project-shell-rm/project-shell-rm.testfile")
            os.rmdir("/tmp/project-shell-rm")
            os.remove(self.testFile)
        except:
            pass
        os.mkdir("/tmp/project-shell-rm")
        self.testFileObject = open(file=self.testFile, mode='w')
        self.thingToWrite = "This is just a test"
        self.testFileObject.write(self.thingToWrite)
        self.testFileObject.close()

    def tearDown(self):
        """ Destroys things from previous tests """
        self.testFileObject.close()

    def test_no_arguments(self):
        """ rm """
        exit_code = rm.run_command([], [])
        self.assertEqual(exit_code, 1)

    def test_delete_lots_of_files(self):
        """ rm  *.txt"""
        os.chdir("/tmp/project-shell-rm")
        for i in range(1, 10):
            the_file = open(str(i)+".txt", "w")
            the_file.write(str(i))
            the_file.close()
        exit_code = rm.run_command([], ['*.txt'])
        self.assertEqual(exit_code, 0)

    def test_delete_directory(self):
        """ rm /tmp/project-shell-rm """
        exit_code = rm.run_command([], ['/tmp/project-shell-rm'])
        self.assertEqual(exit_code, 2)


class TestRmdirCommand(unittest.TestCase):
    """ This class tests the rmdir command
    Most of these just check that the code handles the exception properly"""

    def test_no_arguments(self):
        """ rmdir """
        exit_code = rmdir.run_command([], [])
        self.assertEqual(exit_code, 1)

    def test_delete_an_empty_folder(self):
        """ rmdir project-shell-rmdir-empty"""
        os.chdir("/tmp/")
        try:
            os.rmdir("/tmp/project-shell-rmdir-empty")
        except:
            pass
        os.mkdir("/tmp/project-shell-rmdir-empty")
        exit_code = rmdir.run_command([], ['project-shell-rmdir-empty'])
        self.assertEqual(exit_code, 0)

    def test_delete_full_folder(self):
        """ rmdir project-shell-rmdir-full """
        os.chdir("/tmp/")
        try:
            os.rmdir("/tmp/project-shell-rmdir-full")
        except:
            pass
        os.mkdir("/tmp/project-shell-rmdir-full")
        os.chdir("/tmp/project-shell-rmdir-full")
        for i in range(1, 10):
            the_file = open(str(i)+".txt", "w")
            the_file.write(str(i))
            the_file.close()
        os.chdir("/tmp/")
        exit_code = rmdir.run_command([], ['project-shell-rmdir-full'])
        self.assertEqual(exit_code, 2)
        os.chdir("/tmp/project-shell-rmdir-full")
        for i in range(1, 10):
            os.remove(str(i)+".txt")


if __name__ == '__main__':
    if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
        print("This version of Python is too old. You require Python 3.3+")
        exit()
    unittest.main()
