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


class TestCollision(unittest.TestCase):
    # test 2 spheres no collision
    def test_test1(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([10, 0, 0], 1.)

        result = s1.has_collisions(s2)

        self.assertEqual(result['collision'], False)

    # test 2 spheres with collision
    def test_test1(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([1, 0, 0], 1.)

        result = s1.has_collisions(s2)

        self.assertEqual(result['collision'], True)

    # test 2 spheres are touching each other
    def test_test1(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([2, 0, 0], 1.)

        result = s1.has_collisions(s2)

        self.assertEqual(result['collision'], True)

    # test 2 spheres almost touching, verbose testing
    def test_test1(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([2, 0, 0], 1.)

        result = s1.has_collisions(s2, verbose=True)

        self.assertEqual(result['collision'], True)

    # test 2 spheres almost touching with atol -> collision
    def test_test3(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([2, 0, 0], 1.)
        s2.translation = [1e-4, 0, 0]

        result = s1.has_collisions(s2, atol=1e-3)

        self.assertEqual(result['collision'], True)

    def test_test4(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([2, 0, 0], 1.)
        s2.translation = [1e-4, 0, 0]

        result = s1.has_collisions(s2, atol=1e-5)

        self.assertEqual(result['collision'], False)

    # additional parameter for has_collisions
    def test_test5(self):
        s1 = Sphere([0, 0, 0], 1.)
        s2 = Sphere([2, 0, 0], 1.)
        s2.translation = [1e-4, 0, 0]

        result = s1.has_collisions(s2, atol=1e-5, item='value')

        self.assertEqual(result['collision'], False)

    # test of collision with not collision objects
    def test_test100(self):
        s1 = Sphere([0, 0, 0], 1.)
        i = 1  # int object

        with self.assertRaises(ValueError) as context:
            result = s1.has_collisions(i)
