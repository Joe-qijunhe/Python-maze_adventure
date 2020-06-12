from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game import Game

def test_cells():
    """
    Start , End and Air cell is not tested since they do not have special effect. They can be tested in the e2e test
    Teleport is not tested as it relies on user's input. It can be test in test_game.py and e2e test.
    """
    game = Game('board_hard.txt')

    #Test step in Wall
    game.grid[0][0].step(game)
    assert game.message == '\nYou walked into a wall. Oof!\n', 'Test step in wall fail'
    assert game.is_player_move == False, 'Test step in wall fail'

    #Test step in Fire without and with water
    game.player.num_water_buckets = 0
    game.grid[6][10].step(game)
    assert game.message == 'lose', 'Test step in fire without water fail'
    
    game.player.num_water_buckets = 1
    game.grid[6][10].step(game)
    assert game.player.num_water_buckets == 0, 'Test step in fire with water fail'
    assert game.message == '\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!\n','Test step in fire with water fail'

    #Test step in water
    game.grid[3][5].step(game)
    assert game.player.num_water_buckets == 1, 'Test step in water fail'
    
    print('Test cells success')
def run_tests():
    test_cells()
