from XY import XY
from MapView import MapView
from ActionHandler import ActionHandler
from functools import partial
from Tile import Block, Floor, Border, Tile, Goal, Hole
from Player import Player
from TileView import TileView


def parse(filename):
    with open(filename) as f:
        next(line for line in f if line.startswith("data="))
        parse_line = lambda line: [int(x) for x in line.strip().split(",") if x]
        return [parse_line(line) for line in f if "," in line]

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

        # Dictionary
        self.dct = {-1: Border,
                    1:  Floor,
                    2: partial(self.build_goal, 1),
                    3: partial(self.build_goal, 2),
                    4: partial(self.build_player, 1),
                    5: partial(self.build_player, 2),
                    6: Block,
                    7: Hole,
                    8: "mirrorDU",
                    9: "mirrorUD",
                    10: "memory",
                    11: "p1Wall",
                    12: "p2Wall" }


        # Parse file
        self.mat = add_border(parse(file_name))
        self.width = TileView.nb_lines = len(self.mat)
        self.height = len(self.mat[0])
        self.players = {}
        self.goals = {}
        self.tiles = {pos: self.dct[element](pos, self.get_id(pos))
                          for i, line in enumerate(self.mat)
                              for j, element in enumerate(line)
                                  for pos in [(i,j)]}

        for id_player, player in self.players.items():
            self.action_handler.add_player(id_player, player)


    def build_player(self, player_id, pos, pid):
        floor = Floor(pos, pid)
        self.players[player_id] = Player(player_id, pos, self, floor)
        return floor


    def build_goal(self, goal_id, pos, pid):
        self.goals[goal_id] = Goal(goal_id, pos, pid)
        return self.goals[goal_id]


    def get_id(self, pos):
        pos = XY(*pos)
        return pos.x * self.width + pos.y

    def projection(self, player_id):
        # Init variables
        result = []
        player = self.players[player_id]
        current_pos = player.pos
        other_pos = next(p.pos for i,p in self.players.items() if i!=player_id)

        # Loop over valid positions
        stop = False
        while not stop:
            # Append and update current position
            result.append(current_pos)
            current_pos += player.dir
            # Test new position
            next_tile = self.tiles[current_pos]
            stop = isinstance(next_tile, (Block, Border, Hole))
            stop = stop or current_pos == other_pos

        # Black hole case
        if isinstance(next_tile, Hole):
            result.append(current_pos)

        # Return result
        return result

    def get_success(self):
        # Inint result
        result = []
        # Get results
        for i in (1,2):
            goal = self.goals[i]
            player = self.players[i]
            success = (goal.pos == player.pos)
            goal.set_active(success)
            result.append(success)
        # Return the result
        return tuple(result)

    def win(self):
        self.view.win()

    def lose(self):
        self.view.lose()







