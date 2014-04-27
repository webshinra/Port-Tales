import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from Constants import *
from XY import XY
from TileView import TileView, animation, counter
from Tile import Tile
import os
from itertools import takewhile, count, cycle

class Player(Tile):
    def __init__(self, player_id, pos, mp):
        Tile.__init__(self, *pos)
        self.map = mp
        self.view = PlayerView(player_id, pos, self.map.get_id(pos))
        self.dir = 1,0
        self.id = player_id

    def action(self):
        target = self.map.projection(self.id)[-1]
        self.x = target[0]
        self.y = target[1]

        success = self.map.success()
        if (success):
            self.map.reset()
            otherId = 2 if self.id == 1 else 1
            self.map.players[otherId].update_view()

        self.update_view()

    def update_view(self):
        self.view.board_pos = pos = XY(self.x, self.y)
        TileView.layer_container.change_layer(self.view, self.map.get_id(pos))

    def rotate(self, hat):
        self.dir = hat
        self.view.set_animation(hat)



class PlayerView(TileView):

    folder_dict = {(1, -1,  0) : "red_player_ne",
                   (1,  0,  1) : "red_player_se",
                   (1,  0, -1) : "red_player_nw",
                   (1,  1,  0): "red_player_sw",
                   (2, -1,  0) : "green_player_ne",
                   (2,  0,  1) : "green_player_se",
                   (2,  0, -1) : "green_player_nw",
                   (2,  1,  0): "green_player_sw"}

    ressource_dict = {key: animation(name) for key, name in folder_dict.items()}
    len_animation = min(len(x) for x in ressource_dict.values())

    def __init__(self, player_id, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(PlayerView, self).__init__(self.board_pos, board_id)
        self.id = player_id
        self.dirty = 2
        self.animation = None
        self.set_animation((0,1))
        self.counter = counter(self.len_animation, cyclic=True)
        self.image = self.animation[next(self.counter)]

    def show(self, visible):
        self.visible = visible

    def set_animation(self, hat):
        key = (self.id,) + hat
        self.animation = self.ressource_dict[key]

    def convert(self, pos):
        pos = XY(pos.y-pos.x, pos.x+pos.y)
        factor_y = (self.width-4)/(2*3**0.5)
        pos *= (self.width-4)*0.5, factor_y
        pos += self.width*self.nb_lines/2, 0
        return XY(*map(int,pos))

    def update(self):
        if self.visible:
            self.image = self.animation[next(self.counter)]
        else:
            self.image = Surface((0,0))
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))


