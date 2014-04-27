from TileView import BlockView, FloorView, BorderView, GoalView, HoleView

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.view = None

class Block(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        #super(Block, self).__init__(*pos)
        self.view = BlockView(pos, pid)

class Floor(Tile):
    def __init__(self, pos, pid):
        Tile.__init__(self, *pos)
        #super(Floor, self).__init__(*pos)
        self.view = FloorView(pos, pid)

class Border(Tile):
    def __init__(self, pos, pid):
        #super(Border, self).__init__(*pos)
        Tile.__init__(self, *pos)
        self.view = BorderView(pos, pid)

class Goal(Tile):
    def __init__(self, goal_id, pos, pid):
        #super(Border, self).__init__(*pos)
        Tile.__init__(self, *pos)
        self.view = GoalView(goal_id, pos, pid)

class Hole(Tile):
    def __init__(self, pos, pid):
        #super(Border, self).__init__(*pos)
        Tile.__init__(self, *pos)
        self.view = HoleView(pos, pid)
