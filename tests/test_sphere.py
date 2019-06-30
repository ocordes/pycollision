from pycollision.objects import Sphere

import numpy as np


import unittest


class TestInit(unittest.TestCase):
    # init python list
    def test_test1(self):
        s1 = Sphere([1, 2, 3], 2.)
        self.assertEqual(np.all(s1.position == np.array([1., 2., 3.])), True)

    # init python tuple
    def test_test2(self):
        s1 = Sphere((1, 2, 3), 2.)
        self.assertEqual(np.all(s1.position == np.array([1., 2., 3.])), True)

    # init python strings
    def test_test3(self):
        s1 = Sphere('1,2,3', 2.)
        self.assertEqual(np.all(s1.position == np.array([1., 2., 3.])), True)

    # init numpy array
    def test_test4(self):
        s1 = Sphere(np.array([1, 2, 3]), 2.)
        self.assertEqual(np.all(s1.position == np.array([1., 2., 3.])), True)

    # init python list mixed values
    def test_test5(self):
        s1 = Sphere([1, 2., '3'], 2.)
        self.assertEqual(np.all(s1.position == np.array([1., 2., 3.])), True)

    # exception with wrong parameter
    def test_test6(self):
        with self.assertRaises(TypeError) as context:
            s1 = Sphere('string', 1.)

    # test the radius
    def test_test70(self):
        s1 = Sphere([0, 0, 0], 2.)
        self.assertEqual(s1.radius, 2.)

    def test_test71(self):
        s1 = Sphere([0, 0, 0], 2)
        self.assertEqual(s1.radius, 2.)

    def test_test72(self):
        s1 = Sphere([0, 0, 0], '2')
        self.assertEqual(s1.radius, 2.)

    def test_test73(self):
        with self.assertRaises(TypeError) as context:
            s1 = Sphere([0, 0, 0], 'string')
