import colors
import pygame

# note: self.x max is the maximum number of rows
# while self.y max is maximum number of colums


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.neighbours = []
        self.x = row * width
        # position of x adjusted to scale
        self.y = col * width
        # position of y adjusted to scale
        self.color = colors.WHITE

    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return self.__str__()

    def get_pos(self):
        return self.row, self.col

    def __lt__(self, other):
        x1, y1 = self.get_pos()
        x2, y2 = other.get_pos()
        diff = (x1 - x2) + (y1 - y2)
        if diff > 0:
            return True
        return False

    def is_obstacule(self):
        return bool(self.color == colors.GREY)

    def reset(self):
        self.color = colors.WHITE

    def is_visited(self):
        return bool(self.color == colors.BLUE)

    def make_visited(self):
        self.color = colors.BLUE

    def make_possible_path(self):
        self.color = colors.GREEN

    def make_start(self):
        self.color = colors.ORANGE

    def make_end(self):
        self.color = colors.TURQUOISE

    def make_path(self):
        self.color = colors.PURPLE

    def make_obstacule(self):
        self.color = colors.GREY

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def get_neighbours(self, grid):
        # total_row == total_col because of a square based grid
        # right_neighbour = grid[self.row + 1][self.col]
        # left_neighbour = grid[self.row - 1][self.col]
        # top_neighbour = grid[self.row][self.col - 1]
        # buttom_neighbour = grid[self.row][self.col + 1]
        # example
        # grid = [
        # [0,0], [0,1], [0,2], [0,3], [0,4] - row 0
        # [1,0], [1,1], [1,2], [1,3], [1,4] - row 1
        # [2,0], [2,1], [2,2], [2,3], [2,4] - row 2
        # ]
        # let self.row = 1 and self.col = 2
        # rows go from 0 - (max_row -1)
        # check right -> left-> up  for neighbours i.e nodes that are not obstacles
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].is_obstacule()
        ):  # right_neighbour
            # if the current row i'm on is not the last,
            # check if next row is obstacle
            # if false, add this to my neighbours
            # right_neighbour = [2,2]
            self.neighbours.append(grid[self.row + 1][self.col])

        if (
            self.row > 0 and not grid[self.row - 1][self.col].is_obstacule()
        ):  # left_neighbour
            # check if previous row is obstacle
            # left_neighbour = [0,2]
            self.neighbours.append(grid[self.row - 1][self.col])

        if (
            self.col > 0 and not grid[self.row][self.col - 1].is_obstacule()
        ):  # top_neighbour
            # top_neighbour = [1,1]
            self.neighbours.append(grid[self.row][self.col - 1])

        if (
            self.col < self.total_rows - 1 and grid[self.row][self.col + 1]
        ):  # buttom_neighbour
            # buttom_neighbour = [1,3]
            self.neighbours.append(grid[self.row][self.col + 1])

        return self.neighbours

