from math import floor, ceil


def check_collision(level, x, y):
    if level[floor(y)][floor(x)] == 1 and level[floor(y)][ceil(x)] == 1:
        return True
    if level[floor(y)][ceil(x)] == 1:
        return True
    if level[ceil(y)][floor(x)] == 1:
        return True
    if level[ceil(y)][ceil(x)] == 1:
        return True
    return False


def handle_collisions(player, level):
    player.x += player.x_vel
    if check_collision(level, player.x, player.y):
        player.x -= player.x_vel
        player.x_vel = 0

    player.y += player.y_vel
    if check_collision(level, player.x, player.y):
        player.y -= player.y_vel
        player.y_vel = 0
