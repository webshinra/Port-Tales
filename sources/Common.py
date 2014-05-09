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
from pygame import Surface
from Constants import *
import Constants
import pygame.time as time
from XY import XY
from time import clock
import sys, os

countdown = lambda x: (not x for x in xrange(x-1,-1,-1))

class Timer:
    def __init__(self, arg):
        self.arg = arg
    def __enter__(self):
        self.tag = clock()
    def __exit__(self, *arg):
        delta = clock() - self.tag
        print "{} : {:.3} ms".format(self.arg, delta*1000)

# Handle ressources

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, RESOURCE_DIR, relative)
    return os.path.join(RESOURCE_DIR, relative)

def isfile(path):
    return os.path.isfile(resource_path(path))

def load_image(name):
    return pyg.image.load(resource_path(name))

def load_font(name, size):
    return pyg.font.Font(resource_path(name), size)

def load_music(name):
    return pyg.mixer.music.load(resource_path(name))

def open_resource(name):
    return open(resource_path(name))

# Handle exit event

def safe_exit():
    pyg.quit()
    sys.exit()

def check_exit():
    [safe_exit() for ev in pyg.event.get() if ev.type == pyg.QUIT]

# Handle screen

def reset_screen(img_file=None, color=BACKGROUND_COLOR):
    # Test display
    if not pyg.display.get_init():
        pyg.init()
    # Init screen
    flag = pyg.FULLSCREEN #| pyg.DOUBLEBUF | pyg.HWSURFACE
    flag *=  Constants.FULLSCREEN
    flag |= pyg.NOFRAME * NOFRAME
    screen = pyg.display.set_mode(WINDOW_SIZE, flag)
    ico = load_image(ICON_FILE).convert_alpha()
    pyg.display.set_icon(ico)
    pyg.display.set_caption(WINDOW_TITLE)
    # Build background
    background = Surface(WINDOW_SIZE)
    background.fill(color)
    # Get background
    if isinstance(img_file, basestring):
        image = load_image(img_file).convert_alpha()
        width = int(WINDOW_WIDTH * REDUCE_FACTOR)
        height = int(WINDOW_HEIGHT * REDUCE_FACTOR)
        image = pyg.transform.smoothscale(image, (width,height))
        center = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
        background.blit(image, image.get_rect(center=center))
    # Apply background
    screen.blit(background, background.get_rect())
    pyg.display.flip()
    # Return screen
    return screen, background

def get_stage_image(index):
    size = FONT_SIZE
    font = load_font(FONT_NAME, size)
    string = "Stage {:02}/{:02}".format(index, NB_LEVELS)
    image = font.render(string, False, FONT_COLOR).convert_alpha()
    dim = XY(*image.get_size())
    ratio = 2,2
    image = pyg.transform.smoothscale(image, dim/ratio)
    return image, image.get_rect(topleft = (size/2,size/2))

def play_music(file_name, volume=50.0):
    if not pyg.mixer.get_init():
        pyg.mixer.init()
    if file_name:
        load_music(file_name)
        pyg.mixer.music.set_volume(float(volume)/100)
        channel = pyg.mixer.music.play(-1)


def gen_stage_screen(i):
    screen, background = reset_screen()
    font = load_font(FONT_NAME, FONT_SIZE)
    string = "Stage {:02} ...".format(i)
    image = font.render(string, False, FONT_COLOR).convert_alpha()
    rect = image.get_rect().move(FONT_POS)
    screen.blit(image, rect)
    pyg.display.flip()




class TimeControl:
    def __init__(self, delta):
        self.arg_ms = delta*1000

    def __enter__(self):
        self.enter_time = time.get_ticks()

    def __exit__(self, extype, exception, traceback):
        # Check exception type
        if extype is SystemExit:
            safe_exit()
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
        pyg.event.get()
        time.set_timer(custom_event, delta)
        # Game loop
        while True:
            for ev in pyg.event.get():
                if ev.type == pyg.QUIT or \
                  (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE):
                    safe_exit()
                if ev.type in [custom_event, pyg.JOYBUTTONDOWN, pyg.KEYDOWN]:
                    time.set_timer(custom_event, 0)
                    return pyg.event.post(ev)
            clock.tick(FPS)

