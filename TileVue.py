from xy import XY
import pygame as pyg
from pygame import Surface, Rect
from pygame.sprite import DirtySprite, Sprite

from constants import *

class TileVue(DirtySprite):

    width = 70
    layer_container = None
    nb_lines = 10

    @classmethod
    def resize_ressource(cls, name):
        ressource = pyg.image.load(name).convert_alpha()
        factor = float(cls.width)/ressource.get_width()
        size = XY(*ressource.get_size())*(factor,factor)
        size = map(int, size)
        return pyg.transform.smoothscale(ressource, size)

    def __init__(self, board_pos, layer=0):
        # Init
        super(Tile, self).__init__()
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

class BlockVue(TileVue):

    ressource_name = "block.png"
    ressource = TileVue.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(Block, self).__init__(self.board_pos, board_id)
        self.image = self.ressource

class FloorVue(TileVue):

    ressource_name = "floor.png"
    ressource = TileVue.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(Floor, self).__init__(self.board_pos, board_id)
        self.image = self.ressource

class BorderVue(TileVue):

    ressource_name = "border.png"
    ressource = TileVue.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(Border, self).__init__(self.board_pos, board_id)
        self.image = self.ressource
