import pygame as pyg
from pygame import Surface
from Constants import *

def reset_screen(background_arg = BLACK):
    # Test display
    if not pyg.display.get_init():
        pyg.init()
    # Init screen
    flag = pyg.FULLSCREEN * FULLSCREEN
    flag |= pyg.NOFRAME * NOFRAME
    screen = pyg.display.set_mode(WINDOW_SIZE, flag)
    ico = pyg.image.load(ICON_FILE).convert_alpha()
    pyg.display.set_icon(ico)
    pyg.display.set_caption(WINDOW_TITLE)
    # Get background
    if isinstance(background_arg, tuple):
        background = Surface(WINDOW_SIZE)
        background.fill(background_arg)
    elif isinstance(background_arg, basestring):
        background = pyg.image.load(background_arg).convert_alpha()
        background = pyg.transform.smoothscale(background, WINDOW_SIZE)
    else:
        raise AttributeError("Attribute must be a string or a tuple")
    # Apply background
    screen.blit(background, background.get_rect())
    pyg.display.flip()
    # Return screen
    return screen, background

def play_music(file_name, volume=0.5):
    if not pyg.mixer.get_init():
        pyg.mixer.init()
    pyg.mixer.music.load(file_name)
    pyg.mixer.music.set_volume(volume)
    channel = pyg.mixer.music.play(-1)
