import pygame as pyg
from pygame import Surface
from Constants import *

def reset_screen():
    # Test display
    if not pyg.display.get_init():
        pyg.init()
    # Init screen
    screen = pyg.display.set_mode(WINDOW_SIZE)#, pyg.FULLSCREEN)
    ico = Surface((32,32))
    pyg.display.set_icon(ico)
    pyg.display.set_caption('Test')
    # Apply background
    background = Surface(WINDOW_SIZE)
    background.fill(BACKGROUND)
    screen.blit(background, background.get_rect())
    pyg.display.flip()
    # Return screen
    return screen, background