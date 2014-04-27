import pygame as pyg
from pygame import Surface, joystick

class Input:
    def __init__(self, hat=(0,0), button=False):
        self.hat = hat
        self.button = button

trigo_to_mat = {( 1,  1) : (-1,  0),
                ( 1, -1) : ( 0,  1),
                (-1,  1) : ( 0, -1),
                (-1, -1) : ( 1,  0)}

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
            raise RuntimeError(msg)
        # Set attributes
        self.controllers = controllers[:2]
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
            if sum(map(abs, trigger.hat)) == 2:
                player.rotate(trigo_to_mat[trigger.hat])
            if trigger.button:
                player.action()





