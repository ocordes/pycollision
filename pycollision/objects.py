"""

pycollision/objects.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-06-29

"""

from pycollision.position import Position

from pycollision.utils import input2position, input2float


# every object needs

class BasicObject(Position):
    def __init__(self):
        Position.__init__(self)



class Sphere(BasicObject):
    def __init__(self, x, radius):
        BasicObject.__init__(self)
        self._x = input2position(x)
        self._radius = input2float(radius)


    @property
    def position(self):
        return self.calculate_position(self._x)


    @property
    def radius(self):
        return self._radius



class Box(BasicObject):
    def __init__(self, x, y):
        BasicObject.__init__(self)



class Plane(BasicObject):
    def __init__(self):
        BasicObject.__init__(self)
        
