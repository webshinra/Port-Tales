import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from constants import *
from xy import XY
from tiles import Tile
import os
from itertools import takewhile, count, cycle

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

def animation(folder):
        names = (os.path.join(folder, "{:04}.png".format(i)) for i in count(1))
        names = takewhile(os.path.isfile , names)
        return [Tile.resize_ressource(name) for name in names]


class Player(Tile):

    containers = ()
    ressource_name = "red_player_se"
    ressources = animation(ressource_name)

    def __init__(self, player_id, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(Player, self).__init__(self.board_pos, board_id)
        self.dirty = 2
        self.animation = cycle(self.ressources)
        self.image = next(self.animation)
        self.id = player_id
        self.routine = player_routine(self)
        next(self.routine)
        self.move = False
        self.dir = (1,0)

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
        self.image = next(self.animation)
        self.board_pos = self.routine.send((self.move, self.dir))
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))


