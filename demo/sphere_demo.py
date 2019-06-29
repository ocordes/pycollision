"""
sphere_demo.py

demonstration of the Sphere handling and collision detection

"""

from pycollision.objects import Sphere

import numpy as np

if __name__ == '__main__':


    s1 = Sphere([0,0,0], 1.)

    s1.translation = [1,2,3]
    s1.translation = [-1,2,2]

    print(s1.position)
