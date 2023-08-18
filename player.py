from collisions import handle_collisions


class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen, imgs, block_size):
        screen.blit(imgs["player"], (self.x * block_size, self.y * block_size))

    def update(self, level):
        handle_collisions(self, level)
