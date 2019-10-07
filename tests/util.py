import platform
import tempfile


TMP='/tmp' if platform.system() == 'Darwin' else tempfile.gettempdir()  # ref. https://stackoverflow.com/a/43418319/248616


def write2file(filename: 'path as str', lines: str)-> 'write :lines to :filename':
    with open(filename, 'w') as f:
        print(lines, file=f)


def get_tc_file(self):
    """
    generate tc file path from unittest method
    eg
    unittest method at
        tests.test_2.Test.test_tc01_tc02()
    will generate file path as
        /tmp/test_tc01_tc02

    **note**
    tc aka testcase
    param :self is the unittest method's self param
    """
    return f'{TMP}/{self._testMethodName}'
