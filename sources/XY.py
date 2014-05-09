# this file is part of Port Tales
# Copyright (C) 2014
# Yann Asset <shinra@electric-dragons.org>, 
# Vincent Michel <vxgmichel@gmail.com>,
# Cyril Savary <cyrilsavary42@gmail.com>
  
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Tuple for x,y coordinates and their transformations """

import operator
from collections import namedtuple

XY = namedtuple("XY",("x","y"))
XY.__iadd__ = XY.__add__ = lambda x, y: XY(*map(operator.add, x, y))
XY.__isub__ = XY.__sub__ = lambda x, y: XY(*map(operator.sub, x, y))
XY.__imul__ = XY.__mul__ = lambda x, y: XY(*map(operator.mul, x, y))
XY.__idiv__ = XY.__div__ = lambda x, y: XY(*map(operator.div, x, y))
XY.__abs__ = lambda x: abs(complex(*x))
