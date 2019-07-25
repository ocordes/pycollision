"""

pycollision/geometry.py

written by: Oliver Cordes 2019-07-24
changed by: Oliver Cordes 2019-07-24

"""

import numpy as np
import numpy.linalg as nl


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
