from XY import XY
from MapView import MapView
from ActionHandler import ActionHandler
from functools import partial


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

        # Imports
        from Tile import Block, Floor, Border, Tile, Goal
        from Player import Player
        from TileView import TileView
        self.dct = {-1: Border,
                     1:  Floor,
                     2: partial(self.build_goal, 1),
                     3: partial(self.build_goal, 2),
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
        self.width = TileView.nb_lines = len(self.mat)
        self.height = len(self.mat[0])
        self.players = {}
        self.goal = {}
        for i, line in enumerate(self.mat):
            for j, element in enumerate(line):
                pos = i,j
                self.dct[element](pos, self.get_id(pos))
                if (element == 2) :
                    self.goal1 = (i,j)
                if (element == 3) :
                    self.goal2 = (i,j)
                if (element == 4) :
                    self.start1 = (i,j)
                if (element == 5) :
                    self.start2 = (i,j)

        for id_player, player in self.players.items():
           self.action_handler.add_player(id_player, player)
           self.projection(id_player)



    def build_player(self, player_id, pos, pid):
        from Player import Player
        from Tile import Floor
        Floor(pos, pid)
        self.players[player_id] = Player(player_id, pos, self)


    def build_goal(self, goal_id, pos, pid):
        from Tile import Goal
        self.goal[goal_id] = Goal(goal_id, pos, pid)


    def get_id(self, pos):
        pos = XY(*pos)
        return pos.x * self.width + pos.y

    def projection(self, player_id):
        res = []
        player = self.players[player_id]
        dir = player.dir
        x = player.x
        y = player.y

        continu = True
        dx = dir[0]
        dy = dir[1]

        otherId = 2 if player_id == 1 else 1
        otherX = self.players[otherId].x
        otherY = self.players[otherId].y

        res.append((x,y))

        while(continu):
            nextX = x + dx
            nextY = y + dy
            nextTile = self.mat[nextX][nextY]
            continu = nextTile != 6 and nextTile != -1
            continu = continu and not (nextX == otherX and nextY == otherY)
            if (continu):
                x += dx
                y += dy
                res.append((x,y))

        return res

    def success (self):

        player1 = self.players[1]
        player2 = self.players[2]

        success1 = player1.x == self.goal1[0] and player1.y == self.goal1[1]
        success2 = player2.x == self.goal2[0] and player2.y == self.goal2[1]

        return success1 and success2

    def reset (self) :
        player1 = self.players[1]
        player2 = self.players[2]

        player1.x = self.start1[0]
        player1.y = self.start1[1]
        player2.x = self.start2[0]
        player2.y = self.start2[1]







