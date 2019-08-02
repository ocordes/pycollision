"""
plane_demo.py

demonstration of the Plane handling and collision detection

"""

from pycollision.objects3d import Sphere, Plane, Box
from pycollision.planes import create_xy_plane, create_xz_plane, \
                               create_yz_plane

from pycollision.rotation import *

import numpy as np

if __name__ == '__main__':

    p1 = create_xy_plane(1)
    p1.rotation = create_rotation_Y(90)
    print(p1.norm_vector)

    p1.translation = [1, 10, -10]
    print(p1.distance)


    # plane / sphere
    s1 = Sphere([0, 0, 0], 1.)

    p1 = create_xy_plane(1)
    p1.translation = [1, 0, 0]

    result = s1.has_collisions(p1, verbose=True)

    print(result)
    # get the result
    print(result())


    # plane / plane

    p1 = create_xy_plane(0)
    p2 = create_xy_plane(1e-5)

    result = p1.has_collisions(p2, verbose=True, atol=1e-4)

    print(result)
    # get the result
    print(result())


    # plane / box
    b1 = Box([0, 0, 0], [1, 1, 1])
    p1 = create_yz_plane(0.5)

    reult = b1.has_collisions(p1, verbose=True)
