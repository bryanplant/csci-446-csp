class Algorithm:

    def solve(self, maze):
        pass

    def find_empty_square(self, maze):
        for row in range(maze.height):
            for col in range(maze.width):
                if maze.data[row][col] == '_':
                    return row, col
        return None

    def _get_possible_neighbors(self, row, col):
        return [row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]

    def _count_same_empty(self, maze, row, col, color):
        same = 0
        empty = 0

        for r, c in self._get_possible_neighbors(row, col):
            if maze.height > r >= 0 and maze.width > c >= 0:
                if maze.data[r][c] == color:
                    same += 1
                elif maze.data[r][c] == '_':
                    empty += 1

        return same, empty

    def _neighbor_is_valid(self, maze, row, col):
        neighbor_color = maze.data[row][col]
        if neighbor_color == '_':
            return True

        same, empty = self._count_same_empty(maze, row, col, neighbor_color)

        if (row, col) in maze.ends:
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

    def _neighbors_are_valid(self, maze, row, col):
        for r, c in self._get_possible_neighbors(row, col):
            if maze.height > r >= 0 and maze.width > c >= 0:
                if not self._neighbor_is_valid(maze, r, c):
                    return False

        color = maze.data[row][col]
        same, empty = self._count_same_empty(maze, row, col, color)

        if same == 2:
            return True
        if same > 2:
            return False

        return True

    def is_valid(self, maze, row, col):
        return self._neighbors_are_valid(maze, row, col)
