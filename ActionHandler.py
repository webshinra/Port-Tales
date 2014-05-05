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
from pygame import Surface, joystick
from Constants import *
from XY import XY

class Input:
    def __init__(self, direction=(0,0), valid=False):
        self.dir = direction
        self.valid = valid

trigo_to_mat = {( 0,  0) : ( 0 , 0),
                ( 1,  1) : (-1,  0),
                ( 1, -1) : ( 0,  1),
                (-1,  1) : ( 0, -1),
                (-1, -1) : ( 1,  0),
                ( 0,  1) : (-1,  0),
                ( 1,  0) : ( 0,  1),
                (0,  -1) : ( 1,  0),
                (-1,  0) : ( 0, -1),}

def is_valid(js):
    return (js.get_numaxes() > 1 or js.get_numhats()) and js.get_numbuttons()


class Controller:

    validkey_mapping = {1: pyg.K_SPACE,
                        2: pyg.K_RETURN}

    dirkey_mapping = {1: {pyg.K_w: ( 0,  1),
                          pyg.K_d: ( 1,  0),
                          pyg.K_s: ( 0, -1),
                          pyg.K_a: (-1,  0)},
                      2: {pyg.K_UP:    ( 0,  1),
                          pyg.K_RIGHT: ( 1,  0),
                          pyg.K_DOWN:  ( 0, -1),
                          pyg.K_LEFT:  (-1,  0)}
                          }

    def __init__(self, id_keyboard, js=None):
        self.id = id_keyboard
        self.joystick = js
        self.has_js = js is not None
        self.has_axes = self.has_hat = self.has_button = 0
        if self.has_js:
            self.has_axes = js.get_numaxes() > 1
            self.has_hat = js.get_numhats() > 0
            self.has_button = js.get_numbuttons() > 0

    def get_dir(self):
        if self.has_axes:
            values = self.joystick.get_axis(0), self.joystick.get_axis(1)
            mod = abs(complex(*values))
            # Axes control
            if mod > THRESHOLD_AXES:
                key = tuple(cmp(value,0) for value in values)
                key = XY(*key) * (1,-1)
                return trigo_to_mat[key]
        if self.has_hat:
            key = self.joystick.get_hat(0)
            # Filter for arcade stick
            diagonal = sum(abs(v) for v in key) == 2
            if not self.has_axes and not diagonal:
                key= 0,0
            # Return direction
            if key != (0,0):
                return trigo_to_mat[key]
        # Keyboard handling
        values = XY(0,0)
        keyboard = pyg.key.get_pressed()
        for key, value in self.dirkey_mapping[self.id].items():
            if keyboard[key]:
                values += value
        return trigo_to_mat[values]


    def get_valid(self):
        if self.has_button:
            if any(self.joystick.get_button(key) for key in VALID_BUTTONS):
                return True
        key = self.validkey_mapping[self.id]
        return pyg.key.get_pressed()[key]


class ActionHandler:
    def __init__(self):
        # Get controllers
        joystick.init()
        joys = [joystick.Joystick(x) for x in range(joystick.get_count())]
        [js.init() for js in joys if not js.get_init()]
        joy_gen = (js for js in joys if is_valid(js))
        # Set attributes
        self.controllers = [Controller(i, next(joy_gen, None)) for i in (1,2)]
        self.players = [None,None]
        self.buffers = [Input(), Input()]
        self.triggered = [Input(), Input()]
        self.zipable = self.players, self.controllers, \
                       self.buffers, self.triggered


    def add_player(self, id_player, player):
        self.players[id_player-1] = player

    def read_inputs(self):
        for player, controller, buff, trigger in zip(*self.zipable):
            # Get current input
            current = Input(controller.get_dir(), controller.get_valid())
            # Compare with buffer
            if current.dir != buff.dir:
                trigger.dir = current.dir
            else:
                trigger.dir = 0,0
            trigger.valid = current.valid and not buff.valid
            # Set buffer
            buff.dir = current.dir
            buff.valid = current.valid
            # Perform actions
            if trigger.dir != (0,0):
                player.rotate(trigger.dir)
            if trigger.valid:
                player.action()





