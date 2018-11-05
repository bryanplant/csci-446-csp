from tkinter import *


class Maze:
    data = []           # char values of each square
    legal_values = {}   # possible values for each square
    width = 0
    height = 0
    endpoints = {}      # represents endpoints - dictionary of (r, c) to char
    colors = set()      # possible colors

    # variables for drawing maze
    draw_shapes = []
    display = None
    display_width = 800
    display_height = None
    node_size = None

    def __init__(self, maze_file):
        # get maze data, possible colors, and color positions
        with open(maze_file, 'r') as file:
            for i, line in enumerate(file):
                line_list = list(line.strip('\n'))
                self.data.append([])
                for j, char in enumerate(line_list):
                    self.data[-1].append(char)
                    if char != '_':
                        self.endpoints[(i, j)] = char
                        self.colors.add(char)
        file.close()
        # get maze width and height
        self.width = len(self.data[0])
        self.height = len(self.data)

        # get node_size and display_height for drawing
        self.node_size = int(self.display_width / self.width)
        self.display_height = int(self.node_size * self.height)

        # initialize tkinter
        self.tk = Tk()
        self.canvas = Canvas(
            self.tk, width=self.display_width, height=self.display_height)
        self.canvas.pack()

    def preprocess(self):
        for row in range(self.height):
            for col in range(self.width):
                self.update_neighbor(row, col)

    def is_box(self, squares, color):
        for r, c in squares:
            if not (self.height > r >= 0 and self.width > c >= 0):
                return False
            if self.data[r][c] != color:
                return False
        return True

    def detect_box(self, r, c):
        color = self.data[r][c]
        # box to top left
        if self.is_box([[r, c-1], [r-1, c-1], [r-1, c]], color):
            return True
        # box to bottom left
        if self.is_box([[r, c-1], [r+1, c-1], [r+1, c]], color):
            return True
        # box to top right
        if self.is_box([[r, c+1], [r-1, c+1], [r-1, c]], color):
            return True
        # box to bottom right
        if self.is_box([[r, c+1], [r+1, c+1], [r+1, c]], color):
            return True


    def update_neighbor(self, row, col):
        if (row, col) in self.legal_values:
            del self.legal_values[(row, col)]
        if self.data[row][col] == '_':
            self.legal_values[(row, col)] = []
            for color in self.colors:
                self.data[row][col] = color
                if self.is_valid(row, col):
                    self.legal_values[(row, col)].append(color)
            self.data[row][col] = '_'

    def update_neighbors(self, row, col):
        self.update_neighbor(row, col)
        for r, c in self._get_valid_neighbors(row, col):
            self.update_neighbor(r, c)

    def get_most_constrained(self):
        min_colors = len(self.colors) + 1
        min_rc = None
        for rc, colors in self.legal_values.items():
            if min_colors > len(colors):
                min_colors = len(colors)
                min_rc = rc
        return min_rc

    # iterate through all squares and find first empty
    def find_empty_square(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] == '_':
                    return row, col
        return None

    # return the row and col of all neighbors around given row and col
    def _get_valid_neighbors(self, row, col):
        neighbors = [row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]
        valid = []
        for r, c in neighbors:
            if self.height > r >= 0 and self.width > c >= 0:
                valid.append([r, c])
        return valid

    # count the number of empty and same-colored squares around given square
    def _count_same_empty(self, row, col, color):
        same = 0
        empty = 0

        for r, c in self._get_valid_neighbors(row, col):
            if self.data[r][c] == color:
                same += 1
            elif self.data[r][c] == '_':
                empty += 1

        return same, empty

    # return if the neighbor meets constraints
    def _neighbor_is_valid(self, row, col):
        neighbor_color = self.data[row][col]
        # valid if square is empty
        if neighbor_color == '_':
            return True

        # get number of neighbors that are the same color and number that are empty
        same, empty = self._count_same_empty(row, col, neighbor_color)

        # if square is an endpoint
        if (row, col) in self.endpoints:
            # endpoint must have one or more neighbors with the same color
            if same >= 1:
                return True
            if empty == 0:
                return False
        else:
            # non-endpoint must have 2 or less neighbors with the same color
            # if it does not have two, it must have enough empty neighbors
            if same == 2:
                return True
            if same > 2:
                return False
            if empty < 2 - same:
                return False

        return True

    # return if maze is valid with new addition
    def is_valid(self, row, col):
        color = self.data[row][col]
        same, empty = self._count_same_empty(row, col, color)
        # check if new square has valid number of surrounding colors
        if same > 2:
            return False
        if 2 - same > empty:
            return False

        if self.detect_box(row, col):
            return False

        # iterate through neighbors and check for validity
        for r, c in self._get_valid_neighbors(row, col):
            if not self._neighbor_is_valid(r, c):
                return False


        return True

    @staticmethod
    def get_color(char):
        if char == 'B':
            return "blue"
        # Amaranth
        elif char == 'A':
            return "#E52B50"
        elif char == 'W':
            return "white"
        elif char == 'R':
            return "red"
        elif char == 'P':
            return "#ff69b4"
        # Dark moderate magenta
        elif char == 'D':
            return "#9f55ac"
        elif char == 'O':
            return "#ff7f00"
        elif char == 'G':
            return "green"
        elif char == 'Y':
            return "yellow"
        # Kenyan copper
        elif char == 'K':
            return "#7c1c05"
        # Queen blue
        elif char == 'Q':
            return "#436b95"
        else:
            return "white"

    # draw the maze
    def draw(self):
        self.canvas.delete('all')
        for row in range(self.height):
            for col in range(self.width):
                self.canvas.create_rectangle(
                    col * self.node_size,
                    row * self.node_size,
                    col * self.node_size + self.node_size,
                    row * self.node_size + self.node_size,
                    fill="#696969"
                )

                if self.data[row][col] != '_' and (row, col) not in self.endpoints:
                    self._create_circle(
                        col*self.node_size + self.node_size/2,
                        row*self.node_size + self.node_size/2,
                        self.node_size/5,
                        fill=self.get_color(self.data[row][col])
                    )

        for node, char in self.endpoints.items():
            color = self.get_color(char)

            self.canvas.create_oval(
                node[1] * self.node_size + self.node_size * .1,
                node[0] * self.node_size + self.node_size * .1,
                node[1] * self.node_size + self.node_size * .9,
                node[0] * self.node_size + self.node_size * .9,
                fill=color
            )
        self.tk.update()

    # create a tkinter circle with x, y and radius
    def _create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)
