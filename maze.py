from tkinter import *


class Maze:
    data = []
    width = 0
    height = 0
    ends = {}
    colors = set()

    # variables for drawing maze
    draw_shapes = []
    display = None
    display_width = 800
    display_height = None
    node_size = None

    def __init__(self, maze_file):
        # get maze data and color positions
        with open(maze_file, 'r') as file:
            for i, line in enumerate(file):
                line_list = list(line.strip('\n'))
                self.data.append([])
                for j, char in enumerate(line_list):
                    self.data[-1].append(char)
                    if char != '_':
                        self.ends[(i, j)] = char
                        self.colors.add(char)
        file.close()
        # get maze width and height
        self.width = len(self.data[0])
        self.height = len(self.data)

        self.node_size = int(self.display_width / self.width)
        self.display_height = int(self.node_size * self.height)

        # initialize tkinter
        self.tk = Tk()
        self.canvas = Canvas(
            self.tk, width=self.display_width, height=self.display_height)
        self.canvas.pack()
        self.draw()

    def find_empty_square(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] == '_':
                    return row, col
        return None

    def _get_possible_neighbors(self, row, col):
        return [row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]

    def _count_same_empty(self, row, col, color):
        same = 0
        empty = 0

        for r, c in self._get_possible_neighbors(row, col):
            if self.height > r >= 0 and self.width > c >= 0:
                if self.data[r][c] == color:
                    same += 1
                elif self.data[r][c] == '_':
                    empty += 1

        return same, empty

    def _neighbor_is_valid(self, row, col):
        neighbor_color = self.data[row][col]
        if neighbor_color == '_':
            return True

        same, empty = self._count_same_empty(row, col, neighbor_color)

        if (row, col) in self.ends:
            if same >= 1:
                return True
            if empty == 0:
                return False
        else:
            if same == 2:
                return True
            if same > 2:
                return False
            if empty < 2 - same:
                return False

        return True

    def _neighbors_are_valid(self, row, col):
        for r, c in self._get_possible_neighbors(row, col):
            if self.height > r >= 0 and self.width > c >= 0:
                if not self._neighbor_is_valid(r, c):
                    return False

        color = self.data[row][col]
        same, empty = self._count_same_empty(row, col, color)

        if same == 2:
            return True
        if same > 2:
            return False

        return True

    def is_valid(self, row, col):
        return self._neighbors_are_valid(row, col)

    def get_color(self, char):
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

                if self.data[row][col] != '_' and (row, col) not in self.ends:
                    self._create_circle(
                        col*self.node_size + self.node_size/2,
                        row*self.node_size + self.node_size/2,
                        self.node_size/5,
                        fill=self.get_color(self.data[row][col])
                    )

        for node, char in self.ends.items():
            color = self.get_color(char)

            self.canvas.create_oval(
                node[1] * self.node_size + self.node_size * .1,
                node[0] * self.node_size + self.node_size * .1,
                node[1] * self.node_size + self.node_size * .9,
                node[0] * self.node_size + self.node_size * .9,
                fill=color
            )
        self.tk.update()

    def _create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)
