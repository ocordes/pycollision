"""

typevalidation/decorator.py

written by: Oliver Cordes 2019-07-01
changed by: Oliver Cordes 2019-07-01

"""

from functools import wraps

from pycollision.typevalidation.types import *


class typevalidate(object):
    def __init__ (self, *args, **kwargs):
        # store arguments passed to the decorator
        self.args = args
        self.kwargs = kwargs

        for key, val in kwargs.items():
            if key == 'isclass':
                self._isclass = val


    def __call__(self, func):
        msg = func.__qualname__
        a   = dir(func)

        @wraps(func)
        def wrap(*args, **kwargs):
            print(msg)
            print(id(self))
            print(func.__annotations__)
            args, kwargs = self.convert(args, kwargs, func.__annotations__)
            return func(*args, **kwargs)

        return wrap


    def convert(self, args, kwargs, newtypes):
        newtypesargs = [ val for key,val in newtypes.items()]
        print(newtypesargs)
        # converting args, iterating over indices...
        if self._isclass:
            indx = 1
        else:
            indx = 0

        tindx = 0
        while indx < len(args):
            print(type(args[indx]))
            newval = self.converttype(args[indx], newtypesargs[tindx])
            indx += 1
            tindx += 1
        return args, kwargs


    def converttype(self, val, newtype):
        if newtype in basic_types:
            return newtype(val)
        else:
            return newtype(val)
