from xy import XY
import pygame as pyg
from pygame import Surface, Rect
from pygame.sprite import Sprite

from constants import *

class Tile(Sprite):

    width = 30
    containers = ()

    @staticmethod
    def resize_ressource(cls, name):
        ressource = pyg.image.load(ressource_name).convert()
        factor = float(cls.width)/ressource.width
        size = XY(ressource.size)*(factor,factor)
        ressource = pyg.transform.smoothscale(ressource, size)


    def __init__(self, board_pos):
        super(Tile, self).__init__(self.containers)
        self.pos = self.convert(board_pos)
        self.rect = Rect(self.pos, self.size)
        self.image = Surface(self.rect.size)

    def convert(self, pos):
        factor_y = 3*self.width/(2**1.5)
        pos *= width*0.5, factor_y
        return XY(*map(int,pos))

class Block(Tile):

    ressource_name = "block.png"
    ressource = Tile.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        self.layer = board_id
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