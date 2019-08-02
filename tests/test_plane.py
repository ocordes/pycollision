"""

tests/test_plane.py

written by: Oliver Cordes 2019-07-26
changed by: Oliver Cordes 2019-07-27

"""

from pycollision.objects3d import Plane
from pycollision.planes import create_xy_plane, create_xz_plane, \
                               create_yz_plane
from pycollision.rotation import create_rotation_matrix, \
                                    create_rotation_X, \
                                    create_rotation_Y, \
                                    create_rotation_Z

import numpy as np


import unittest

from unittest import mock
from unittest.mock import patch
import io


class TestInit(unittest.TestCase):
    # test xy plane
    def test_test1(self):
        p1 = create_xy_plane(1)

        v = np.array([0., 0., 1.])

        self.assertEqual(p1.distance, 1.)
        self.assertEqual(np.all(p1.norm_vector == v), True)

    # test xz plane
    def test_test2(self):
        p1 = create_xz_plane(1)

        v = np.array([0., 1., 0.])

        self.assertEqual(p1.distance, 1.)
        self.assertEqual(np.all(p1.norm_vector == v), True)

    # test yz plane
    def test_test3(self):
        p1 = create_yz_plane(1)

        v = np.array([1., 0., 0.])

        self.assertEqual(p1.distance, 1.)
        self.assertEqual(np.all(p1.norm_vector == v), True)

    # test yz plane + translation parallel to norm vector
    def test_test4(self):
        p1 = create_yz_plane(1)
        p1.translation = [1, 0., 0.]

        v = np.array([1., 0., 0.])

        self.assertEqual(np.isclose(p1.distance, 2.), True)
        self.assertEqual(np.all(p1.norm_vector == v), True)

    # test yz plane + translation to another direction
    def test_test4(self):
        p1 = create_yz_plane(1)
        p1.translation = [1, -100, 22000.]

        v = np.array([1., 0., 0.])

        self.assertEqual(np.isclose(p1.distance, 2.), True)
        self.assertEqual(np.all(p1.norm_vector == v), True)


class TestCollision(unittest.TestCase):
    # 2 xy planes with difference = 1
    def test_test1(self):
        p1 = create_xy_plane(0)
        p2 = create_xy_plane(1)

        result = p1.has_collisions(p2)

        self.assertEqual(result['collision'], False)

    # xy and yz collision
    def test_test2(self):
        p1 = create_xy_plane(0)
        p2 = create_yz_plane(1)

        result = p1.has_collisions(p2)

    # 2 xy planes parallel to test atol
    def test_test10(self):
        p1 = create_xy_plane(0)
        p2 = create_xy_plane(1e-5)

        result = p1.has_collisions(p2, atol=1e-4)

        self.assertEqual(result['collision'], True)

    def test_test11(self):
        p1 = create_xy_plane(0)
        p2 = create_xy_plane(1e-5)

        result = p1.has_collisions(p2, atol=1e-6)

        self.assertEqual(result['collision'], False)

    # test all parameters for has_collisions
    def test_test20(self):
        p1 = create_xy_plane(0)
        p2 = create_yz_plane(1)

        result = p1.has_collisions(p2, verbose=True, item='value')

    # test of collision with not collision objects
    def test_test100(self):
        p1 = create_xy_plane(0)
        i = 1  # int object

        with self.assertRaises(ValueError) as context:
            result = p1.has_collisions(i)
