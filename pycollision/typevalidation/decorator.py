"""

typevalidation/decorator.py

written by: Oliver Cordes 2019-07-01
changed by: Oliver Cordes 2019-07-01

"""

from functools import wraps



class typevalidate(object):
    def __init__ (self, *args, **kwargs):
        # store arguments passed to the decorator
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        msg = func.__qualname__

        @wraps(func)
        def wrap(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)

        return wrap
