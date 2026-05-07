import pygame
from queue import Queue

def reconstruct_path(came_from, current, draw):

    while current in came_from:

        current = came_from[current]

        current.make_path()

        draw()

def bfs(draw, start, end):

    queue = Queue()

    queue.put(start)

    came_from = {}

    visited = {start}

    while not queue.empty():

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

        current = queue.get()

        if current == end:

            reconstruct_path(came_from, end, draw)

            end.make_end()

            return True

        for neighbor in current.neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                came_from[neighbor] = current

                queue.put(neighbor)

                neighbor.make_open()

        draw()

        if current != start:

            current.make_closed()

    return False