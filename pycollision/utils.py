"""

pycollision/utils.py

written by: Oliver Cordes 2019-06-29
changed by: Oliver Cordes 2019-06-29

"""

import numpy as np


def input2float(x):
    try:
        return float(x)
    except:
        raise TypeError('x is not a suitable float value')


def input2position(x):
    if isinstance(x, (list, tuple)):
        if len(x) == 3:
            return np.array(x, dtype=np.float64)
        else:
            raise TypeError('List/tuple needs 3 entries for a suitable position')
    elif isinstance(x, np.ndarray ):
        if x.shape == (3,):
            return x.copy()
        else:
            raise TypeError('numpy array needs 3 entries for a suitable position')
    elif isinstance(x, str):
        s = x.split(',')
        if len(s) == 3:
            return np.array([float(i) for i in s], dtype=np.float64)
        else:
            raise TypeError('string array needs 3 entries for a suitable position')
    else:
        raise TypeError('x is not of a suitable type for a position')
