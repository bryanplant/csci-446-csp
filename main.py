from backtracking_dumb import BacktrackingDumb
from backtracking_smart import BacktrackingSmart
from maze import Maze

import time


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
        # draw solution
        self.maze.draw()

        # wait until user presses a key to end
        input("Press Enter to close...")

    @staticmethod
    def get_maze():
        print("Choose a maze")
        print("\t1. 5x5")
        print("\t2. 7x7")
        print("\t3. 8x8")
        print("\t4. 9x9")
        print("\t5. 10x10")
        print("\t6. 12x12")
        print("\t7. 14x14")
        selection = int(input())

        if selection == 1:
            return Maze('mazes/5x5maze.txt')
        elif selection == 2:
            return Maze('mazes/7x7maze.txt')
        elif selection == 3:
            return Maze('mazes/8x8maze.txt')
        elif selection == 4:
            return Maze('mazes/9x9maze.txt')
        elif selection == 5:
            return Maze('mazes/10x10maze.txt')
        elif selection == 6:
            return Maze('mazes/12x12maze.txt')
        elif selection == 7:
            return Maze('mazes/14x14maze.txt')

    @staticmethod
    def get_algorithm():
        print("Choose a search algorithm")
        print("\t1. Dumb Backtracking")
        print("\t2. Smart Backtracking")
        selection = int(input())

        if selection == 1:
            return BacktrackingDumb()
        elif selection == 2:
            return BacktrackingSmart()


main = Main()
main.run()
