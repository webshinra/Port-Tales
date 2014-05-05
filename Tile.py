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

from TileView import BlockView, FloorView, BorderView, GoalView, HoleView
from XY import XY
import operator

class Tile:
    def __init__(self, pos):
        self.pos = XY(*pos)
        self.view = None

class Block(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, pos)
        self.view = BlockView(pos, pid)

class Floor(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, pos)
        self.view = FloorView(pos, pid)
        self.active_dict = {1:False, 2:False}

    def set_active(self, active, player_id):
        self.active_dict[player_id] = active
        mul = map(operator.mul, self.active_dict, self.active_dict.values())
        self.view.set_color(sum(mul))


class Border(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, pos)
        self.view = BorderView(pos, pid)
        self.active = False

class Goal(Tile):
    def __init__(self, goal_id, pos, pid):
        Tile.__init__(self, pos)
        self.view = GoalView(goal_id, pos, pid)

    def set_active(self, active):
        self.active = active
        self.view.set_active(active)

class Hole(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, pos)
        self.view = HoleView(pos, pid)
