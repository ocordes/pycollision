"""
sphere_demo.py

demonstration of the Sphere handling and collision detection

"""

from pycollision.objects import Sphere

from pycollision.rotation import *

import numpy as np

if __name__ == '__main__':


    s1 = Sphere([0,0,0], 1.)

    s1.translation = [1,2,3]
    s1.translation = [-1,2,2]

    s1.rotation = create_rotation_Y(90)
    s1.rotation = create_rotation_Z(90)
    s1.rotation = create_rotation_X(90)

    print(s1.position)


    s2 = Sphere([5,0,0], 1.)
    print(s2.position)

    print(s2)
