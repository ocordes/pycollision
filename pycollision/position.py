"""

pycollision/position.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-07-22

"""

from typevalidation.decorator import typevalidate
from typevalidation.types import Vector, Matrix

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
    @typevalidate(isclass=True)
    def rotation(self, val: Matrix):
        zval = zero_matrix.copy()
        zval[:3, :3] = val

        self._matrix = np.dot(zval, self._matrix)

    @property
    def translation(self):
        return self._matrix[:3, 3]

    @translation.setter
    @typevalidate(isclass=True)
    def translation(self, val: Vector):
        self._matrix[:3, 3] += val

        # alternatively
        # zval = zero_matrix
        # zval[3, :3] = val
        # self._matrix *= zval

    @property
    def post_translation(self):
        return self._post_translation

    @post_translation.setter
    @typevalidate(isclass=True)
    def post_translation(self, val: Vector):
        self._post_translation += val

    @typevalidate(isclass=True)
    def calculate_position(self, val: Vector):
        xval = np.array([0., 0., 0., 1.], dtype=np.float64)
        xval[:3] = val

        return np.dot(self._matrix, xval)[:3] + self._post_translation
