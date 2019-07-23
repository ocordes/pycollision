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

        if isinstance(self, pycollision.objects.Box):
            if isinstance(obj, pycollision.objects.Box):
                return coll_box2box(self, obj, **kwargs)

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
    verbose = False
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
        debug(' absolute distance is: %g' % distance)

    distance -= sph1.radius + sph2.radius

    result['outerdistance'] = distance
    if verbose:
        debug(' outer distance is: %g' % distance)

    # every outside atol is clear
    if distance < atol:
        result['collision'] = True
    else:
        result['collision'] = np.isclose(distance, 0., atol=atol)

    if verbose:
        debug(' collision:', result['collision'])
        debug('Done.')

    return result


def box_inside_box(box1, box2, atol, verbose):
    # the algorithm based on the assumption that we can check if
    # all corner points of box1 are not in box2 the box1 has no
    # overlap with box2 (true, but one has to check the other way
    # as well)!

    for i in box1._corners:
        i = box1.calculate_position(i)
        vol = box2.get_volume(center=i)
        if verbose:
            debug(' c=%s vol=%g vol_ref=%g' % (i, vol, box2._volume))
        if np.isclose(vol, box2._volume, rtol=atol, atol=atol):
            return True

    return False


def coll_box2box(box1, box2, **kwargs):
    atol = cmp_atol
    verbose = False
    # handle all arguments
    for key, value in kwargs.items():
        if key == 'verbose':
            verbose = value
        elif key == 'atol':
            atol = value

    if verbose:
        debug('calculating collision between two boxes')
        debug(' atol=%g' % atol)
    result = CollisionResult()

    collision = box_inside_box(box1, box2, atol, verbose)
    if not collision:
        collision = box_inside_box(box2, box1, atol, verbose)

    result['collision'] = collision

    if verbose:
        debug('collision:', result['collision'])
        debug('Done.')

    return result
