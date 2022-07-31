from recursive_backtracker import *
from collections import deque

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

running = True

maze = generate_maze_recursive_backtracker()




while running:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [cell.draw(sc) for cell in maze]

    

    pygame.display.flip()
    clock.tick(60)
