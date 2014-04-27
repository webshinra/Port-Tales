from xy import XY
from MapVue import MapVue

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
    dct = {-1: "borders",
           1: "floors",
           2: "goal1",
           3: "goal2",
           4: "p1",
           5: "p2",
           6: "blocks",
           7: "hole",
           8: "mirrorDU",
           9: "mirrorUD",
           10: "memory",
           11: "p1Wall",
           12: "p2Wall" }

    def __init__(self, file_name):
        self.vue = MapVue()

        from Tiles import Block, Floor, Border, Tile

        self.mat = add_border(parse(file_name))
        self.width = Tile.nb_lines = len(self.mat)
        self.height = len(self.mat[0])
        self.blocks = []
        self.floors = []
        self.borders = []
        self.p1 = []
        self.p2 = []
        for i, line in enumerate(self.mat):
            for j, element in enumerate(line):
                getattr(self, self.dct[element]).append((i,j))
        self.p1 = self.p1[0]
        self.p2 = self.p2[0]

    def get_id(self, pos):
        pos = XY(*pos)
        return pos.x * self.width + pos.y


# class Stage:
#     def __init__(self, filename):
#         self.board = Board(filename)
#         for pos in self.board.blocks:
#             Block(pos, self.board.get_id(pos))
#         for pos in self.board.floors:
#             Floor(pos, self.board.get_id(pos))
#         for pos in self.board.borders:
#             Border(pos, self.board.get_id(pos))
#         args = 1, self.board.p1, self.board.get_id(self.board.p1)
#         self.player1 = Player(*args)
#         args = 2, self.board.p2, self.board.get_id(self.board.p2)
#         self.player2 = Player(*args)


