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

""" Module defining useful constants """
import os

# GLOBAL RESSOURCES
RESOURCE_DIR = "data"
ICON_FILE = "icon_exe.png"
INSTRUCTION_FILE = "explication.png"
ENDSCREEN_FILE = "game_ended.png"
CREDITS_FILE = "credits.png"
GAMEOVER_FILE = "game_over.png"

# COLOR
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
GREY = 128,128,128
PURPLE = 255,0,255
YELLOW = 255,255,0
BACKGROUND_COLOR = 38,28,48

# WINDOW
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
REDUCE_FACTOR = 0.9
Y_OFFSET = -75
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
WINDOW_TITLE = "Port Tales"
FULLSCREEN = False
NOFRAME = False

# CONTROLS
RESET_BUTTONS = 3,
VALID_BUTTONS = 0,1,2
THRESHOLD_AXES = 0.8

# LEVEL
NB_LEVELS = 10

# FONT
FONT_NAME = "advanced_led_board.ttf"
FONT_COLOR = 220,0,0
FONT_SIZE = 100
FONT_POS = 200,200

# TIME
FIRST_INSTRUCTION_TIME = 0
INSTRUCTION_TIME = -1
STAGE_TIME = 2
GAMEOVER_TIME = 4
ENDSCREEN_TIME = -1
CREDITS_TIME = -1

# SPRITES
SPRITE_WIDTH = 100

# IMAGE
IMG_FORMAT = "{:04}.png"

# MAP
MAP_DIR = "maps"
MAP_FILE = "map{}.txt"
MAP_FORMAT = os.path.join(MAP_DIR, MAP_FILE)

# SOUND
MUSIC_FILE = ""
VOLUME = 50.0

# FPS
FPS = 40
DISPLAY_FPS = False

