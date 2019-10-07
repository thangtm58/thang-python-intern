import unittest
import textwrap
import filecmp

from tests.util import write2file, get_tc_file
from week00_python_basic.challenge01.challenge01b import find_max_claim

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.7229ru1vnyi1
        """

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            invalid_input = '/any/path/not/exist'
            find_max_claim(input=invalid_input, output='any/thing')
        assert str(ec.exception) == f'File {invalid_input} not found'

    def test_tc01(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.c94ptzuqqtop
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
                0
            ''').strip(),
        )
        #endregion

        #region make expected output
        expected_output = f'{tc_file}.expected.out'
        write2file(
            filename = expected_output,
            lines    = textwrap.dedent('').strip(),
        )
        #endregion

        # run testee code
        actual_output = f'{tc_file}.out'
        find_max_claim(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc02(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.w2a1103zyh53
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                4
                0
                -22
                3
                44
            ''').strip(),
        )
        #endregion

        #region make expected output
        expected_output = f'{tc_file}.expected.out'
        write2file(
            filename = expected_output,
            lines    = textwrap.dedent('''
                0
                0
                0
                1
            ''').strip(),
        )
        #endregion

        # run testee code
        actual_output = f'{tc_file}.out'
        find_max_claim(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc03a(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.e3cieiz84v1i
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
               abc
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'N must be an integer number'

    def test_tc03b(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.v5dmpp98umnc
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
               \n
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'N must have a value'

    def test_tc03c(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.rjt0hzegdweo
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        open(valid_input, 'w').close()
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'Invalid input: Empty file'

    def test_tc04a(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.jfgz7yrat44n
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                4
                0
                1
                abc
                2
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'All claim-count must be valid'

    def test_tc04b(self):
        """
        ref. https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.bfnsn71ffq4t
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
                4
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'Claim-count is empty'

