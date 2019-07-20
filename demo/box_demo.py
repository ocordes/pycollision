"""
box_demo.py

demonstration of the box handling and collision detection

written by: Oliver Cordes 2019-07-19
changed by: Oliver Cordes 2019-07-19

"""

from pycollision.objects import Box

from pycollision.rotation import *

import numpy as np

if __name__ == '__main__':


    b1 = Box([0, 0, 0], [1, 1, 1])

    b1.translation = [-1, 0, 0]
    #b1.translation = [-1, 2, 2]

    #b1.rotation = create_rotation_Y(90)
    b1.rotation = create_rotation_Z(-45)
    #b1.rotation = create_rotation_X(90)

    print(b1.position)


    b2 = Box([0,0,0], [1,1,1])
    b2.translation = [1,0,0]


    b1.get_volume()

    #result = s1.has_collisions(s2, verbose=True)

    #print(result)
    # get the result
    #print(result())
