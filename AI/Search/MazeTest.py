from Maze import Maze


def test_maze_creation_clean():
    testMaze = Maze("testmaze.png")
    assert testMaze.pixels[0,1] == (0,0,0)
    assert testMaze.pixels[0,0] == (255,255,255)
    assert testMaze.pixels[1,0] == (255,255,255)
    assert testMaze.pixels[1,1] == (255,255,255)

def test_maze_start_position():
    testMaze = Maze("testmaze.png")
    assert testMaze.START_POSITION == (0,0)

def test_maze_end_position():
    testMaze = Maze("testmaze.png")
    assert testMaze.END_POSITION == (1,1)

def test_maze_is_open_true():
    testMaze = Maze("testmaze.png")
    assert testMaze.is_open(0,0)

def test_maze_is_open_false():
    testMaze = Maze("testmaze.png")
    assert testMaze.is_open(0,1) is False