from algorithm import Algorithm


class BacktrackingSmart(Algorithm):

    def solve(self, maze):
        maze.preprocess()
        self.solve_recursive(maze)

    def solve_recursive(self, maze):
        maze.preprocess()
        # get most constrained square to populate
        rc = maze.get_most_constrained()
        if rc is None:
            return True

        # split into row and col
        r, c = rc
        for color in maze.legal_values[(r, c)]:
            # set empty square to a value
            maze.data[r][c] = color
            # maze.draw()

            # recurse
            if self.solve_recursive(maze):
                return True
            # set color back if maze not solved
            maze.data[r][c] = '_'

        return False
