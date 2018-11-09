
class BacktrackingSmart:

    def solve(self, maze):
        maze.preprocess()
        # get most constrained square to populate
        rc = maze.get_most_constrained()
        if rc is None:
            return True

        # split into row and col
        r, c = rc
        for color in maze.order_colors(r, c):
            # set empty square to a value
            maze.data[r][c] = color
            maze.draw()

            # recurse
            if self.solve(maze):
                return True
            # set color back if maze not solved
            maze.data[r][c] = '_'

        return False
