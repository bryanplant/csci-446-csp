from collections import defaultdict
from tkinter import *

class Maze:
    data = []
    width = 0
    height = 0
    colors = defaultdict(list)

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
                        self.colors[char].append((i, j))
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
        for i in range(self.height):
            for j in range(self.width):
                self.canvas.create_rectangle(
                    i * self.node_size,
                    j * self.node_size,
                    i * self.node_size + self.node_size,
                    j * self.node_size + self.node_size,
                    fill="#696969"
                )

        for k, v in self.colors.items():
            color = self.get_color(k)

            for node in v:
                self.canvas.create_oval(
                    node[1] * self.node_size + self.node_size * .1,
                    node[0] * self.node_size + self.node_size * .1,
                    node[1] * self.node_size + self.node_size * .9,
                    node[0] * self.node_size + self.node_size * .9,
                    fill=color
                )
        self.tk.update()

        # color = None
        # for i, line in enumerate(self.data):
        #     for j, char in enumerate(line):
        #         if char == ' ':
        #             if [i, j] in path:
        #                 color = "green"
        #             elif [i, j] in visited:
        #                 color = "blue"
        #             else:
        #                 color = "white"
        #         elif char == '%':
        #             color = "black"
        #         elif char == 'P':
        #             color = "red"
        #         elif char == '*':
        #             color = "yellow"
        #
        #         if color != self.canvas.itemcget(self.squares[i][j], "fill"):
        #             self.canvas.itemconfig(self.squares[i][j], fill=color)
        # self.tk.update()

