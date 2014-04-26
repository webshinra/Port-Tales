import pygame as pyg
from pygame import Surface
from pygame.sprite import Sprite
from constants import *

class Fps(Sprite):
    """ Sprite class to display the FPS rate """

    color = BLACK
    containers = ()

    def __init__(self,clock):
        super(Fps, self).__init__(self.containers)
        self.enable = True
        self.clock = clock
        self.image = Surface((0,0))
        try :
            self.font = pyg.font.Font('visitor2.ttf', 20)
        except Exception :
            self.enable = False

    def update(self):
        if self.enable :
            string = "FPS = {}".format(int(self.clock.get_fps()))
            self.image = self.font.render(string, False, self.color)
        self.rect = self.image.get_rect().move(10,5)