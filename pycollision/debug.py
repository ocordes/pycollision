#
# pycollision/debug.py
#
# written by: Oliver Cordes 2019-06-30
# changed by: Oliver Cordes 2019-08-02
#

"""

debug

writes a debug message
"""


def debug(*vars):
    """
    prints a debug message

    Arguments
    ---------
    vars:
        variable number of arguments similar to the print function
    """
    s = ' '.join([str(i) for i in vars])
    print('DEBUG: '+s, flush=True)
