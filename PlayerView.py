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
                   (1,  1,  0): "red_player_sw",
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

    def show(self, visible):
        self.visible = visible

    def move(self, delay):
        self.visible = False
        self.moving = delay

    def set_animation(self, hat):
        key = (self.id,) + hat
        self.animation = self.ressource_dict[key]

    def update(self):
        if self.moving:
            self.moving -= 1
            self.visible = not self.moving
        if self.visible:
            self.image = self.animation[next(self.counter)]
        else:
            self.image = Surface((0,0))
        self.rect = self.image.get_rect(topleft=self.convert(self.board_pos))