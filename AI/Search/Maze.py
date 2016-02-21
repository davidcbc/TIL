import sys
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Maze:
    def __init__(self, maze):
        self.OPEN_COLOR = (255, 255, 255)
        self.CLOSED_COLOR = (0, 0, 0)
        self.START_COLOR = (0, 255, 0)
        self.END_COLOR = (255, 0, 0)

        # Load image.
        self.image = Image.open(self.file_in)
        self.image = self.image.convert('RGB')
        self.pixels = self.image.load()
        self._determine_start_and_finish()
        self._clean_image()

        logging.info("Loaded image '{0}' ({1} pixels).".format(self.file_in, self.image.size))

    def _determine_start_and_finish(self):
        x, y = self.image.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                if (r, g, b) == self.END_COLOR:
                    self.pixels[i,j] = (255,255,255)
                    self.END_POSITION = (i, j)
                elif (r, g, b) == self.START_COLOR:
                    self.pixels[i,j] = (255,255,255)
                    self.START_POSITION = (i, j)

    def _clean_image(self):
        th = 256/2
        x,y = self.image.size
        for i in range(x):
            for j in range(y):
                r,g,b = self.pixels[i,j]
                if r > th and g > th and b > th:
                    self.pixels[i,j] = self.OPEN_COLOR
                else:
                    self.pixels[i,j] = self.CLOSED_COLOR


    def is_open(self, x, y):
        return True if self.pixels[x,y] == self.OPEN_COLOR else False

    def is_end(self, x, y):
        logging.info("X, Y: " + str(x) + ", " + str(y))
        logging.info("END: " + str(self.END_POSITION))
        return True if (x,y) == self.END_POSITION else False

    def to_string(self):
        x,y = self.image.size
        for i in range(0, x):
            thisLine = ""
            for j in range(0, y):
                if self.is_open(i,j):
                    thisLine = thisLine + " "
                else:
                    thisLine = thisLine + "X"
            print thisLine


if __name__ == '__main__':
    solver = Maze(sys.argv[1])
