"""

tests/test_debug.py

written by: Oliver Cordes 2019-07-25
changed by: Oliver Cordes 2019-07-25

"""

from pycollision.geometry import *


import unittest
from unittest import mock
from unittest.mock import patch
import io

import numpy as np


class Test_projection_vector(unittest.TestCase):
    # test with a reference vector parallel to the test vector
    # reference vector is normalized
    def test_test1(self):
        n1 = np.array([1., 0., 0.])

        v = n1 * 2.

        res = projection_vector(v, n1)

        self.assertEqual(np.all(np.isclose(res, v)), True)

    # test with a reference vector parallel to the test vector
    # reference vector is not normalized
    def test_test2(self):
        n1 = np.array([2., 0., 0.])

        v = n1 * 2.

        res = projection_vector(v, n1)

        self.assertEqual(np.all(np.isclose(res, v)), True)

    # test with a reference vector perpendicular to the test vector
    # reference vector is normalized
    def test_test3(self):
        n1 = np.array([1., 0., 0.])

        v = np.array([0., 1., 1.])

        res = projection_vector(v, n1)

        res_cmp = np.array([0., 0., 0.])

        self.assertEqual(np.all(np.isclose(res, res_cmp)), True)

    # test with a reference vector perpendicular to the test vector
    # reference vector is not normalized
    def test_test4(self):
        n1 = np.array([2., 0., 0.])

        v = np.array([0., 1., 1.])

        res = projection_vector(v, n1)

        res_cmp = np.array([0., 0., 0.])

        self.assertEqual(np.all(np.isclose(res, res_cmp)), True)


class Test_pyramid_volume(unittest.TestCase):
    # calculate a perfect pyramid with the top directly over the
    # center of the plane
    def test_test1(self):
        a = np.array([0., 0., 0.])
        b = np.array([1., 0., 0.])
        c = np.array([1., 0., 1.])
        d = np.array([0., 0., 1.])

        # generate a 1x1 plane
        plane = [a, b, c, d]

        center = np.array([0.5, 3, 0.5])

        self.assertEqual(np.isclose(pyramid_volume(plane, center), 1.0), True)

    # calculate a perfect pyramid with the top somwhere away from
    # the plane
    def test_test2(self):
        a = np.array([0., 0., 0.])
        b = np.array([1., 0., 0.])
        c = np.array([1., 0., 1.])
        d = np.array([0., 0., 1.])

        # generate a 1x1 plane
        plane = [a, b, c, d]

        center = np.array([-100, 3, 100])

        self.assertEqual(np.isclose(pyramid_volume(plane, center), 1.0), True)
