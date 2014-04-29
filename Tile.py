from TileView import BlockView, FloorView, BorderView, GoalView, HoleView

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.view = None

class Block(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        self.view = BlockView(pos, pid)

class Floor(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        self.view = FloorView(pos, pid)

class Border(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        self.view = BorderView(pos, pid)

class Goal(Tile):
    def __init__(self, goal_id, pos, pid):
        Tile.__init__(self, *pos)
        self.view = GoalView(goal_id, pos, pid)

class Hole(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        self.view = HoleView(pos, pid)
