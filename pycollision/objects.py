"""

pycollision/objects.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-07-22

"""

from pycollision.position import Position
from pycollision.collision import Collision
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

    def get_single_volume(self, plane, height):
        v1 = plane[0] - plane[1]
        v2 = plane[0] - plane[2]

        # the height vector on one edge of the pyramid
        hv = height - plane[0]

        # normal vector of the plane
        nv = np.cross(v1, v2)
        # the normalization of the normal vector
        # is equal to the area of the plane
        nnv = nl.norm(nv)

        # the projected height vector in the center
        phv = np.dot(hv, nv) / nnv
        # scalar height of the pyramid
        nh = nl.norm(phv)

        return nnv * nh / 3.

    def get_volume(self, center=None):
        if center is None:
            center = self.calculate_position(self._center)
        six = self.get_six_plane_corrected()

        vol = 0.
        for i in six:
            vol += self.get_single_volume(i, center)
        return vol


class Plane(BasicObject):
    def __init__(self):
        BasicObject.__init__(self)
