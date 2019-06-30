"""

pycollision/rotation.py


written by: Oliver Cordes 2019-06-30
changed by: Oliver Cordes 2019-06-30


"""

import numpy as np

"""
create _rotation_matrix

creates a matrix for a rotation around a given vector
and angle

:params vector:  the vector of the rotation axis
:params angle:   rotate around this angle
"""
def create_rotation_matrix(vector, angle):
    angle = angle * np.pi / 180.
    matrix = np.zeros(9).reshape((3,3))

    u_x = vector[0]
    u_y = vector[1]
    u_z = vector[2]
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    matrix[0,0] = cos_a + u_x**2 * (1.-cos_a)
    matrix[0,1] = u_x * u_y * (1.-cos_a) - u_z * sin_a
    matrix[0,2] = u_x * u_z * (1.-cos_a) + u_y * sin_a
    matrix[1,0] = u_y * u_x * (1.-cos_a) + u_z * sin_a
    matrix[1,1] = cos_a + u_y**2 * (1.-cos_a)
    matrix[1,2] = u_y * u_z * (1.-cos_a) - u_x * sin_a
    matrix[2,0] = u_z * u_x * (1.-cos_a) - u_y * sin_a
    matrix[2,1] = u_z * u_y * (1.-cos_a) + u_x * sin_a
    matrix[2,2] = cos_a + u_z**2 * (1.-cos_a)

    return matrix


"""
create_rotation_X

rotates around the x axis with the given angle
"""
def create_rotation_X(angle):
    return create_rotation_matrix([1., 0., 0.], angle)


"""
create_rotation_Y

rotates around the y axis with the given angle
"""
def create_rotation_Y(angle):
    return create_rotation_matrix([0., 1., 0.], angle)


"""
create_rotation_Z

rotates around the z axis with the given angle
"""
def create_rotation_Z(angle):
    return create_rotation_matrix([0., 0., 1.], angle)
