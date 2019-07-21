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


    b1 = Box([0, 0, 0], [1, 1, 1], verbose=True)

    b1.translation = [-1, 0, 0]
    #b1.translation = [-1, 2, 2]

    #b1.rotation = create_rotation_Y(90)
    #b1.rotation = create_rotation_Z(-25)
    #b1.rotation = create_rotation_X(90)

    b1.post_translation = [1, 0, 0]

    #b1.rotation = create_rotation_Z(-20)

    print(b1.position)



    b2 = Box([0,0,0], [1,1,1])
    b2.translation = [1.5,0,0]


    for i in range(90):
        print('%2i : %s' % (i, b1.has_collisions(b2, verbose=False, atol=1e-10)))
        b1.rotation = create_rotation_Z(-1)

    result = b1.has_collisions(b2, verbose=True, atol=1e-10)

    #print(result)
    # get the result
    print(result())
