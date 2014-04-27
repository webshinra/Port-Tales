from XY import XY
from MapView import MapView
from ActionHandler import ActionHandler
from functools import partial


def parse(filename):
    with open(filename) as f:
        return [[int(x) for x in line.split(",")] for line in f]

def add_border(mat):
    res = [[-1] * (2 + len(mat[0]))]
    for x in mat:
        res.append([-1] + x + [-1])
    res.append([-1] * (2 + len(mat[0])))
    return res

class Map:

    def __init__(self, file_name):

        # Action handling
        self.action_handler = ActionHandler()

        # Create mapview
        self.view = MapView(self.action_handler)

        # Imports
        from Tile import Block, Floor, Border, Tile, Goal
        from Player import Player
        self.dct = {-1: Border,
                     1:  Floor,
               2: Goal,
               3: "goal2",
               4: partial(self.build_player, 1),
               5: partial(self.build_player, 2),
               6: Block,
               7: "hole",
               8: "mirrorDU",
               9: "mirrorUD",
               10: "memory",
               11: "p1Wall",
               12: "p2Wall" }

        # Parse file
        self.mat = add_border(parse(file_name))
        self.width = Tile.nb_lines = len(self.mat)
        self.height = len(self.mat[0])
        self.players = {}
        for i, line in enumerate(self.mat):
            for j, element in enumerate(line):
                pos = i,j
                self.dct[element](pos, self.get_id(pos))

        for id_player, player in self.players.items():
           self.action_handler.add_player(id_player, player)

    def build_player(self, player_id, pos, pid):
        from Player import Player
        from Tile import Block, Floor, Border, Tile
        Floor(pos, pid)
        self.players[player_id] = Player(player_id, pos, self)


    def get_id(self, pos):
        pos = XY(*pos)
        return pos.x * self.width + pos.y




