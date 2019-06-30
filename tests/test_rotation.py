from pycollision.rotation import create_rotation_matrix, \
                                    create_rotation_X, \
                                    create_rotation_Y, \
                                    create_rotation_Z

import numpy as np


import unittest


class TestInit(unittest.TestCase):
    # matrix creation with vectors
    def test_test1(self):
        m1 = create_rotation_matrix([1, 0, 0], 180.)
        print(m1)
        m2 = np.array([[1., 0., 0.], [0., -1., 0.], [0., 0., -1.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)

    def test_test2(self):
        m1 = create_rotation_matrix([0, 1, 0], 180.)
        print(m1)
        m2 = np.array([[-1., 0., 0.], [0., 1., 0.], [0., 0., -1.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)

    def test_test3(self):
        m1 = create_rotation_matrix([0, 0, 1], 180.)
        print(m1)
        m2 = np.array([[-1., 0., 0.], [0., -1., 0.], [0., 0., 1.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)

    def test_test4(self):
        m1 = create_rotation_X(90.)
        print(m1)
        m2 = np.array([[1., 0., 0.], [0., 0., -1.], [0., 1., 0.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)

    def test_test5(self):
        m1 = create_rotation_Y(90.)
        print(m1)
        m2 = np.array([[0, 0., 1.], [0., 1., 0.], [-1., 0., 0.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)

    def test_test6(self):
        m1 = create_rotation_Z(90.)
        print(m1)
        m2 = np.array([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
        self.assertEqual(np.all(np.isclose(m1, m2)), True)
