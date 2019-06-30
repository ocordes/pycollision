"""

pycollision/collision.py

written by: Oliver Cordes 2019-06-30
changed by: Oliver Cordes 2019-06-30


"""

import pycollision.objects
from pycollision.debug import debug


import numpy as np


# constants
cmp_atol = 1e-08


class Collision(object):
    def __init__(self):
        pass

    def has_collisions(self, obj, **kwargs):
        if isinstance(self, pycollision.objects.Sphere):
            if isinstance(obj, pycollision.objects.Sphere):
                return coll_sphere2sphere(self, obj, **kwargs)

        raise ValueError('Cannot find any collision procedure' +
                         ' for given types {} and {}'.format(
                                self.__class__.__name__,
                                obj.__class__.__name__))


class CollisionResult(object):
    def __init__(self):
        self._collision = False
        self._data = {}

    def __setitem__(self, idx, val):
        if idx == 'collision':
            self._collision = val
        else:
            self._data[idx] = val

    def __getitem__(self, idx):
        if idx == 'collision':
            return self._collision
        else:
            return self._data[idx]

    def items(self):
        return self._data.items()

    def __call__(self):
        return self._collision

    def __str__(self):
        return '{{collision: {}, data: {}}}'.format(self._collision,
                                                    self._data)


def coll_sphere2sphere(sph1, sph2, **kwargs):
    atol = cmp_atol
    # handle all arguments
    for key, value in kwargs.items():
        if key == 'verbose':
            verbose = value
        elif key == 'atol':
            atol = value

    if verbose:
        debug('calculating collision between two spheres')
    result = CollisionResult()

    # calculate the distance of the two spheres
    distance = np.sqrt(np.sum((sph1.position - sph2.position)**2))

    result['distance'] = distance
    if verbose:
        debug('absolte distance is:', distance)

    distance -= sph1.radius + sph2.radius

    result['outerdistance'] = distance
    if verbose:
        debug('outer distance is:', distance)

    # every outside atol is clear
    if distance < atol:
        result['collision'] = True
    else:
        result['collision'] = np.isclose(distance, 0., atol=atol)

    if verbose:
        debug('collision:', result['collision'])
        debug('Done.')

    return result
