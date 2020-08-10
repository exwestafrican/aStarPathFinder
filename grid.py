from node import Node
import pygame
import colors
from path_finder import path_finder_algo

WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def make_grid(full_lenght, total_num_of_rows):
    grid = []
    width = full_lenght // total_num_of_rows
    # print(width)
    # gives width of a node

    for row in range(total_num_of_rows):
        # make a list of points [(x,y)]
        grid.append([])
        for col in range(total_num_of_rows):
            node = Node(row, col, width, total_num_of_rows)
            # i.e [ (0,0, 0,1),(1,0, 1,1)]
            # i.e [ (i,j, i,j++),(i++,j++, i++,j++)]
            # node adjused for width [ (i*width , j*width)]
            grid[row].append(node)

    # print(grid)
    return grid


def draw_grid_lines(win, full_lenght, total_num_of_rows):
    gap = full_lenght // total_num_of_rows
    for i in range(total_num_of_rows):
        # for horizontal line
        pygame.draw.line(
            win, colors.GREY, (0, i * gap), (full_lenght, i * gap),
        )
        # hint x2 - x1 lenght of horizontal line

        # for vertical lines
        pygame.draw.line(
            win, colors.GREY, (i * gap, 0), (i * gap, full_lenght),
        )
        # in y2 - y1 = full_lenght
    # i.e (0,current_point_on_y_axis ) and
    # (last_point_on_x_axis ,current_point_on_y_axis )


def draw_grid_window(win, grid, full_lenght, total_num_of_rows):
    for rows in grid:
        for nodes in rows:
            # draw each node in array
            nodes.draw(win)
    # DRAW GRID LINES
    draw_grid_lines(win, full_lenght, total_num_of_rows)
    pygame.display.update()


# e.g
# make_grid(8, 4)
# [[0-0, 0-2, 0-4, 0-6], [2-0, 2-2, 2-4, 2-6],
# [4-0, 4-2, 4-4, 4-6], [6-0, 6-2, 6-4, 6-6]]


def get_position_on_click(position, grid, full_lenght, total_num_of_rows):
    """
    get mouse position on click 
    and converts it to scale
    """
    gap = full_lenght // total_num_of_rows
    # space between two points

    x, y = position
    row = x // gap
    col = y // gap
    # convert to current scale used
    # for window

    node = grid[row][col]
    return node


def main(win, full_lenght):
    ROWS = 50

    grid = make_grid(full_lenght, total_num_of_rows=ROWS)
    start = None
    end = None

    running = True
    while running:
        draw_grid_window(win, grid, full_lenght, total_num_of_rows=ROWS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # if user hits space bar after setting start and end node
                if event.key == pygame.K_SPACE and start and end:
                    draw = lambda: draw_grid_window(win, grid, ROWS, full_lenght)
                    path_finder_algo(draw,start,end,grid)


        if pygame.mouse.get_pressed()[0]:  # left click
            pos = pygame.mouse.get_pos()
            # print("mouse pos", pos)
            node = get_position_on_click(pos, grid, full_lenght, ROWS)
            if start is None and node != end:
                # on the first click, make spot start
                # if not spot is start,
                # make this spot the start
                start = node
                start.make_start()
            elif end is None and node != start:
                # if no spot is the end and
                # the current spot is not a start
                # then make it an end
                end = node
                end.make_end()
            elif node != start and node != end:
                # if spot is not start or stop,
                # then it can be an obstacle
                node.make_obstacule()

        if pygame.mouse.get_pressed()[2]:  # right click
            pos = pygame.mouse.get_pos()
            node = get_position_on_click(pos, grid, full_lenght, ROWS)
            if node == start:
                start = None
            elif node == end:
                end = None
            node.reset()

        

    pygame.quit()


main(WIN, WIDTH)

