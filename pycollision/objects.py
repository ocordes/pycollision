"""

pycollision/objects.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-06-29

"""

from pycollision.position import Position

from pycollision.utils import input2position, input2float


# every object needs

class BasicObject(Position):
    pass



class Sphere(BasicObject):
    def __init__(self, x, radius):
        self._x = input2position(x)
        self._radius = input2float(radius)


    def _real_position(self):
        return self._x


    @property
    def position(self):
        return self._real_position()


    @property
    def radius(self):
        return self._radius


class Box(BasicObject):
    def __init__(self):
        pass



class Plane(BasicObject):
    def __init__(self):
        pass
