"""

tests/test_position.py

written by: Oliver Cordes 2019-07-22
changed by: Oliver Cordes 2019-07-22

"""

from pycollision.position import Position
from pycollision.rotation import create_rotation_matrix, \
                                    create_rotation_X, \
                                    create_rotation_Y, \
                                    create_rotation_Z


import unittest
from unittest import mock
from unittest.mock import patch
import io

import numpy as np


class TestPosition(unittest.TestCase):
    # single translation
    def test_test1(self):
        p = Position()

        p.translation = [1, 2, 3]

        self.assertEqual(np.all(p.translation == np.array([1., 2., 3.])), True)

    # double translation
    def test_test2(self):
        p = Position()

        p.translation = [1, 2, 3]

        p.translation = [3, -1, -10]

        v = np.array([4., 1., -7.])
        self.assertEqual(np.all(p.translation == v), True)

    # single rotation
    def test_test10(self):
        p = Position()

        p.rotation = create_rotation_X(90.)

        m2 = np.array([[1., 0., 0.], [0., 0., -1.], [0., 1., 0.]])
        self.assertEqual(np.all(np.isclose(p.rotation, m2)), True)

    # double rotation
    def test_test11(self):
        p = Position()

        p.rotation = create_rotation_X(90.)
        p.rotation = create_rotation_Y(90.)

        m2 = np.array([[0., 1., 0.], [0., 0., -1.], [-1., 0., 0.]])
        self.assertEqual(np.all(np.isclose(p.rotation, m2)), True)

    # single post_translation
    def test_test20(self):
        p = Position()

        p.post_translation = [1, 2, 3]

        v2 = np.array([1., 2., 3.])
        self.assertEqual(np.all(np.isclose(p.post_translation, v2)), True)

    # double post_translation
    def test_test21(self):
        p = Position()

        p.post_translation = [1, 2, 3]
        p.post_translation = [-2, 3, -10]

        v2 = np.array([-1., 5., -7.])
        self.assertEqual(np.all(np.isclose(p.post_translation, v2)), True)
