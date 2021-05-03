import copy
import csv
import sys

import pygame

# The size of the grid, in number of cells
# horizontally and vertically.
#
# With WIDTH = 3 and HEIGHT = 3 we
# could have a grid such as:
# [
#    [0,0,1],
#    [0,1,1],
#    [0,0,1],
# ]
WIDTH = 40
HEIGHT = 40

# The cell width and height in pixels when drawing.
CELL_WIDTH = 25
CELL_HEIGHT = 25


def create_row_zeros(length):
    result= []
    for i in range(length):
        result.append(0)
    return result


def create_empty_grid(width, height):
    """Create an empty grid of size width x height

    All cells are 0 indicating the all cells are dead.

    width: the width of the grid in cells
    height: the height of the grid in cells
    """
    result = []
    for i in range(height):
        result.append(create_row_zeros(width))
    return result


def get_left(grid, x, y):
    """Return the value on the left of the cell.

    grid: the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the left border, return 0.
    """
    if x == 0:
        return 0
    result = grid[y][x - 1]
    return result



def get_right(grid, width, x, y):
    """Return the value on the right of the cell.

    grid: the grid
    width: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the right border, return 0.
    """
    if x == width - 1:
        return 0
    result = grid[y][x + 1]
    return result


def get_top(grid, x, y):
    """Return the value above of the cell.

    grid: the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the top row, return 0.
    """
    if y == 0:
        return 0
    result = grid[y - 1][x]
    return result


def get_bottom(grid, height, x, y):
    """Return the value below of the cell.

    grid: the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the bottom row, return 0.
    """
    if y == height - 1:
        return 0
    result = grid[y+1][x]
    return result



def get_topleft(grid, x, y):
    """Return the value on the top left of the cell.

    grid: the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the top row, return 0.
    If the cell is on the left column, return 0.
    """
    if x == 0:
        return 0
    if y == 0:
        return 0
    result = grid[y-1][x-1]
    return result


def get_topright(grid, width, x, y):
    """Return the value on the top right of the cell.

    grid: the grid
    width: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the top row, return 0.
    If the cell is on the last column , return 0.
    """
    if x == width -1:
        return 0
    if y == 0:
        return  0
    result = grid[y-1][x+1]
    return result


def get_bottomleft(grid, height, x, y):
    """Return the value on the bottom left of the cell.

    grid: the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the last row, return 0.
    If the cell is on the first column , return 0.
    """
    if x == 0:
        return 0
    if y == height - 1:
        return 0
    result = grid[y+1][x-1]
    return result


def get_bottomright(grid, width, height, x, y):
    """Return the value on the bottom right of the cell.

    grid: the grid
    width: the width of the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell

    If the cell is on the last row, return 0.
    If the cell is on the last column , return 0.
    """
    if x == width - 1:
        return 0
    if y == height - 1:
        return 0
    result = grid[y+1][x+1]
    return result


def get_neighbours(grid, width, height, x, y):
    """Return a list of values of all 8 neighbours of the cell.

    grid: the grid
    width: the width of the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell
    """

    result = []

    result.append(get_topleft(grid, x, y))
    result.append(get_top(grid, x, y))
    result.append(get_topright(grid, width, x, y))
    result.append(get_right(grid, width, x, y))
    result.append(get_bottomright(grid, width, height, x, y))
    result.append(get_bottom(grid, height, x, y))
    result.append(get_bottomleft(grid, height, x, y))
    result.append(get_left(grid, x, y))
    return result




def count_neighbours(grid, width, height, x, y):
    """Return the number of living neighbours.

    The neighbours are living if they are not 0.

    grid: the grid
    width: the width of the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell
    """
    result = get_neighbours(grid, width, height, x, y)
    som = 0
    for i in result:
         som = som + i

    return som



def live_or_die(grid, width, height, x, y):
    """Return True if the current cell lives, False if it dies.

    The current cell keeps living if it was currently alive,
    and has 2 or 3 living neighbours.
    The current cell lives again, if it was currently dead,
    but has 3 living neighbours.

    In all other cases, the current cell dies.

    grid: the grid
    width: the width of the grid
    height: the width of the grid
    x: the x-position of the cell
    y: the y-position of the cell
    """
    result = get_neighbours(grid, width, height, x, y)
    if grid[y][x] == 0
        return false
    if grid[y][x] == 1
        return true


    return result


def update_grid(grid, width, height):
    """Update the grid according to the game of live rules"""
    # Create a copy of the current grid.
    original_grid = copy.deepcopy(grid)
    # Determine for each cell if the cell lives or dies
    # and update the grid accordingly.
    for y, row in enumerate(original_grid):
        for x, _ in enumerate(row):
            alive = live_or_die(original_grid, width, height, x, y)
            if alive:
                grid[y][x] = 1
            else:
                grid[y][x] = 0


def read_map(grid, filename):
    """Read a spreadsheet and use it mark cells as alive."""
    with open(filename, "rt") as map_file:
        csv_file = csv.reader(map_file)
        for y, row in enumerate(csv_file):
            for x, cell in enumerate(row):
                # If the spreadsheet element is 1 and not a space,
                # the cell should be alive.
                if cell and cell != " ":
                    grid[y][x] = int(cell)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * CELL_HEIGHT, HEIGHT * CELL_HEIGHT))
    clock = pygame.time.Clock()

    # Create a 2D map with all zero's indicating
    # all cells are dead.
    grid = create_empty_grid(WIDTH, HEIGHT)

    # If there's no map specified on the commandline,
    # load map.csv.
    map_filename = "map.csv"

    # If there's filename specified on the commandline,
    # load that file as a map.
    if len(sys.argv) > 1:
        map_filename = sys.argv[1]

    # Assume the file is a CSV file (a spreadsheet)
    # and use it to mark some cells as alive.
    read_map(grid, map_filename)

    running = True
    while running:
        # Wipe the screen
        screen.fill((250, 250, 0))
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    color = (255, 0, 0)
                else:
                    color = (0, 255, 0)
                # Draw a filled rectangle for each cell.
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x * CELL_WIDTH,
                        y * CELL_HEIGHT,
                        CELL_WIDTH,
                        CELL_HEIGHT,
                    ),
                )

        # Update all the cells of the grid
        update_grid(grid, WIDTH, HEIGHT)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)


if __name__ == "__main__":
    main()
