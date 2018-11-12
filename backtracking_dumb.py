
class BacktrackingDumb:
    count = 0

    def solve(self, maze):
        # get next empty square
        rc = maze.find_empty_square()
        # if there were no empty squares, then the maze is complete
        if rc is None:
            return True

        # split into row and col
        r, c = rc
        for color in maze.colors:
            # set empty square to a value
            maze.data[r][c] = color
            self.count += 1
            # check if this color is valid
            if maze.is_valid(r, c):
                # recurse
                if self.solve(maze):
                    return True
                # set color back if maze not solved
                maze.data[r][c] = '_'
            else:
                # otherwise set color back
                maze.data[r][c] = '_'
        return False
