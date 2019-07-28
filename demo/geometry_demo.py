"""

demo/geometry_demo.py

written by: Oliver Cordes 2019-07-28
changed by: Oliver Cordes 2019-07-28

"""


import numpy as np

from pycollision.geometry import *


if __name__ == '__main__':

    # recalculate the vectors which are spanning a plane
    # from a norm vector

    norm_vector = np.array([1, 1, 1])   # yz plane

    v = orthogonal_vector(norm_vector)

    print(v)

    v, w = plane_vectors(norm_vector)

    print(v, w)

    print('Random points of the plane:')
    for i in range(10):
        x = point_of_plane_random(norm_vector, 0., 20)
        print(' %s' % x)


    print(point_of_plane(norm_vector, 1.))
