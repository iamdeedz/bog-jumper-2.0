from events import handle_events


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen, imgs, block_size):
        screen.blit(imgs["player"], (self.x * block_size, self.y * block_size))

    def update(self, level):
        gamestate = handle_events(self, level)
        return gamestate
