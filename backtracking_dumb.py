from algorithm import Algorithm


class BacktrackingDumb(Algorithm):

    def solve(self, maze):
        rc = maze.find_empty_square()
        if rc is None:
            return True

        r, c = rc
        for color in maze.colors:
            maze.data[r][c] = color
            if maze.is_valid(r, c):
                if self.solve(maze):
                    return True
                maze.data[r][c] = '_'
            else:
                maze.data[r][c] = '_'
        return False
