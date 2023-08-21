import pygame as p
from constants import gamestates


def load_level(level):
    with open(f"levels/{level}.bjlevel", 'r') as lvlFile:
        return [[int(char) for char in line] for line in [line.split() for line in [line.strip() for line in lvlFile]]] # wow, that's a lot of list comprehensions # NOQA: PEP 8: E501


def draw_level(screen, imgs, block_size, level):
    for y, line in enumerate(level):
        for x, char in enumerate(line):
            if char == 1:
                screen.blit(imgs["block"], (x * block_size, y * block_size))

            if char == 2:
                screen.blit(imgs["flag"], (x * block_size, y * block_size))


def draw_game(screen, imgs, block_size, player, level):
    screen.fill("black")
    draw_level(screen, imgs, block_size, level)
    player.draw(screen, imgs, block_size)


def draw_win(screen, font):
    screen.fill("grey 50")
    text = font.render("You Win!", True, "white")
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))


def draw_frame(screen, imgs, block_size, player, level, font, gamestate):
    if gamestate == gamestates[0]:
        # Menu
        pass

    if gamestate == gamestates[1]:
        # In Game
        draw_game(screen, imgs, block_size, player, level)

    if gamestate == gamestates[2]:
        # Game Over
        pass

    if gamestate == gamestates[3]:
        # Win
        draw_win(screen, font)

    p.display.update()
