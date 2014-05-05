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
from pygame.sprite import DirtySprite
from Common import load_font
from Constants import *

class Fps(DirtySprite):
    """ Sprite class to display the FPS rate """

    color = BLACK
    containers = ()

    def __init__(self,clock):
        super(Fps, self).__init__(self.containers)
        self.dirty = 2
        self.visible = True
        self.clock = clock
        self.image = Surface((0,0))
        try :
            self.font = load_font('visitor2.ttf', 20)
        except Exception :
            self.visible = False
            self.dirty = 0

    def update(self):
        if self.visible :
            string = "FPS = {}".format(int(self.clock.get_fps()))
            self.image = self.font.render(string, False, self.color)
        self.rect = self.image.get_rect().move(10,5)
