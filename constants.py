import pygame as p
from screeninfo import get_monitors

screen_width = 640
screen_height = 480

for monitor in get_monitors():
    if monitor.is_primary:
        screen_width = monitor.width
        screen_height = monitor.height
        break

gamestates = ["menu", "game", "gameover", "win"]
block_size = 32
screen_width_blocks = screen_width // block_size
screen_height_blocks = screen_height // block_size
fps = 144

imgs = {}
imgs_to_load = ["block", "player", "finish"]
for img in imgs_to_load:
    imgs[img] = p.transform.scale(p.image.load(f"imgs/{img}.png"), (block_size, block_size))
