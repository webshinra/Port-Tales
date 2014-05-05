# this file is part of Port Tales
# Copyright (C) 2014
# Yann Asset <shinra@electric-dragons.org>, 
# Vincent Michel <vxgmichel@gmail.com>,
# Cyril Savary <cyrilsavary42@gmail.com>
  
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame as pyg
from pygame.sprite import Sprite, LayeredDirty, Group, LayeredUpdates
from Fps import Fps
from Constants import *
from pygame import Surface, Rect
from Common import reset_screen, safe_exit, countdown, get_stage_image
from TileView import GoalView, FallingPlayerView, \
                     MinimizingPlayerView, TeleportingPlayerView

class MapView:
    def __init__(self, action_handler, index):
        # Init clock
        self.clock = pyg.time.Clock()

        # Set handler
        self.action_handler = action_handler

        # Init groupsView
        self.all_sprites = LayeredDirty()
        Fps.containers += (self.all_sprites,)

        # Create window
        self.screen, self.background = reset_screen()
        if DISPLAY_FPS:
            Fps(self.clock)

        # Blit level
        image, rect = get_stage_image(index)
        self.background.blit(image, rect)

        # Tile handling
        from TileView import TileView
        TileView.layer_container = self.all_sprites

        # Initialize attributes
        self.exit = False
        self.done = False
        self.countdown = None

    def win(self):
        self.done = True
        self.win = True
        self.countdown = countdown(GoalView.len_animation)

    def lose(self, nb_tiles):
        self.done = True
        self.win = False
        value = MinimizingPlayerView.len_animation
        value += TeleportingPlayerView.len_animation * (nb_tiles-2)
        value += FallingPlayerView.len_animation
        value *= 2
        self.countdown = countdown(value)


    def reactor_loop(self):
        # Infinite loop
        while True:
            # Get input
            for ev in pyg.event.get():
                # Quit
                if (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE)\
                   or ev.type == pyg.QUIT:
                    safe_exit()
                # Reset
                if ev.type == pyg.JOYBUTTONDOWN and \
                   ev.button in RESET_BUTTONS:
                    win_reset = False, True
                    return win_reset

            # Handle countdown
            if self.done and next(self.countdown):
                self.all_sprites.empty()
                win_reset = self.win, False
                return win_reset

            # Read input
            if not self.done:
                self.action_handler.read_inputs()

            # Clear sprites from screen
            self.all_sprites.clear(self.screen, self.background)

            # Update sprites
            self.all_sprites.update()

            # Draw sprites on screen
            dirty = self.all_sprites.draw(self.screen)

            # Update display
            pyg.display.flip()

            # Frame rate control
            self.clock.tick(FPS)
