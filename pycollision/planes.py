#
# pycollision/planes.py
#
# written by: Oliver Cordes 2019-07-24
# changed by: Oliver Cordes 2019-07-24
#

"""

This module defines some initialization routines for
basic 3d-planes.

"""


import numpy as np


from pycollision.objects import Plane

"""
default normal vectors
"""

norm_xy = np.array([0., 0., 1.], dtype=np.float64)
norm_xz = np.array([0., 1., 0.], dtype=np.float64)
norm_yz = np.array([1., 0., 0.], dtype=np.float64)


def create_xy_plane(distance=0.):
    return Plane(norm_xy, d=distance)


def create_xz_plane(distance=0.):
    return Plane(norm_xz, d=distance)


def create_yz_plane(distance=0.):
    return Plane(norm_yz, d=distance)
