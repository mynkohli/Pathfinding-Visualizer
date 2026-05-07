import pygame

from grid.node import Node
from utils.colors import *
from utils.constants import *

def make_grid():

    grid = []

    gap = WIDTH // ROWS

    for i in range(ROWS):

        grid.append([])

        for j in range(ROWS):

            node = Node(i, j, gap, ROWS)

            grid[i].append(node)

    return grid

def draw_grid(win):

    gap = WIDTH // ROWS

    for i in range(ROWS):

        pygame.draw.line(
            win,
            GREY,
            (0, i * gap),
            (WIDTH, i * gap)
        )

        for j in range(ROWS):

            pygame.draw.line(
                win,
                GREY,
                (j * gap, 0),
                (j * gap, WIDTH)
            )

def draw(win, grid):

    win.fill(WHITE)

    for row in grid:

        for node in row:

            node.draw(win)

    draw_grid(win)

    pygame.display.update()