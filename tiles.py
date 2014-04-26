from xy import XY
import pygame as pyg
from pygame import Surface, Rect
from pygame.sprite import Sprite

from constants import *

class Tile(Sprite):

    width = 70
    containers = ()

    @classmethod
    def resize_ressource(cls, name):
        ressource = pyg.image.load(name).convert_alpha()
        factor = float(cls.width)/ressource.get_width()
        size = XY(*ressource.get_size())*(factor,factor)
        size = map(int, size)
        return pyg.transform.smoothscale(ressource, size)


    def __init__(self, board_pos):
        super(Tile, self).__init__(self.containers)
        self.pos = self.convert(board_pos)
        self.rect = Rect(self.pos, (0, 0))
        self.image = Surface(self.rect.size)

    def convert(self, pos):
        pos = XY(pos.y-pos.x, pos.x+pos.y)
        factor_y = (self.width-2)/(2*3**0.5)
        pos *= (self.width-2)*0.5, factor_y
        pos += 500, 100
        return XY(*map(int,pos))

class Block(Tile):

    ressource_name = "block.png"
    ressource = Tile.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        self._layer = board_id
        super(Block, self).__init__(self.board_pos)
        self.image = self.ressource

class Floor(Tile):

    ressource_name = "floor.png"
    ressource = Tile.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        self.layer = board_id
        super(Floor, self).__init__(self.board_pos)
        self.image = self.ressource