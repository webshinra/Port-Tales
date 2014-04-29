from XY import XY
import pygame as pyg
from pygame import Surface, Rect
from pygame.sprite import DirtySprite, Sprite
from itertools import takewhile, count, cycle
import os
from Constants import *


countdown = lambda x: xrange(x-1,-1,-1)

def counter(period, reverse= False, cyclic = False):
    current = period-1 if reverse else 0
    inc = -1 if reverse else +1
    while True:
        reverse = yield current
        if reverse is not None:
            inc = -5 if reverse else 1
        current += inc
        if not cyclic and current < 0:
            break
        current %= period
        if not cyclic and not current:
            break
    if reverse:
        yield 0

def animation(folder):
        names = (os.path.join(folder, "{:04}.png".format(i)) for i in count(1))
        names = takewhile(os.path.isfile , names)
        return [TileView.resize_ressource(name) for name in names]

class TileView(DirtySprite):

    width = SPRITE_WIDTH
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

class HoleView(TileView):

    ressource_name = "black_hole_repos/0001.png"
    ressource = TileView.resize_ressource(ressource_name)

    def __init__(self, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(HoleView, self).__init__(self.board_pos, board_id)
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

    folder_dict = {1 : "goal_red",
                   2 : "goal_green"}

    ressource_dict = {key: animation(name) for key, name in folder_dict.items()}
    len_animation = min(len(x) for x in ressource_dict.values())

    def __init__(self, goal_id, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(GoalView, self).__init__(self.board_pos, board_id)
        self.id = goal_id
        self.animation = self.ressource_dict[self.id]
        self.counter = None
        self.image = self.animation[0]
        self.moving = False
        self.deployed = False

    def set_active(self, active):
        if active ^ self.deployed:
            self.moving = True
        self.deployed = active


    def update_image(self):
        if not self.moving:
            return
        elif not self.counter:
            self.counter = counter(self.len_animation, not self.deployed)
            next(self.counter)
        try:
            self.image = self.animation[self.counter.send(not self.deployed)]
        except StopIteration:
            self.moving = False
            self.counter = None

    def update(self):
        self.update_image()
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))

    def convert(self, pos):
        pos = XY(pos.y-pos.x, pos.x+pos.y)
        factor_y = (self.width-4)/(2*3**0.5)
        pos *= (self.width-4)*0.5, factor_y
        pos += self.width*self.nb_lines/2, -19
        return XY(*map(int,pos))
