"""
box_demo.py

demonstration of the box handling and collision detection

written by: Oliver Cordes 2019-07-19
changed by: Oliver Cordes 2019-07-21

"""

from pycollision.objects3d import Box

from pycollision.rotation import *

import numpy as np

if __name__ == '__main__':

    # this setup is dynamically
    # two boxes with a distance of x=0.5 and box1
    # rotates at x=1 side around the z axis against
    # box2 like a falling domino ...
    b1 = Box([0, 0, 0], [1, 1, 1], verbose=True)

    # first translation as a preperation of the rotation
    b1.translation = [-1, 0, 0]

    # compensation of the 1st translation
    b1.post_translation = [1, 0, 0]



    b2 = Box([0,0,0], [1,1,1])
    b2.translation = [1.5,0,0]


    for i in range(90):
        print('%2i : %s' % (i, b1.has_collisions(b2, verbose=False, atol=1e-10)))
        b1.rotation = create_rotation_Z(-1)

    #print(b1.has_collisions(b2, verbose=False, atol=1e-10))

    # obviously after a rotation >30 degrees both boxes are colliding!
