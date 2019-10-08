import unittest
import textwrap
import filecmp

from tests.util import write2file, get_tc_file
from week00_python_basic.challenge01.challenge01 import find_min


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now


    def test_tc00(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.hdbeb7ctivvb
        """

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            invalid_input = '/any/path/not/exist'
            find_min(input=invalid_input, output='any/thing')
        assert str(ec.exception) == f'File {invalid_input} not found'

    def test_tc01(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.ej3k2ud0bk6m
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
            1 
            22
            333
            44 
            55
            66
            ''').strip(),
        )
        #endregion

        #region make expected output
        expected_output = f'{tc_file}.expected.out'
        write2file(
            filename=expected_output,
            lines=textwrap.dedent('1').strip(),
        )
        #endregion

        # run testee code
        actual_output = f'{tc_file}.out'
        find_min(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc02(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.bn49fls8npyl
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
                1
                22
                333            
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/any/thing/'
            find_min(input=valid_input, output=actual_output)
        assert str(ec.exception) == f'Invalid input: List of numbers should have 6 numbers'

    def test_tc03a(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.1a6jj95xd435
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
                1
                22
                333 
                44 
                555
                a
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_min(input=valid_input, output=actual_output)
        assert str(ec.exception) == f'Invalid input: The item in the list must be a number'

    def test_tc03b(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.r0torxrmg9uh
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            find_min(input=valid_input, output='any/thing')
        assert str(ec.exception) == f'Invalid input: Empty file with empty String'

    def test_tc03c(self):
        """
        ref. https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.a6tazu4n6psx
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        open(valid_input, 'w').close()
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            find_min(input=valid_input, output='any/thing')
        assert str(ec.exception) == f'Invalid input: Empty file'
