from grid import grid_to_string
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player

def test_grid():
    player = Player()
    
    """
    positive cases
    """
    # Test print simple grid
    grid = [[Start(),Air(),Wall()],[Wall(),End(),Air()]]
    expect = 'A *\n*Y \n\nYou have 0 water buckets.'
    assert grid_to_string(grid,player) == expect, 'test simple grid fail'

    #Test print grid contains fire and water
    grid = [[Start(), Wall(), Wall()],[Air(),Water(), Fire()], [Wall(),End(),Wall()]]
    expect = 'A**\n WF\n*Y*\n\nYou have 0 water buckets.'
    assert grid_to_string(grid,player) == expect, 'test fire and water grid fail'

    #Test print grid contains teleport
    grid = [[Start(), Air(), Wall()],[Air(), Teleport('1'), Teleport('1')], [Wall(),End(),Wall()]]
    expect = 'A *\n 11\n*Y*\n\nYou have 0 water buckets.'
    assert grid_to_string(grid,player) == expect, 'test teleport grid fail'

    #Test print hard grid that have all kind of cell
    grid = [[Start(), Air(), Air(), Wall(),Wall()],[Air(), Water(), Fire(),Teleport('1'), Teleport('1')], [Wall(),End(),Wall(),Wall(),Wall()]]
    expect = 'A  **\n WF11\n*Y***\n\nYou have 0 water buckets.'
    assert grid_to_string(grid,player) == expect, 'test hard grid with all kind of cell fail'

    #Test print player have one water
    player.num_water_buckets = 1
    grid = [[Start(), Air(), Air(), Wall(),Wall()],[Air(), Water(), Fire(),Teleport('1'), Teleport('1')], [Wall(),End(),Wall(),Wall(),Wall()]]
    expect = 'A  **\n WF11\n*Y***\n\nYou have 1 water bucket.'
    assert grid_to_string(grid,player) == expect, 'Test player have one water fail'

    #Test print player have 2 water
    player.num_water_buckets = 2
    grid = [[Start(), Air(), Air(), Wall(),Wall()],[Air(), Water(), Fire(),Teleport('1'), Teleport('1')], [Wall(),End(),Wall(),Wall(),Wall()]]
    expect = 'A  **\n WF11\n*Y***\n\nYou have 2 water buckets.'
    assert grid_to_string(grid,player) == expect, 'Test player have more than one water fail'
    
    """
    negative case
    """
    #Test input a one dimension grid
    try:
        grid = [Wall(),Start(),Wall()]
        grid_to_string(grid,player)
    except TypeError:
        pass
    else:
        print('one dimension grid fail')
    
    """
    edge casae: test grid is a one dimension list
    """
    grid = []
    assert grid_to_string(grid,player) == '\nYou have 2 water buckets.' , 'Test edge case fail'
    
    print('Test grid success')

def run_tests():
    test_grid()