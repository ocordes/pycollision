#
# pycollision/collision.py
#
# written by: Oliver Cordes 2019-06-30
# changed by: Oliver Cordes 2019-08-02
#
"""

This module defines all 3d collision routines

"""
import sys

try:
    import pycollision.objects3d
except:
    pass


from pycollision.debug import debug
from pycollision.geometry import *

import numpy as np


# constants
cmp_atol = 1e-08


class Collision(object):
    """
    The collision object, provides only the member has_collisions.
    """
    def __init__(self):
        pass

    def has_collisions(self, obj, **kwargs):
        """

        calls the external collision functions

        Parameters
        ----------
        obj:
            the object to test for collision
        kwargs:
            additional named parameters which were redirected to
            the collision functions

        Raises
        ------
        ValueError
            will be raised if obj doesn't fit to any collision
            functions

        """
        if isinstance(self, pycollision.objects3d.Sphere):
            if isinstance(obj, pycollision.objects3d.Sphere):
                return coll_sphere2sphere(self, obj, **kwargs)
            elif isinstance(obj, pycollision.objects3d.Plane):
                return coll_sphere2plane(self, obj, **kwargs)

        if isinstance(self, pycollision.objects3d.Box):
            if isinstance(obj, pycollision.objects3d.Box):
                return coll_box2box(self, obj, **kwargs)
            elif isinstance(obj, pycollision.objects3d.Plane):
                return coll_box2plane(self, obj, **kwargs)

        if isinstance(self, pycollision.objects3d.Plane):
            if isinstance(obj, pycollision.objects3d.Plane):
                return coll_plane2plane(self, obj, **kwargs)
            elif isinstance(obj, pycollision.objects3d.Sphere):
                return coll_sphere2plane(obj, self, **kwargs)
            elif isinstance(obj, pycollision.objects3d.Box):
                return coll_box2plane(obj, self, **kwargs)

        raise ValueError('Cannot find any collision procedure' +
                         ' for given types {} and {}'.format(
                                self.__class__.__name__,
                                obj.__class__.__name__))


class CollisionResult(object):
    """
    The CollisionResult object which provides the results of
    the collision test. It works like a normal Python
    dictionary. The only item which is always available is
    'collision'. All additional data are different for different
    collision types.

    Attributes
    ----------
    _collision: bool
        hold the collision result
    _data: dict
        additional information
    """
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
        """
        Returns
        -------
        dict
            the complete data of the result dictionary

        """
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


def coll_plane2plane(plane1, plane2, **kwargs):
    atol = cmp_atol
    verbose = False
    # handle all arguments
    for key, value in kwargs.items():
        if key == 'verbose':
            verbose = value
        elif key == 'atol':
            atol = value

    if verbose:
        debug('calculating collision between two planes')
        debug(' atol=%g' % atol)
    result = CollisionResult()

    cross = np.cross(plane1.norm_vector, plane2.norm_vector)

    if verbose:
        debug(' cross_check_vector=%s' % cross)

    # if the cross vector has zero length, that there both
    # norm vectors are parallel
    if not np.isclose(nl.norm(cross), 0., atol=atol):
        result['collision'] = True
        result['type'] = 'crossing'
        p, v = intersection_of_planes(plane1.norm_vector, plane1.distance,
                                      plane2.norm_vector, plane2.distance)
        result['intersection'] = 'line'
        result['intersection_params'] = (p, v)
    else:
        if np.isclose(plane1.distance, plane2.distance, atol=atol):
            result['collision'] = True
            result['type'] = 'identical'
            result['intersection'] = 'plane'
            result['intersection_params'] = (plane1.distance, plane2.distance)

    if verbose:
        debug('collision:', result['collision'])
        debug('Done.')

    return result


def coll_sphere2plane(sphere, plane, **kwargs):
    atol = cmp_atol
    verbose = False
    # handle all arguments
    for key, value in kwargs.items():
        if key == 'verbose':
            verbose = value
        elif key == 'atol':
            atol = value

    if verbose:
        debug('calculating collision between a sphere and a plane')
        debug(' atol=%g' % atol)
    result = CollisionResult()

    v = sphere.position

    # the vector s is the vector which is perpendicular to
    # the plane pointing direct to the center of the sphere
    # s = projection_vector(v, plane.norm_vector)
    # distance = nl.norm(s) + plane.distance
    distance = np.abs(distance_to_plane(v, plane.norm_vector, plane.distance))

    result['distance'] = distance
    if verbose:
        debug(' absolute distance is: %g' % distance)

    distance -= sphere.radius

    result['outerdistance'] = distance
    if verbose:
        debug(' outer distance is: %g' % distance)

    # every outside atol is clear
    result['collision'] = np.isclose(distance, 0., atol=atol)

    if verbose:
        debug('collision:', result['collision'])
        debug('Done.')

    return result


"""
coll_box2plane

the algorithm based on the brute force test of all eight corners and
their distances to the plane. If all distances have the same sign,
they are always on the same side of the plane and therefore there is
no collision. Otherwise with some points in front and behind the plane
we have a collision. The collision figure, the polygon is a different
story.
"""


def coll_box2plane(box, plane, **kwargs):
    atol = cmp_atol
    verbose = False
    # handle all arguments
    for key, value in kwargs.items():
        if key == 'verbose':
            verbose = value
        elif key == 'atol':
            atol = value

    if verbose:
        debug('calculating collision between a box and a plane')
        debug(' atol=%g' % atol)
    result = CollisionResult()

    distances = np.zeros(len(box._corners))
    c = box.corners
    for i in range(len(distances)):
        distances[i] = distance_to_plane(c[i],
                                         plane.norm_vector,
                                         plane.distance)

    if verbose:
        debug(' distances=%s' % distances)

    nnp = nnm = nnn = 0
    for i in distances:
        if np.isclose(i, 0., atol=atol):
            nnn += 1
        elif i > atol:
            nnp += 1
        else:
            nnm += 1

    if verbose:
        debug(' (nnp, nnm, nnn)=(%i, %i, %i)' % (nnp, nnm, nnn))

    if nnn > 0:
        # one or more points directly on the plane
        result['collision'] = True
    else:
        if (nnp != 8) or (nnm != 8):
            result['collision'] = True

    if result['collision']:
        # try to get the intersection figure
        edges = box.edges
        points = []
        for e in edges:
            # test a single edge ...
            p = intersection_line_plane(e, plane.norm_vector, plane.distance)
            if p is not None:
                vol = box.get_volume(center=p)
                if verbose:
                    debug(' c=%s vol=%g vol_ref=%g' % (i, vol, box._volume))
                if np.isclose(vol, box._volume, rtol=atol, atol=atol):
                    points.append(p)

        points = np.array(points)

        if verbose:
            debug(' points (unsorted) in the plane = %s' % points)
        if len(points) > 3:
            points = polygon_sort(points, plane.norm_vector, atol=atol)

        if verbose:
            debug(' points (sorted) in the plane = %s' % points)

    if verbose:
        debug('collision:', result['collision'])
        debug('Done.')

    return result
