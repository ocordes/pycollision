"""

pycollision/position.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-06-30

"""

from pycollision.utils import input2vector, input2matrix

import numpy as np


zero_matrix = np.array([[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]], dtype=np.float64)


class Position(object):
    def __init__(self):
        self._matrix = zero_matrix.copy()
        self._post_translation = np.array([0., 0., 0.], dtype=np.float64)

    @property
    def rotation(self):
        return self._matrix[:3, :3]

    @rotation.setter
    def rotation(self, val):
        val = input2matrix(val)
        zval = zero_matrix.copy()
        zval[:3, :3] = val

        self._matrix = np.dot(zval, self._matrix)

    @property
    def translation(self):
        return self._matrix[3, :3]

    @translation.setter
    def translation(self, val):
        val = input2vector(val)

        self._matrix[:3, 3] += val

        # alternatively
        # zval = zero_matrix
        # zval[3, :3] = val
        # self._matrix *= zval

    @property
    def post_translation(self):
        return self._post_translation

    @post_translation.setter
    def post_translation(self, val):
        val = input2vector(val)
        self._post_translation += val

    def calculate_position(self, val):
        xval = np.array([0., 0., 0., 1.], dtype=np.float64)
        xval[:3] = val

        return np.dot(self._matrix, xval)[:3] + self._post_translation
