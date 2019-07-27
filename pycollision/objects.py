"""

pycollision/objects.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-07-26

"""

from pycollision.position import Position
from pycollision.collision import Collision
from pycollision.geometry import projection_vector, pyramid_volume
from pycollision.debug import debug


from typevalidation.decorator import typevalidate
from typevalidation.types import PosInt, PosFloat, Vector

import numpy as np
import numpy.linalg as nl

# every object needs


class BasicObject(Position, Collision):
    def __init__(self, verbose=False):
        Position.__init__(self)
        Collision.__init__(self)

        self._verbose = verbose


class Sphere(BasicObject):
    @typevalidate(isclass=True)
    def __init__(self, x: Vector, radius: PosFloat, verbose: bool=False):
        BasicObject.__init__(self, verbose=verbose)
        self._x = x
        self._radius = radius

    @property
    def position(self):
        return self.calculate_position(self._x)

    @property
    def radius(self):
        return self._radius

    def __repr__(self):
        return 'Sphere({}, {})'.format(self._x.__repr__(), self._radius)


class Box(BasicObject):
    @typevalidate(isclass=True)
    def __init__(self, x1: Vector, x2: Vector, verbose: bool=False):
        BasicObject.__init__(self, verbose=verbose)
        self._x1 = x1
        self._x2 = x2

        self._center = (x2 - x1) / 2.

        self._six, self._corners = self.get_box_planes_and_corners(self._x1,
                                                                   self._x2)

        self._volume = self.get_volume(self._center)

        if self._verbose:
            debug('reference volume:', self._volume)

    @property
    def position(self):
        return [self.calculate_position(self._x1),
                self.calculate_position(self._x2)]

    @property
    def corners(self):
        return [self.calculate_position(i) for i in self._corners]

    def get_box_planes_and_corners(self, x1, x2):
        a = np.array([x1[0], x1[1], x1[2]])
        b = np.array([x2[0], x1[1], x1[2]])
        c = np.array([x2[0], x1[1], x2[2]])
        d = np.array([x1[0], x1[1], x2[2]])
        e = np.array([x1[0], x2[1], x1[2]])
        f = np.array([x2[0], x2[1], x1[2]])
        g = np.array([x2[0], x2[1], x2[2]])
        h = np.array([x1[0], x2[1], x2[2]])
        s1 = [a, d, e, h]
        s2 = [a, b, f, e]
        s3 = [b, c, g, f]
        s4 = [d, c, g, h]
        s5 = [a, b, c, d]
        s6 = [e, f, g, h]

        return [s1, s2, s3, s4, s5, s6], [a, b, c, d, e, f, g, h]

    def get_six_plane_corrected(self):
        nsix = []
        for i in self._six:
            ni = []
            for j in i:
                nj = self.calculate_position(j)
                ni.append(nj)
            nsix.append(ni)

        return nsix

    def get_volume(self, center=None):
        if center is None:
            center = self.calculate_position(self._center)
        six = self.get_six_plane_corrected()

        vol = 0.
        for i in six:
            # vol += self.get_single_volume(i, center)
            vol += pyramid_volume(i, center)
        return vol


class Plane(BasicObject):
    @typevalidate(isclass=True)
    def __init__(self, n: Vector, d: float, verbose: bool=False):
        BasicObject.__init__(self, verbose=verbose)
        self._n = n
        self._d = d

    @property
    def norm_vector(self):
        # calculate_position is not the right procedure here
        # we need only the rotation applied to the norm_vector
        return np.dot(self.rotation, self._n)

    @property
    def distance(self):
        # the distance is a little bit crucial ...
        # first we need the total translation
        trans = self.translation + self.post_translation
        # now we need the current norm vector
        nv = self.norm_vector
        # calculate the part of the translation vector parallel
        # to the norm vector
        tnv = projection_vector(trans, nv)

        return self._d + nl.norm(tnv)
