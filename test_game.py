from game import Game


def test_game():
    game = Game('board_hard.txt')
    test_player(game)
    test_find(game)
    test_in_bound(game)
    test_game_move(game)

def run_tests():
    test_game()

def test_player(game):
    """
    Test if the player is in the Start
    """
    
    assert game.player.row == 0 and game.player.col == 1, 'Player position is wrong'
    print('Test player position success')

def test_find(game):
    """
    Test if find function returns the right row and col of the cell
    """
    
    """
    positive case: find corresponding teleport
    """
    assert game.find('2', 1, 8) == [5,3], 'find teleport fail'
    assert game.find('1',7,2) == [3,10], 'find teleport fail'
    
    """
    edge case: find start with current row and col -1
    """
    assert game.find('X', -1, -1) == [0,1], 'find start position fail'
    
    """
    negative case
    """
    #find some invalid cell, it shoud raise ValueError
    try:
        game.find('J', 0, 0)
    except ValueError as e:
        assert str(e) == 'Please enter a valid display' , 'test an invalid cell fail'
    #lack one argument, it should raise TypeError
    try:
        game.find(0, 0)
    except TypeError:
        pass
    else:
        print('lack one argument fail')
    
    print('Test find function success')


def test_in_bound(game):
    """
    Test a in bound point, if returns true ,the in_bound function works
    Test a out bound point, if returns false, the in_bound function works
    """
    
    """
    positive case: in bound point should return True and out bound return False
    """
    assert game.in_bound(1,1) == True, 'Test in_bound function in bound point fail'
    assert game.in_bound(-1,0) == False, 'Test in_bound function out bound point fail'
    assert game.in_bound(0,-1) == False, 'Test in_bound function out bound point fail'
    assert game.in_bound(0,15) ==  False, 'Test in_bound function out bound point fail'
    
    """
    edge case: point on the bound should returns True
    """
    assert game.in_bound(0,0) == True, 'Test in_bound function bound point fail'
    assert game.in_bound(8,14) == True, 'Test in_bound function bound point fail'
    
    """
    negative case
    """
    #lack argument should raise Type
    try:
        game.in_bound('hello','joe')
    except ValueError as e:
        assert str(e) == 'Please enter an integer row and col', 'Test in_bound function negative case fail'
    #non integer should raise ValueError
    try:
        game.in_bound(0)
    except TypeError:
        pass
    else:
        print('lack one argument fail')
    
    print('Test in_bound function success')

def test_game_move(game):
    """
    Test game_move function can trigger the cell's effect by testing the game message
    """
    
    """
    positive case
    """
    #Test player move out of bound
    game.game_move('w')
    assert game.message == '\nYou walked into a wall. Oof!\n', 'test player move out of bound fail'

    #Test player move into fire when player have no water
    game.player.row, game.player.col = 6, 11
    game.game_move('a')
    assert game.message == 'lose', 'test player move into fire when player have no water fail'
    
    #Test player move into water cell
    game.player.row, game.player.col = 3, 4
    game.game_move('d')
    assert game.player.num_water_buckets == 1, 'test player move into water cell fail'
    
    #Test player in teleport
    game.player.row, game.player.col = 1, 8
    game.game_move('e')
    assert game.player.row == 5 and game.player.col == 3, 'game_move function fail'
    assert game.message == '\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n', 'test player in teleport fail'

    """
    negative case
    """
    #Test user's invalid input
    game.game_move('j')
    assert game.message == '\nPlease enter a valid move (w, a, s, d, e, q).\n', 'Test user\'s invalid input fail'
    assert game.is_player_move == False, 'Test user\'s invalid input fail'


    game.game_move('')
    assert game.message == '\nPlease enter a valid move (w, a, s, d, e, q).\n', 'Test user\'s invalid input fail'
    assert game.is_player_move == False, 'Test user\'s invalid input fail'

    try:
        game.game_move()
    except TypeError:
        pass
    else:
        print('lack one argument fail')
    
    print('Test game_move function success')

    """
    message_parse function is not test because it is simple and just print out game's message.
    """