import pygame as pyg
from pygame import Surface
from Constants import *
import pygame.time as time
import sys

def safe_exit():
    pyg.quit()
    sys.exit()

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

def play_music(file_name, volume=50.0):
    if not pyg.mixer.get_init():
        pyg.mixer.init()
    pyg.mixer.music.load(file_name)
    pyg.mixer.music.set_volume(float(volume)/100)
    channel = pyg.mixer.music.play(-1)


class TimeControl:
    def __init__(self, delta):
        self.arg_ms = delta*1000

    def __enter__(self):
        self.enter_time = time.get_ticks()

    def __exit__(self, *args):
        # Compute delta
        delta = self.enter_time + self.arg_ms - time.get_ticks()
        # Handle case delta == 0
        delta += not delta
        # Validate delta with sign of the argument
        delta *= self.arg_ms >= 0
        # Return if no need to wait
        if delta < 0:
            return
        # Prepare timer event
        custom_event = pyg.USEREVENT + 1
        clock = time.Clock()
        time.set_timer(custom_event, delta)
        # Game loop
        while True:
            for ev in pyg.event.get():
                if ev.type == custom_event or \
                   (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE):
                    time.set_timer(custom_event, 0)
                    return pyg.event.post(ev)
                if ev.type == pyg.QUIT:
                    safe_exit()
            clock.tick(FPS)

