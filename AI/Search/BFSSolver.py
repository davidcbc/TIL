from Maze import Maze
from collections import deque
import sys
import logging


class BFSSolver:
    def __init__(self,maze):
        self.maze = Maze(maze)
        self.current_position = self.maze.current_position
        self.visited_positions = {self.current_position}
        self.path_queue = deque()

    def solve(self):
        x,y = self.current_position
        self.visited_positions.add((x,y))
        path = [self.current_position]
        while not self.maze.is_end(x,y):
            self.maze.mark_checked(x,y)
            if (x,y+1) not in self.visited_positions and self.maze.is_open(x,y+1):
                self.visited_positions.add((x, y + 1))
                new_path = list(path)
                new_path.append((x, y + 1))
                self.path_queue.append(new_path)
            if (x,y-1) not in self.visited_positions and self.maze.is_open(x,y-1):
                self.visited_positions.add((x, y - 1))
                new_path = list(path)
                new_path.append((x, y - 1))
                self.path_queue.append(new_path)
            if (x+1,y) not in self.visited_positions and self.maze.is_open(x+1,y):
                self.visited_positions.add((x + 1, y))
                new_path = list(path)
                new_path.append((x + 1, y))
                self.path_queue.append(new_path)
            if (x-1,y) not in self.visited_positions and self.maze.is_open(x-1,y):
                self.visited_positions.add((x - 1, y))
                new_path = list(path)
                new_path.append((x - 1, y))
                self.path_queue.append(new_path)
            path = self.path_queue.popleft()
            x,y = path[len(path)-1]

        prevX, prevY = self.current_position
        for (solX, solY) in path:
            if solY > prevY:
                if not self.maze.move('s'):
                    logging.error("Failed move south")
            if solY < prevY:
                if not self.maze.move('n'):
                    logging.error("Failed move north")
            if solX > prevX:
                if not self.maze.move('e'):
                    logging.error("Failed move east")
            if solX < prevX:
                if not self.maze.move('w'):
                    logging.error("Failed move west")
            prevX = solX
            prevY = solY
        if self.maze.at_end():
            logging.info("Solved in " + str(len(path)) + " moves!")
            self.maze.print_solution()
        else:
            logging.error("Failed! End position: " + str(self.maze.END_POSITION) + " Current position: "  + str(self.maze.current_position))


if __name__ == '__main__':
    solver = BFSSolver(sys.argv[1])
    solver.solve()