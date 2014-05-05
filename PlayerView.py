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

from TileView import TileView, animation
from random import randint
from XY import XY
from pygame import Surface, Rect

def random_counter(period, random=2):
    current = 0
    while True:
        yield current
        current += randint(1,random)
        current %= period



class PlayerView(TileView):

    folder_dict = {(1, -1,  0) : "red_player_ne",
                   (1,  0,  1) : "red_player_se",
                   (1,  0, -1) : "red_player_nw",
                   (1,  1,  0) : "red_player_sw",
                   (2, -1,  0) : "green_player_ne",
                   (2,  0,  1) : "green_player_se",
                   (2,  0, -1) : "green_player_nw",
                   (2,  1,  0): "green_player_sw"}

    ressource_dict = {key: animation(name) for key, name in folder_dict.items()}
    len_animation = min(len(x) for x in ressource_dict.values())

    def __init__(self, player_id, board_pos, board_id):
        self.board_pos = XY(*board_pos)
        super(PlayerView, self).__init__(self.board_pos, board_id)
        self.id = player_id
        self.dirty = 2
        self.animation = None
        self.set_animation((0,1))
        self.counter = random_counter(self.len_animation)
        self.image = self.animation[next(self.counter)]
        self.moving = False
        self.hidden = False

    def show(self, visible):
        self.visible = visible

    def move(self, delay, hidden):
        self.visible = False
        self.moving = delay
        self.hidden = hidden

    def set_animation(self, hat):
        key = (self.id,) + hat
        self.animation = self.ressource_dict[key]

    def update_pos(self, pos, pos_id):
        self.board_pos = pos
        self.layer_container.change_layer(self, pos_id)

    def update(self):
        if self.moving:
            self.moving -= 1
            self.visible = not (self.moving or self.hidden)
        if self.visible:
            self.image = self.animation[next(self.counter)]
        else:
            self.image = Surface((0,0))
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))


