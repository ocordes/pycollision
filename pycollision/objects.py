"""

pycollision/objects.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-06-29

"""

from pycollision.position import Position

from pycollision.utils import input2vector, input2float


from pycollision.collision import Collision

from typevalidation.decorator import typevalidate
from typevalidation.types import PosInt, Vector

import numpy as np


# every object needs

class BasicObject(Position, Collision):
    def __init__(self):
        Position.__init__(self)
        Collision.__init__(self)


class Sphere(BasicObject):
    @typevalidate(isclass=True)
    def __init__(self, x:Vector, radius:float, debug:bool=False):
        BasicObject.__init__(self)
        self._x = input2vector(x)
        self._radius = input2float(radius)

    @property
    def position(self):
        return self.calculate_position(self._x)

    @property
    def radius(self):
        return self._radius

    def __repr__(self):
        return 'Sphere({}, {})'.format(self._x.__repr__(), self._radius)


class Box(BasicObject):
    def __init__(self, x, y):
        BasicObject.__init__(self)


class Plane(BasicObject):
    def __init__(self):
        BasicObject.__init__(self)
