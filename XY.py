""" Tuple for x,y coordinates and their transformations """

import operator
from collections import namedtuple

XY = namedtuple("XY",("x","y"))
XY.__iadd__ = XY.__add__ = lambda x, y: XY(*map(operator.add, x, y))
XY.__isub__ = XY.__sub__ = lambda x, y: XY(*map(operator.sub, x, y))
XY.__imul__ = XY.__mul__ = lambda x, y: XY(*map(operator.mul, x, y))
XY.__idiv__ = XY.__div__ = lambda x, y: XY(*map(operator.div, x, y))
XY.__abs__ = lambda x: abs(complex(*x))