from Maze import Maze
import sys
import logging


class DFSSolver:
    def __init__(self,maze):
        self.maze = Maze(maze)
        self.current_position = self.maze.current_position
        self.visited_positions = {self.current_position}
        self.position_stack = [self.current_position]

    def solve(self):
        x,y = self.current_position
        while(not self.maze.is_end(x,y)):
            self.maze.mark_checked(x,y)
            self.visited_positions.add((x,y))
            if (x,y+1) not in self.visited_positions and self.maze.is_open(x,y+1):
                self.position_stack.append((x,y+1))
                y += 1
            elif (x,y-1) not in self.visited_positions and self.maze.is_open(x,y-1):
                self.position_stack.append((x,y-1))
                y -= 1
            elif (x+1,y) not in self.visited_positions and self.maze.is_open(x+1,y):
                self.position_stack.append((x+1,y))
                x += 1
            elif (x-1,y) not in self.visited_positions and self.maze.is_open(x-1,y):
                self.position_stack.append((x-1,y))
                x -= 1
            else:
                prevX, prevY = self.position_stack.pop()
                x,y = self.position_stack[len(self.position_stack)-1]
        prevX, prevY = self.current_position
        for (solX, solY) in self.position_stack:
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
            logging.info("Solved in " + str(len(self.position_stack)) + " moves!")
            self.maze.print_solution()
        else:
            logging.error("Failed! End position: " + str(self.maze.END_POSITION) + " Current position: "  + str(self.maze.current_position))

if __name__ == '__main__':
    solver = DFSSolver(sys.argv[1])
    solver.solve()