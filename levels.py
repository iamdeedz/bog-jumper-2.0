def load_level(level):
    with open(f"levels/{level}.bjlevel", 'r') as lvlFile:
        return [[int(char) for char in line] for line in [line.split() for line in [line.strip() for line in lvlFile]]] # wow, that's a lot of list comprehensions # NOQA: PEP 8: E501


def draw_level(screen, imgs, block_size, level):
    for y, line in enumerate(level):
        for x, char in enumerate(line):
            if char == 1:
                screen.blit(imgs["block"], (x * block_size, y * block_size))
