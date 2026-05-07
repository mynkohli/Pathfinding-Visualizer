import pygame

from grid.grid import *
from algorithms.bfs import bfs
from utils.constants import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("Pathfinding Visualizer")

def get_clicked_pos(pos):

    gap = WIDTH // ROWS

    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main():

    grid = make_grid()

    start = None
    end = None

    run = True

    while run:

        draw(WIN, grid)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()

                row, col = get_clicked_pos(pos)

                node = grid[row][col]

                if not start and node != end:

                    start = node

                    start.make_start()

                elif not end and node != start:

                    end = node

                    end.make_end()

                elif node != start and node != end:

                    node.make_barrier()

            # RIGHT CLICK
            elif pygame.mouse.get_pressed()[2]:

                pos = pygame.mouse.get_pos()

                row, col = get_clicked_pos(pos)

                node = grid[row][col]

                node.reset()

            # START BFS
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and start and end:

                    for row in grid:

                        for node in row:

                            node.update_neighbors(grid)

                    bfs(
                        lambda: draw(WIN, grid),
                        start,
                        end
                    )

    pygame.quit()

main()