from player import Player

def test_player():
    player = Player()
    """
    Test if player can be moved and if moves can be recorded
    """

    """
    positive case
    """
    # test player moves
    player.move('w')
    assert player.row == -1 and player.col == 0, 'test player moves fail'
    
    player.move('s')
    assert player.row == 0 and player.col == 0, 'test player moves fail'
    
    player.move('d')
    assert player.row == 0 and player.col == 1, 'test player moves fail'
    
    player.move('a')
    assert player.row == 0 and player.col == 0, 'test player moves fail'
    
    assert player.moves == ['w','s','d','a'], 'test player moves fail'

    """
    negative case
    """
    try:
        player.move()
    except TypeError:
        pass
    else:
        print('Test lack argument fail')
    
    """
    edge case
    """
    player.move('e')
    assert player.moves == ['w','s','d','a', 'e'], 'test player moves fail'
    print('Test player moves success')

def run_tests():
    test_player()