import pygame as p
from levels import *
from player import Player

screen_width = 640
screen_height = 480
block_size = 32
screen_width_blocks = screen_width // block_size
screen_height_blocks = screen_height // block_size
fps = 60

imgs = {}
imgs_to_load = ["block", "player"]
for img in imgs_to_load:
    imgs[img] = p.transform.scale(p.image.load(f"imgs/{img}.png"), (block_size, block_size))


def main():
    p.init()
    screen = p.display.set_mode((screen_width, screen_height))
    clock = p.time.Clock()
    player = Player()
    level = load_level("test")
    print(level)
    p.display.set_caption("Bog Jumper 2.0")

    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    player.x_vel = -0.25
                if event.key == p.K_RIGHT:
                    player.x_vel = 0.25
                if event.key == p.K_UP:
                    player.y_vel = -0.25
                if event.key == p.K_DOWN:
                    player.y_vel = 0.25
            if event.type == p.KEYUP:
                if event.key == p.K_LEFT:
                    player.x_vel = 0
                if event.key == p.K_RIGHT:
                    player.x_vel = 0
                if event.key == p.K_UP:
                    player.y_vel = 0
                if event.key == p.K_DOWN:
                    player.y_vel = 0

        screen.fill(p.Color("black"))
        player.update(level)
        draw_level(screen, imgs, block_size, level)
        player.draw(screen, imgs, block_size)
        clock.tick(fps)
        p.display.update()


if __name__ == "__main__":
    main()
