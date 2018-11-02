from algorithm import Algorithm


class BacktrackingDumb(Algorithm):

    def solve(self, maze):
        rc = self.find_empty_square(maze)
        if rc is None:
            return True

        r, c = rc
        for color in maze.colors:
            maze.data[r][c] = color
            if self.is_valid(maze, r, c):
                if self.solve(maze):
                    return True
                maze.data[r][c] = '_'
            else:
                maze.data[r][c] = '_'


        return False
