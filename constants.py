import pygame as p
from random import randint

gamestates = ["menu", "game", "gameover", "win"]
screen_width = 640
screen_height = 480
block_size = 32
screen_width_blocks = screen_width // block_size
screen_height_blocks = screen_height // block_size
fps = 60

imgs = {}
imgs_to_load = ["block", "player", "flag"]
for img in imgs_to_load:
    imgs[img] = p.transform.scale(p.image.load(f"imgs/{img}.png"), (block_size, block_size))
