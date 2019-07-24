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
    def test_test10(self):
        b1 = Box([-1, -1, -1], [1, 1, 1])

        self.assertEqual(b1._volume, 8.)

    def test_test11(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            b1 = Box([-1, -1, -1], [1, 1, 1], verbose=True)

        self.assertEqual(fake_stdout.getvalue(),
                         'DEBUG: reference volume: 8.0\n')

    def test_test12(self):
        b1 = Box([-1, -1, -1], [1, 1, 1])

        self.assertEqual(b1.get_volume(), 8.)


class TestCollision(unittest.TestCase):
    # test 2 boxes without collision
    def test_test1(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([2, 0, 0], [3, 1, 1])

        result = b1.has_collisions(b2)

        self.assertEqual(result['collision'], False)

    # test 2 boxes with collision
    def test_test2(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [0.5, 0, 0]

        result = b1.has_collisions(b2)

        self.assertEqual(result['collision'], True)

    # test 2 boxes touching eacch other
    def test_test3(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]

        result = b1.has_collisions(b2)

        self.assertEqual(result['collision'], True)

    # test 2 boxes touching eacch other, the second box smaller
    # than the first one
    def test_test4(self):
        b1 = Box([0, -1, -1], [1, 2, 2])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]

        result = b1.has_collisions(b2)

        self.assertEqual(result['collision'], True)

    # verbose test
    def test_test5(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]

        result = b1.has_collisions(b2, verbose=True)

        self.assertEqual(result['collision'], True)

    # atol difference tests
    def test_test6(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]
        b2.translation = [1e-4, 0, 0]

        result = b1.has_collisions(b2, atol=1e-4)

        self.assertEqual(result['collision'], True)

    def test_test7(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]
        b2.translation = [1e-4, 0, 0]

        result = b1.has_collisions(b2, verbose=True, atol=1e-5)

        self.assertEqual(result['collision'], False)

    # additional useless parameter for has_collisions
    def test_test7(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        b2 = Box([0, 0, 0], [1, 1, 1])
        b2.translation = [1, 0, 0]
        b2.translation = [1e-4, 0, 0]

        result = b1.has_collisions(b2, verbose=True, atol=1e-5, item='value')

        self.assertEqual(result['collision'], False)

    # test of collision with not collision objects
    def test_test100(self):
        b1 = Box([0, 0, 0], [1, 1, 1])
        i = 1  # int object

        with self.assertRaises(ValueError) as context:
            result = b1.has_collisions(i)
