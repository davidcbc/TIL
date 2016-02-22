import sys
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Maze:
    def __init__(self, maze):
        self.OPEN_COLOR = (255, 255, 255)
        self.CLOSED_COLOR = (0, 0, 0)
        self.CHECKED_COLOR = (0, 255, 0)
        self.PATH_COLOR = (255, 0, 0)
        self.START_COLOR = (0, 255, 0)
        self.END_COLOR = (255, 0, 0)

        # Load image.
        self.file_in = maze
        self.image = Image.open(self.file_in)
        self.image = self.image.convert('RGB')
        self.pixels = self.image.load()
        self.solution_image = self.image.copy()
        self.solution_pixels = self.solution_image.load()
        self._determine_start_and_finish()
        self._clean_image()
        self.current_position = self.START_POSITION
        logging.info("Loaded image '{0}' ({1} pixels).".format(self.file_in, self.image.size))

    def move(self, direction):
        x, y = self.current_position
        if direction == "n":
            if self.is_open(x, y - 1) is True:
                self.current_position = (x, y - 1)
                self._mark_path(x, y - 1)
                return True
            return False
        if direction == "s":
            if self.is_open(x, y + 1) is True:
                self.current_position = (x, y + 1)
                self._mark_path(x, y + 1)
                return True
            return False
        if direction == "e":
            if self.is_open(x + 1, y) is True:
                self.current_position = (x + 1, y)
                self._mark_path(x + 1, y)
                return True
            return False
        if direction == "w":
            if self.is_open(x - 1, y) is True:
                self.current_position = (x - 1, y)
                self._mark_path(x - 1, y)
                return True
            return False
        return False

    def mark_checked(self, x, y):
        self.solution_pixels[x, y] = self.CHECKED_COLOR

    def print_solution(self):
        logging.info("In here!")
        self.solution_image.save("out/{0}".format(self.file_in))
        logging.info("Image saved: out/{0}".format(self.file_in))

    def _mark_path(self, x, y):
        self.solution_pixels[x, y] = self.PATH_COLOR

    def _determine_start_and_finish(self):
        x, y = self.image.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                if (r, g, b) == self.END_COLOR:
                    self.pixels[i, j] = (255, 255, 255)
                    self.END_POSITION = (i, j)
                elif (r, g, b) == self.START_COLOR:
                    self.pixels[i, j] = (255, 255, 255)
                    self.START_POSITION = (i, j)

    def _clean_image(self):
        th = 256 / 2
        x, y = self.image.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                if r > th and g > th and b > th:
                    self.pixels[i, j] = self.OPEN_COLOR
                else:
                    self.pixels[i, j] = self.CLOSED_COLOR

    def is_open(self, x, y):
        border_x, border_y = self.image.size
        if x < 0 or y < 0 or x >= border_x or y >= border_y:
            return False
        return self.pixels[x, y] == self.OPEN_COLOR

    def is_end(self, x, y):
        return True if (x, y) == self.END_POSITION else False

    def at_end(self):
        return True if self.current_position == self.END_POSITION else False

    def to_string(self):
        x, y = self.image.size
        for i in range(0, x):
            this_line = ""
            for j in range(0, y):
                if self.is_open(i, j):
                    this_line += " "
                else:
                    this_line += "X"
            print this_line


if __name__ == '__main__':
    solver = Maze(sys.argv[1])
