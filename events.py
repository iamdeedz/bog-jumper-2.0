from math import floor, ceil


def check_collision(level, x, y):
    try:
        if level[floor(y)][floor(x)].is_solid:
            return True
        if level[floor(y)][ceil(x)].is_solid:
            return True
        if level[ceil(y)][floor(x)].is_solid:
            return True
        if level[ceil(y)][ceil(x)].is_solid:
            return True

    except IndexError:
        return False

    return False


def check_flag_collision(level, x, y):
    if x < 0 or y < 0:
        return False
    
    try:
        if level[floor(y)][floor(x)].is_win:
            return True
        if level[floor(y)][ceil(x)].is_win:
            return True
        if level[ceil(y)][floor(x)].is_win:
            return True
        if level[ceil(y)][ceil(x)].is_win:
            return True

    except IndexError:
        return False

    return False


def handle_events(player, level):
    next_gamestate = 1

    # Walls
    player.x += player.x_vel
    if check_collision(level, player.x, player.y):
        player.x -= player.x_vel
        player.x_vel = 0

    player.y += player.y_vel
    if check_collision(level, player.x, player.y):
        player.y -= player.y_vel
        player.y_vel = 0

    # Flag
    if check_flag_collision(level, player.x, player.y):
        next_gamestate = 3

    return next_gamestate
