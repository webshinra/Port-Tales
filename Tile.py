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
