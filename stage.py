from xy import XY
from player import Player
from tiles import Block, Floor, Border, Tile

def parse(filename):
    with open(filename) as f:
        return [[int(x) for x in line.split(",")] for line in f]

def add_border(mat):
    res = [[-1] * (2 + len(mat[0]))]
    for x in mat:
        res.append([-1] + x + [-1])
    res.append([-1] * (2 + len(mat[0])))
    return res

class Board:

    dct = {-1: "borders",
           0: "floors",
           1: "blocks"}

    def __init__(self, file_name):
        self.mat = add_border(parse(file_name))
        self.width = Tile.nb_lines = len(self.mat)
        self.height = len(self.mat[0])
        self.blocks = []
        self.floors = []
        self.borders = []
        for i, line in enumerate(self.mat):
            for j, element in enumerate(line):
                getattr(self, self.dct[element]).append((i,j))

    def get_id(self, pos):
        pos = XY(*pos)
        return pos.x * self.width + pos.y


class Stage:
    def __init__(self, filename):
       self.board = Board(filename)
       #self.player1 = Player(1, self.board.p1)
       #self.player2 = Player(2, self.board.p2)
       for pos in self.board.blocks:
           Block(pos, self.board.get_id(pos))
       for pos in self.board.floors:
           Floor(pos, self.board.get_id(pos))
       for pos in self.board.borders:
           Border(pos, self.board.get_id(pos))


