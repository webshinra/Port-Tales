from xy import XY
from player import Player
from tiles import Block, Floor

def parse(filename):
    with open(filename) as f:
        return [[int(x) for x in line.split(",")] for line in f]

class Board:

    dct = {0: "floors",
           1: "blocks"}

    def __init__(self, file_name):
        self.mat = parse(file_name)
        self.width = len(self.mat)
        self.height = len(self.mat[0])
        self.blocks = []
        self.floors = []
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
       for pos_block in self.board.blocks:
           Block(pos_block, self.board.get_id(pos_block))
       for pos_block in self.board.floors:
           Floor(pos_block, self.board.get_id(pos_block))


