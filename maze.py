from collections import defaultdict
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
                    self.canvas.create_oval(
                        col * self.node_size + self.node_size * .3,
                        row * self.node_size + self.node_size * .3,
                        col * self.node_size + self.node_size * .7,
                        row * self.node_size + self.node_size * .7,
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
