from constants import imgs


class Tile:
    def __init__(self):
        self.img = imgs[self.__class__.__name__.lower()] if self.__class__.__name__.lower() != "air" else None
        self.is_solid = True
        self.is_win = False

    def draw(self, screen, x, y, block_size):
        if self.img:
            screen.blit(self.img, (x * block_size, y * block_size))


class Block(Tile):
    def __init__(self):
        super().__init__()


class Finish(Tile):
    def __init__(self):
        super().__init__()
        self.is_solid = False
        self.is_win = True


class Air(Tile):
    def __init__(self):
        super().__init__()
        self.is_solid = False


tiles = {0: Air, 1: Block, 2: Finish}
