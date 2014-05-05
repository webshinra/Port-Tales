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

class Input:
    def __init__(self, hat=(0,0), button=False):
        self.hat = hat
        self.button = button

trigo_to_mat = {( 1,  1) : (-1,  0),
                ( 1, -1) : ( 0,  1),
                (-1,  1) : ( 0, -1),
                (-1, -1) : ( 1,  0)}

extended = {( 0,  1) : (-1,  0),
            ( 1,  0) : ( 0,  1),
            (0,  -1) : ( 1,  0),
            (-1,  0) : ( 0, -1),}

if EXTENDED_CONTROLS:
    trigo_to_mat.update(extended)

def is_valid(js):
    return js.get_numhats() and js.get_numbuttons()


class FakePlayer:
    def __init__(self, arg):
        self.id = arg

    def action(self):
        print("Action {}".format(self.id))

    def rotate(self, arg):
        print("Rotate {} to {}".format(self.id, arg))

class ActionHandler:
    def __init__(self):
        # Get controllers
        joystick.init()
        controllers = [joystick.Joystick(x) for x in range(joystick.get_count())]
        [js.init() for js in controllers if not js.get_init()]
        controllers = [js for js in controllers if is_valid(js)]
        if len(controllers) < 2:
            msg = "{} over 2 valid joysticks detected".format(len(controllers))
            #raise RuntimeError(msg)
        # Set attributes
        try:
            self.controllers = controllers[:2]
        except:
            self.controllers = [None, None]
        # Set attributes
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
            current = Input(controller.get_hat(0), controller.get_button(0))
            # Compare with buffer
            if current.hat != buff.hat:
                trigger.hat = current.hat
            else:
                trigger.hat = 0,0
            trigger.button = current.button and not buff.button
            # Set buffer
            buff.hat = current.hat
            buff.button = current.button
            # Perform actions
            limit = 0 if EXTENDED_CONTROLS else 1
            if sum(map(abs, trigger.hat)) > limit:
                player.rotate(trigo_to_mat[trigger.hat])
            if trigger.button:
                player.action()





