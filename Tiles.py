from TilesVue import BlockVue, FloorVue, BorderVue
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.vue = 0
    
class Block(Tile):
    def __init__(self, x, y):
        super(Block, self).__init__(x,y)
        self.vue = BlockVue((self.x, self.y))

class Floor(Tile):
    def __init__(self, x, y):
        super(Floor, self).__init__(x,y)
        self.vue = FloorVue((self.x, self.y))

class Border(Tile):
    def __init__(self, x, y):
        super(Floor, self).__init__(x,y)
        self.vue = FloorVue((self.x, self.y))
