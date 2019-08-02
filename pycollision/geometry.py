#
# pycollision/geometry.py
#
# written by: Oliver Cordes 2019-07-24
# changed by: Oliver Cordes 2019-08-02
#

"""

geometry library defines some linear algebra routines
which were used by the objects and collision algorithms

"""

import numpy as np
import numpy.linalg as nl

import numpy.random as nr

from pycollision.debug import debug

# constants
cmp_atol = 1e-8

zero_x = np.array([1., 0., 0.])
zero_y = np.array([0., 1., 0.])
zero_z = np.array([0., 0., 1.])


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


def point_of_plane(plane_norm, plane_dist, atol=cmp_atol):
    """
    point_of_plane

    calculates a random point on the plane
    """
    # debug('plane_norm=%s' % plane_norm)
    # debug('plane_dist=%s' % plane_dist)
    if not np.isclose(plane_norm[2], 0, atol=atol):
        x1 = 0.
        x2 = 0.
        x3 = plane_dist / plane_norm[2]
    elif not np.isclose(plane_norm[1], 0, atol=atol):
        x1 = 0.
        x3 = 0.
        x2 = plane_dist / plane_norm[1]
    elif not np.isclose(plane_norm[0], 0, atol=atol):
        x2 = 0.
        x3 = 0.
        x1 = plane_dist / plane_norm[0]
    else:
        raise ValueError('zero norm vector given for plane!')

    return np.array([x1, x2, x3], dtype=np.float64)


def point_of_plane_random(norm, dist, rvalue, atol=cmp_atol):
    """
    point_of_plane

    calculates a random point on the plane
    """
    # debug('plane_norm=%s' % plane_norm)
    # debug('plane_dist=%s' % plane_dist)
    if not np.isclose(norm[2], 0, atol=atol):
        x1 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x2 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x3 = (dist - norm[0] * x1 - norm[1] * x2) / norm[2]
    elif not np.isclose(norm[1], 0, atol=atol):
        x1 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x3 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x2 = (dist - norm[0] * x1 - norm[2] * x3) / norm[1]
    elif not np.isclose(norm[0], 0, atol=atol):
        x2 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x3 = nr.randint(1, rvalue) * nr.choice((-1, 1))
        x1 = (dist - norm[1] * x2 - norm[2] * x3) / norm[0]
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


def orthogonal_vector(plane_norm, atol=cmp_atol):
    """
    orthogonal_vector

    calculates one pseudo-random vector which is orthogonal to
    the plane_norm vector
    """

    if not np.isclose(plane_norm[2], 0., atol=atol):
        x1 = 1.
        x2 = 0.
        x3 = -x1*plane_norm[0] / plane_norm[2]
    elif not np.isclose(plane_norm[1], 0., atol=atol):
        x1 = 1.
        x3 = 0.
        x2 = -x1*plane_norm[0] / plane_norm[1]
    elif not np.isclose(plane_norm[0], 0., atol=atol):
        x2 = 1.
        x3 = 0.
        x1 = -x2*plane_norm[1] / plane_norm[0]
    else:
        raise ValueError('zero norm vector given for plane!')

    # put all elements together
    v = np.array([x1, x2, x3])

    return v / nl.norm(v)


def plane_vectors(plane_norm, atol=cmp_atol):
    """
    plane vectors

    calculate two spanning vectors for the plane given by the
    norm_vector
    """
    v = orthogonal_vector(plane_norm, atol=atol)

    w = np.cross(plane_norm, v)

    w = w / nl.norm(w)

    return v, w


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


def get_center_of_points_3D(points):
    """
    get_center_of_points_3D

    calculates a center point for the given point array, using
    a simple approach of calculating the middle of the min and max
    values for all 3 dimensions
    """
    first = True
    for p in points:
        if first:
            min_x = max_x = p[0]
            min_y = max_y = p[1]
            min_z = max_z = p[2]
            first = False
        else:
            if p[0] > max_x:
                max_x = p[0]
            if p[0] < min_x:
                min_x = p[0]
            if p[1] > max_y:
                max_y = p[1]
            if p[1] < min_y:
                min_y = p[1]
            if p[2] > max_z:
                max_z = p[2]
            if p[2] < min_z:
                min_z = p[2]

    return np.array([(max_x+min_x)/2., (max_y+min_y)/2., (max_z+min_z)/2.])


def angle_between_vectors(x, v, w):
    """
    angle_between_vectors

    calculates the angle bewteen 2 given vectors, taking care of
    rounding errors for the norm!
    Basically it the the angle between x and v, but these gives
    sometimes the same angle if x  is mirrored by v, so the
    orthogonal vector w is then giving with is sign the left or
    right side of v! The angle may be not mathematically correct,
    but it is only used for sorting!
    """
    a1 = np.clip(np.dot(x, v) / (nl.norm(x) * nl.norm(v)), -1., 1.)
    a2 = np.clip(np.dot(x, w) / (nl.norm(x) * nl.norm(w)), -1., 1.)

    return np.sign(a2)*np.arccos(a1)


def polygon_sort(points, norm_vector, atol=cmp_atol):
    """
    polygon_sort

    sort the array of points to form a polygon which is on the plane
    given by the norm_vector

    First Idea is to use scipy.spatial.ConvexHull , but in the end,
    there is a much simply algorithm which do not base on any
    external extra package
    """

    center = get_center_of_points_3D(points)

    # get the reference vectors inside the plane
    v, w = plane_vectors(norm_vector, atol=atol)

    # to store the angles
    angles = np.zeros(len(points))

    i = 0
    for p in points:
        angles[i] = angle_between_vectors((center-p), v, w)
        i += 1

    # sort the angles -> argsort to apply on points
    a = np.argsort(angles)

    return points[a]


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


def intersection_line_plane(edge, norm_vector, distance, atol=cmp_atol):
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
