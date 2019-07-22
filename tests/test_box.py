"""

tests/test_box.py

written by: Oliver Cordes 2019-07-22
changed by: Oliver Cordes 2019-07-22

"""

from pycollision.objects import Box

import numpy as np


import unittest

from unittest import mock
from unittest.mock import patch
import io


class TestInit(unittest.TestCase):
    # init python list
    def test_test1(self):
        b1 = Box([1, 2, 3], [4, 5, 6])
        p = b1.position

        self.assertEqual(np.all(p[0] == np.array([1., 2., 3.])), True)
        self.assertEqual(np.all(p[1] == np.array([4., 5., 6.])), True)

    # volume calculation and debug
    def test_test100(self):
        b1 = Box([-1, -1, -1], [1, 1, 1])

        self.assertEqual(b1._volume, 8.)

    def test_test101(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            b1 = Box([-1, -1, -1], [1, 1, 1], verbose=True)

        self.assertEqual(fake_stdout.getvalue(),
                         'DEBUG: reference volume: 8.0\n')

    def test_test102(self):
        b1 = Box([-1, -1, -1], [1, 1, 1])

        self.assertEqual(b1.get_volume(), 8.)
