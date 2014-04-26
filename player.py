import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from constants import *
from xy import XY

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


class Player(Sprite):

    containers = ()
    size = 20,20
    #ressource_name = "player.png"
    #ressource = pyg.image.load(ressource_name).convert()
    #ressource = pyg.transform.smoothscale(ressource, Tile.size)

    def __init__(self, player_id, board_pos):
        super(Player, self).__init__(self.containers)
        self.id = player_id
        self.board_pos = board_pos
        self.routine = player_routine(self)
        next(self.routine)


    def set_input(self, keys):
        self.move = False
        self.dir = (1,0)


    def update(self):
        self.image = pyg.transform.rotate(self.image_base, degree(self.angle))
        args = self.angle, self.tprop, self.tstop
        self.board_pos = self.routine.send(self.move, self.dir)
        self.graph_pos = self.board_pos * self.size
        self.rect = self.image.get_rect(topleft=self.graph_pos)


