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

def test_move_north():
    testMaze = Maze("maze0.png")
    assert testMaze.move('n')

def test_move_south():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (1,47)
    assert testMaze.move('s')

def test_move_east():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (6,47)
    assert testMaze.move('e')

def test_move_west():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (6,47)
    assert testMaze.move('w')

def test_move_north_fail():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (0,49)
    assert not testMaze.move('n')

def test_move_south_fail():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (0,48)
    assert not testMaze.move('s')

def test_move_east_fail():
    testMaze = Maze("maze0.png")
    assert not testMaze.move('e')

def test_move_west_fail():
    testMaze = Maze("maze0.png")
    assert not testMaze.move('w')

def test_move_north_fail_border():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (49,49)
    assert not testMaze.move('n')

def test_move_south_fail_border():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (0,0)
    assert not testMaze.move('s')

def test_move_east_fail_border():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (49,49)
    assert not testMaze.move('e')

def test_move_west_fail_border():
    testMaze = Maze("maze0.png")
    testMaze.current_position = (0,0)
    assert not testMaze.move('w')