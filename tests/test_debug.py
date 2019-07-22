"""

tests/test_debug.py

written by: Oliver Cordes 2019-07-22
changed by: Oliver Cordes 2019-07-22

"""

from pycollision.debug import debug


import unittest
from unittest import mock
from unittest.mock import patch
import io


class TestDebug(unittest.TestCase):
    """
    Test simple debug output
    """
    def test_debug1(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            debug('Something')

        self.assertEqual(fake_stdout.getvalue(), 'DEBUG: Something\n')

    """
    Test the debug output with more than 1 parameter
    """
    def test_debug1(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            debug(42, 'the answer')

        self.assertEqual(fake_stdout.getvalue(), 'DEBUG: 42 the answer\n')
