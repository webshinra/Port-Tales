import pygame as pyg
from pygame.sprite import Sprite, LayeredDirty, Group, LayeredUpdates
from Fps import Fps
from Constants import *
from pygame import Surface

class MapView:
    def __init__(self, action_handler):
        # Init clock
        self.clock = pyg.time.Clock()

        # Set handler
        self.action_handler = action_handler

        # Init groupsView
        self.all_sprites = LayeredUpdates()
        Fps.containers += (self.all_sprites,)

        # Create window
        self.screen = pyg.display.set_mode(WINDOW_SIZE)#, pyg.FULLSCREEN)
        ico = Surface((32,32))
        pyg.display.set_icon(ico)
        pyg.display.set_caption('Test')

        # Apply background
        self.background = Surface(WINDOW_SIZE)
        self.background.fill(BACKGROUND)
        self.screen.blit(self.background, self.background.get_rect())
        pyg.display.flip()
        Fps(self.clock)

        # Tile handling
        from TileView import TileView
        TileView.layer_container = self.all_sprites


    def reactor_loop(self):
        # Infinite loop
        while True:
            # Get input
            for ev in pyg.event.get():
                if ev.type == pyg.QUIT or \
                    (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE):
                        self.all_sprites.empty()
                        #pyg.quit()
                        return

            # Read input
            self.action_handler.read_inputs()

            # Clear sprites from screen
            self.all_sprites.clear(self.screen, self.background)

            # Update sprites
            self.all_sprites.update()

            # Draw sprites on screen
            dirty = self.all_sprites.draw(self.screen)

            # Update display
            pyg.display.flip()
            #pyg.display.update(dirty)

            # Frame rate control
            self.clock.tick(30)
