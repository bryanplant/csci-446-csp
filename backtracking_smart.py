import keyboard


class BacktrackingSmart:
    count = 0

    def solve(self, maze):
        maze.preprocess()
        self.solve_recursive(maze)

    def solve_recursive(self, maze):

        # get most constrained square to populate
        rc = maze.get_most_constrained()
        if rc is None:
            return True

        # split into row and col
        r, c = rc
        for color in maze.order_colors(r, c):
            # set empty square to a value
            maze.data[r][c] = color
            self.count += 1
            maze.update_neighbors(r, c)
            if keyboard.is_pressed('d'):
                maze.draw()

            # recurse
            if self.solve_recursive(maze):
                return True

            # set color back if maze not solved
            maze.data[r][c] = '_'
            maze.update_neighbors(r, c)

        return False
