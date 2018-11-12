from backtracking_dumb import BacktrackingDumb
from backtracking_smart import BacktrackingSmart
from maze import Maze

import time
import sys


class Main:
    maze = None
    algorithm = None

    def run(self):
        # get maze and algorithm selection from user
        self.algorithm = self.get_algorithm()
        self.maze = self.get_maze()

        # draw initial setup
        self.maze.draw()

        # store start time
        start = time.time()
        # run selected algorithm on selected maze
        self.algorithm.solve(self.maze)

        # print how long algorithm took
        print("Elapsed:", time.time() - start)
        print("Assigned:", self.algorithm.count)
        # draw solution
        self.maze.draw()

        # wait until user presses a key to end
        input("Press Enter to close...")

    @staticmethod
    def get_maze():
        return Maze(sys.argv[2])

    @staticmethod
    def get_algorithm():
        try:
            selection = int(sys.argv[1])
        except:
            print('invalid algorithm choice!')
            print("\t1. Dumb Backtracking")
            print("\t2. Smart Backtracking")
            sys.exit(1)

        if selection == 1:
            return BacktrackingDumb()
        elif selection == 2:
            return BacktrackingSmart()


main = Main()
main.run()
