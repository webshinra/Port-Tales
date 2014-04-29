import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from Constants import *
from XY import XY
from TileView import TileView, animation, TeleportingPlayerView
from PlayerView import PlayerView
from Tile import Tile
from itertools import takewhile, count, cycle


class Player(Tile):
    def __init__(self, player_id, pos, mp):
        Tile.__init__(self, *pos)
        self.map = mp
        self.view = PlayerView(player_id, pos, self.map.get_id(pos))
        self.dir = 1,0
        self.id = player_id
        self.preview = []

    def action(self):
        projection = self.map.projection(self.id)
        self.generate_animation(projection, self.dir)
        target = projection[-1]
        self.x = target[0]
        self.y = target[1]

        if (self.map.mat[self.x][self.y] == 7): #hole
            self.map.reset()
            otherId = 2 if self.id == 1 else 1
            self.map.players[otherId].update_view()


        success = self.map.success()
        if (success):
            self.map.next_level()
            return

        self.update_view()
        for tile in self.preview:
            tileId = self.map.mat[tile[0]][tile[1]]
            if (tileId == 1 or tileId == 4 or tileId == 5):
                self.map.tiles[tile[0], tile[1]].view.reset()

    def generate_animation(self, positions, direction):
        for i,pos in enumerate(positions):
            delay = (TeleportingPlayerView.len_animation/2) * i
            TeleportingPlayerView(pos, self.map.get_id(pos), direction, delay)


    def update_view(self):
        self.view.board_pos = pos = XY(self.x, self.y)
        TileView.layer_container.change_layer(self.view, self.map.get_id(pos))

    def rotate(self, hat):
        self.dir = hat
        self.view.set_animation(hat)


        for tile in self.preview:
            tileId = self.map.mat[tile[0]][tile[1]]
            if (tileId == 1 or tileId == 4 or tileId == 5):
                self.map.tiles[tile[0], tile[1]].view.reset()


        self.preview = self.map.projection(self.id)
        ressource_name = "floor_red.png"
        if (self.id == 2):
            ressource_name = "floor_green.png"

        for tile in self.preview:
            tileId = self.map.mat[tile[0]][tile[1]]
            if (tileId == 1 or tileId == 4 or tileId == 5):
                self.map.tiles[tile[0], tile[1]].view.image = TileView.resize_ressource(ressource_name)






