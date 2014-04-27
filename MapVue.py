import pygame as pyg
from pygame.sprite import Sprite, LayeredDirty, Group, LayeredUpdates
from fps import Fps
from constants import *
from pygame import Surface

class MapVue:
    def __init__(self):
        # Init clock
        self.clock = pyg.time.Clock()

        # Init groupsView
        all_sprites = LayeredUpdates()
        Fps.containers += (all_sprites,)

        size_window = WINDOW_SIZE
        screen = pyg.display.set_mode(size_window)#, FULLSCREEN)
        ico = Surface((32,32))
        pyg.display.set_icon(ico)
        pyg.display.set_caption('Test')
        background = pyg.image.load('background.jpg').convert()
        background = pyg.transform.smoothscale(background, WINDOW_SIZE)
        background.fill(BLACK)
        screen.blit(background, background.get_rect())
        pyg.display.flip()
        from TileVue import TileVue

        TileVue.layer_container = all_sprites
