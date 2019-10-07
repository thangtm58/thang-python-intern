import unittest
import textwrap
import filecmp

from tests.util import write2file, get_tc_file
from week00_python_basic.challenge02_w_class.challenge02_w_class import insurance_policies

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.q1lpunwc78v8
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename=valid_input,
            lines=textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
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
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output) is True


    def test_tc01_tc02(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.4g8u3yvsoc7f
        """
        tc_file=get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                2
                S122333aG aN vaN nguyeN 1985-01-24 500 2   
                S122333aG binh thi tran 1986-01-23 500 0
            ''').strip(),
        )
        #endregion

        #region make expected output
        expected_output = f'{tc_file}.expected.out'
        write2file(
            filename = expected_output,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                S122333aG, An V. NGUYEN, 34, 1500
                S122333aG, Binh T. TRAN, 33, 500
            ''').strip(),
        )
        #endregion

        # run testee code
        actual_output = f'{tc_file}.out'
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output) is True


    def test_tc03_tc04(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.7r8ck1i20run
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                2
                S122333aG thuOnG bInh vU 2000-01-23 500 1   
                S122333aG triNH Do CAO 2000-04-23 500 2
            ''').strip(),
        )
        #endregion

        #region make expected output
        expected_output = f'{tc_file}.expected.out'
        write2file(
            filename = expected_output,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                S122333aG, Thuong B. VU, 19, 1000
                S122333aG, Trinh D. CAO, 19, 1500
            ''').strip(),
        )
        #endregion

        # run testee code
        actual_output = f'{tc_file}.out'
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output) is True

    def test_tc05a(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.vn2rpimh9xvp
        """
        tc_file = get_tc_file(self)

        #region make input
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                1 an van nguyen 1999-01-22 500 0
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'n must be a string'

    def test_tc05b(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.4or02ub25guj
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                empty an van nguyen 1999-01-22 500 0
            ''').strip().replace("empty", ''),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'n must have a value'

    def test_tc06a(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.avsqnj1qeba3
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG 0 @@ thai$ 1990-02-11 500 0
            ''').strip().replace("empty", ''),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must be a string'

    def test_tc06b(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.y618786kmtie
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG ab1cd ab1cd ab1cd 1990-02-11 500 0
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must not include number'

    def test_tc06c(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.djcmn0dlr5f3
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG       1990-02-11 500 0
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must have a value'

    def test_tc07a(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.aptazpl02c30
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG trinh do cao abcd-12-34 500 2
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'd must be a date i.e. yyyy-mm-dd'

    def test_tc07b(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.z8vx14fyvskh
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG thuong binh vu  500 1
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'd must have a value'

    def test_tc08a(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.79gt5un0wtc2
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG binh thi tran 1990-02-11 -500 0
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'p must be a positive float number'

    def test_tc08b(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.d5q872q8kj3l
        """
        tc_file = get_tc_file(self)

        # region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG binh thi tran 1990-02-11   0
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'p must have a value'

    def test_tc09a(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.8gw4r2c1oftj
        """
        tc_file = get_tc_file(self)

        #region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG trinh do cao 2000-02-11 500 abc
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'c must be a not-negative integer'

    def test_tc09b(self):
        """
        ref. https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.g2o57ezfn79p
        """
        tc_file = get_tc_file(self)

        # region make input file
        valid_input = f'{tc_file}.input'
        write2file(
            filename = valid_input,
            lines    = textwrap.dedent('''
                nricfin first_name middle_name last_name date_of_birth premium claim_count
                1
                S122333bG trinh do cao 2000-02-11 500 empty
            ''').strip(),
        )
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = f'{tc_file}.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'c must have a value'

