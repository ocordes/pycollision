"""

pycollision/geometry.py

written by: Oliver Cordes 2019-07-24
changed by: Oliver Cordes 2019-07-27

"""

import numpy as np
import numpy.linalg as nl

import numpy.random as nr

from pycollision.debug import debug


def projection_vector(v, ref):
    """
    projection_vector

    calculate the vector projection of v on ref

    :param v:   3d vector v
    :param ref: 3d vector on which v should be projected

    """
    # normalize the ref vector
    nref = nl.norm(ref)

    # calculate the projected vector
    return ref * np.dot(v, ref) / (nref**2)


def point_of_plane(plane_norm, plane_dist, atol=1e-8):
    """
    point_of_plane

    calculates a random point on the plane
    """
    debug('plane_norm=%s' % plane_norm)
    debug('plane_dist=%s' % plane_dist)
    if not np.isclose(plane_norm[2], 0, atol=atol):
        x1 = nr.randint(0, 10) + 1
        x2 = nr.randint(0, 10) + 1
        x3 = (plane_dist - plane_norm[0] * x1 - plane_norm[1] * x2) / plane_norm[2]
    elif not np.isclose(plane_norm[1], 0, atol=atol):
        x1 = nr.randint(0, 10) + 1
        x3 = nr.randint(0, 10) + 1
        x2 = (plane_dist - plane_norm[0] * x1 - plane_norm[2] * x3) / plane_norm[1]
    elif not np.isclose(plane_norm[0], 0, atol=atol):
        x2 = nr.randint(0, 10) + 1
        x3 = nr.randint(0, 10) + 1
        x1 = (plane_dist - plane_norm[1] * x2 - plane_norm[2] * x3) / plane_norm[0]
    else:
        raise ValueError('zero norm vector given for plane!')

    return np.array([x1, x2, x3], dtype=np.float64)


def distance_to_plane(v, plane_norm, plane_dist):
    """
    distance_to_plane

    calculate the distance from a point v to the plane given
    by the normal vector and the distance
    """
    s = projection_vector(v, plane_norm)

    return nl.norm(s) - plane_dist


def pyramid_volume(plane, height):
    """
    pyramid_volume

    calculate the volume of a Pyramid

    :param plane:   array of the 4 corners given by a 3d vector
    :param height:  3d vector to the height point

    """

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
    # phv = nv * np.dot(hv, nv) / (nnv**2)
    # length of the vector is the scalar height of the pyramid
    # nh = nl.norm(phv)
    nh = np.abs(np.dot(hv, nv) / nnv)

    return nnv * nh / 3.


"""
--------------------------------------------------------------------------------
Intersections
"""


"""
intersection_of_planes

Line of intersection between two planes

taken from: https://en.wikipedia.org/wiki/Plane_(geometry)
      anchor: #Line_of_intersection_between_two_planes

"""


def intersection_of_planes(n1, d1, n2, d2):
    # normalize the norm vectors
    n1 = n1 / nl.norm(n1)
    n2 = n2 / nl.norm(n2)

    n1n2 = np.dot(n1, n2)
    n1n2sqm1 = 1 - n1n2**2
    n1xn2 = np.cross(n1, n2)

    c1 = (d1 - d2 * n1n2)/n1n2sqm1
    c2 = (d2 - d1 * n1n2)/n1n2sqm1

    p = (c1 * n1) + (c2 * n2)

    return p, n1xn2


def intersection_line_plane(edge, norm_vector, distance, atol=1e-8):
    """
    intersection_line_plane

    calculates the intersection point between a ray and a plane
    """
    edge_direction = edge[0] - edge[1]

    plane_point = point_of_plane(norm_vector, distance)

    debug(' plane_point=%s' % plane_point)

    ndotu = norm_vector.dot(edge_direction)

    if abs(ndotu) < atol:
        debug(' no intersection or line is within plane')
        return None

    w = edge[0] - plane_point
    si = -norm_vector.dot(w) / ndotu
    Psi = w + si * edge_direction + plane_point

    print(Psi)
    debug(' intersection point=%s' % Psi)

    return Psi
