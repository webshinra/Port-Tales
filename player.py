import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from constants import *
from xy import XY
from tiles import Tile

countdown = lambda x: xrange(x-1,-1,-1)

def counter(period):
    current = period
    while True:
        current -= 1
        current %= period
        yield not current


def player_routine(self):
    pos = self.board_pos
    while True:
        move, direction = yield pos


class Player(Tile):

    containers = ()
    ressource_name = "player.png"
    ressource = Tile.resize_ressource(ressource_name)

    def __init__(self, player_id, board_pos, layer=0):
        self.board_pos = XY(*board_pos)
        super(Block, self).__init__(self.board_pos, board_id)
        self.image = self.ressource
        self.id = player_id
        self.routine = player_routine(self)
        next(self.routine)

    def convert(self, pos):
        pos = XY(pos.y-pos.x, pos.x+pos.y)
        factor_y = (self.width-4)/(2*3**0.5)
        pos *= (self.width-4)*0.5, factor_y
        pos += self.width*self.nb_lines/2, 0
        return XY(*map(int,pos))

    def set_input(self, keys):
        self.move = False
        self.dir = (1,0)


    def update(self):
        self.image = pyg.transform.rotate(self.image_base, degree(self.angle))
        args = self.angle, self.tprop, self.tstop
        self.board_pos = self.routine.send(self.move, self.dir)
        self.graph_pos = self.board_pos * self.size
        self.rect = self.image.get_rect(topleft=self.graph_pos)


