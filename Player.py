import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite, RenderUpdates, Group
from Constants import *
from XY import XY
from TileView import TileView, animation, TeleportingPlayerView, \
                     MinimizingPlayerView, MaximizingPlayerView
from PlayerView import PlayerView
from Tile import Tile, Hole, Floor
from itertools import takewhile, count, cycle
from functools import partial


class Player(Tile):
    def __init__(self, player_id, pos, mp, floor):
        # Build view
        Tile.__init__(self, pos)
        self.view = PlayerView(player_id, pos, mp.get_id(pos))
        # Initialize attributes
        self.map = mp
        self.dir = 1,0
        self.id = player_id
        self.preview = []
        self.success = False
        # Activate first tile
        floor.set_active(True, self.id)

    def update_view(self):
        self.view.update_pos(self.pos, self.map.get_id(self.pos))

    def set_preview(self, active):
        for tile_pos in self.preview:
            tile = self.map.tiles[tile_pos]
            if isinstance(tile, Floor):
                tile.set_active(active, self.id)

    def action(self):
        # Moving case:
        if self.view.moving:
            return

        # Get projection
        projection = self.map.projection(self.id)
        self.pos = projection[-1]

        # Update view
        previous_success = self.success
        success1, success2 = self.map.get_success()
        self.success = (success1 and self.id == 1) or \
                       (success2 and self.id == 2)
        self.generate_animation(projection, self.dir, previous_success)
        self.update_view()

        # End of level
        if success1 and success2:
            self.map.win()
        elif isinstance(self.map.tiles[self.pos], Hole):
            self.map.lose()


    def generate_animation(self, positions, direction, previous_success):
        # Non moving case
        if len(positions) < 2:
            return

        # Minimizing
        if not previous_success:
            # Handle tile if it is floor
            pos = positions[0]
            tile = self.map.tiles[pos]
            if isinstance(tile, Floor):
                callback = partial(tile.set_active, False, self.id)
            else:
                callback = False
            # Prepare animation
            board_id = self.map.get_id(pos)
            MinimizingPlayerView(pos, board_id, direction, 0, callback)

        # Initialize delay
        delay = MinimizingPlayerView.len_animation

        # Teleporting
        for i,pos in enumerate(positions[1:-1]):
            # Handle tile if it is floor
            tile = self.map.tiles[pos]
            if isinstance(tile, Floor):
                callback = partial(tile.set_active, False, self.id)
            else:
                callback = False
            # Prepare animation
            board_id = self.map.get_id(pos)
            TeleportingPlayerView(pos, board_id, direction, delay, callback)
            delay += TeleportingPlayerView.len_animation-1

        # Maximizing
        if not self.success:
            # Handle tile if it is floor
            pos = positions[-1]
            tile = self.map.tiles[pos]
            if isinstance(tile, Floor):
                callback = partial(tile.set_active, True, self.id)
            else:
                callback = False
            # Prepare animation
            delay += 1
            board_id = self.map.get_id(pos)
            MaximizingPlayerView(pos, board_id, direction, delay, callback)
            delay += MaximizingPlayerView.len_animation

        # Moving player
        self.view.move(delay + 1, self.success)


    def rotate(self, hat):
        # Moving case:
        if self.view.moving:
            return

        # Rotate view
        self.dir = hat
        self.view.set_animation(self.dir)

        # Set new preview
        self.set_preview(False)
        self.preview = self.map.projection(self.id)
        self.set_preview(True)







