from XY import XY
import pygame as pyg
from pygame import Surface, Rect
from pygame.sprite import DirtySprite, Sprite
from itertools import takewhile, count, cycle
import os
from Constants import *

class TileView(DirtySprite):

    width = 70#141
    layer_container = None
    nb_lines = 0

    @classmethod
    def resize_ressource(cls, name):
        ressource = pyg.image.load(name).convert_alpha()
        factor = float(cls.width)/ressource.get_width()
        size = XY(*ressource.get_size())*(factor,factor)
        size = map(int, size)
        return pyg.transform.smoothscale(ressource, size)

    def __init__(self, board_pos, layer=0):
        # Init
        super(TileView, self).__init__()
        self.layer_container.add(self, layer=layer)
        self.pos = self.convert(board_pos)
        self.rect = Rect(self.pos, (0, 0))
        self.image = Surface(self.rect.size)
        self.dirty = 1

    def convert(self, pos):
        pos = XY(pos.y-pos.x, pos.x+pos.y)
        factor_y = (self.width-4)/(2*3**0.5)
        pos *= (self.width-4)*0.5, factor_y
        pos += self.width*self.nb_lines/2, 0
        return XY(*map(int,pos))

class BlockView(TileView):

    ressource_name = "block.png"
    ressource = TileView.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(BlockView, self).__init__(self.board_pos, board_id)
        self.image = self.ressource

class FloorView(TileView):

    ressource_name = "floor.png"
    ressource = TileView.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(FloorView, self).__init__(self.board_pos, board_id)
        self.image = self.ressource

class BorderView(TileView):

    ressource_name = "border.png"
    ressource = TileView.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(BorderView, self).__init__(self.board_pos, board_id)
        self.image = self.ressource

class GoalView(TileView):

    def animation(folder):
        names = (os.path.join(folder, "{:04}.png".format(i)) for i in count(1))
        names = takewhile(os.path.isfile , names)
        return [TileView.resize_ressource(name) for name in names]

    ressource_name = "goal"
    ressources = animation(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(GoalView, self).__init__(self.board_pos, board_id)
        self.animation = cycle(self.ressources)
        self.image = next(self.animation)

    def update(self):
        self.image = next(self.animation)
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))
