import PIL.Image

from constants import *
from visuals import draw_frame, load_level
from player import Player
from random import randint


def main():
    p.init()
    screen = p.display.set_mode((screen_width, screen_height), p.NOFRAME)
    clock = p.time.Clock()
    player = Player()
    level = load_level("test")
    font = p.font.SysFont(p.font.get_fonts()[randint(0, len(p.font.get_fonts()))], 32)
    p.display.set_caption("Bog Jumper 2.0")
    gamestate = gamestates[0]

    running = True
    while running:
        if gamestate == gamestates[0]:
            # Menu
            gamestate = gamestates[1]

            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

                if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                    running = False

        if gamestate == gamestates[1]:
            # In Game
            gamestate = gamestates[player.update(level)]

            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

                if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                    running = False

                if event.type == p.KEYUP:
                    if event.key == p.K_LEFT:
                        player.x_vel = 0
                    if event.key == p.K_RIGHT:
                        player.x_vel = 0
                    if event.key == p.K_UP:
                        player.y_vel = 0
                    if event.key == p.K_DOWN:
                        player.y_vel = 0

                if event.type == p.KEYDOWN:
                    if event.key == p.K_LEFT:
                        player.x_vel = -0.2
                    if event.key == p.K_RIGHT:
                        player.x_vel = 0.2
                    if event.key == p.K_UP:
                        player.y_vel = -0.2
                    if event.key == p.K_DOWN:
                        player.y_vel = 0.2

        if gamestate == gamestates[2]:
            # Game Over

            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

                if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                    running = False

        if gamestate == gamestates[3]:
            # Win

            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

                if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                    running = False

        draw_frame(screen, imgs, block_size, player, level, font, gamestate)
        clock.tick(fps)
        p.display.update()


if __name__ == "__main__":
    main()
