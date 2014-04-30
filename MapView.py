import pygame as pyg
from pygame.sprite import Sprite, LayeredDirty, Group, LayeredUpdates
from Fps import Fps
from Constants import *
from pygame import Surface, Rect
from Common import reset_screen, safe_exit, countdown
from TileView import GoalView

class MapView:
    def __init__(self, action_handler):
        # Init clock
        self.clock = pyg.time.Clock()

        # Set handler
        self.action_handler = action_handler

        # Init groupsView
        self.all_sprites = LayeredDirty()
        Fps.containers += (self.all_sprites,)

        # Create window
        self.screen, self.background = reset_screen(BACKGROUND_COLOR)
        Fps(self.clock)

        # Tile handling
        from TileView import TileView
        TileView.layer_container = self.all_sprites

        # Initialize attributes
        self.next_level = False
        self.countdown = countdown(GoalView.len_animation)


    def reactor_loop(self):
        # Infinite loop
        while True:
            # Get input
            for ev in pyg.event.get():
                if (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE)\
                   or ev.type == pyg.QUIT:
                    safe_exit()

            # Handle countdown
            if self.next_level and next(self.countdown):
                return self.all_sprites.empty()

            # Read input
            if not self.next_level:
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
