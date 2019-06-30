"""

pycollision/debug.py

written by: Oliver Cordes 2019-06-30
changed by: Oliver Cordes 2019-06-30


"""

"""
debug

writes a debug message
"""


def debug(*vars):
    s = ' '.join([str(i) for i in vars])
    print('DEBUG: '+s, flush=True)
