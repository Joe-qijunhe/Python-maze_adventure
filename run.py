from game import Game
import os
import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: python3 run.py <filename> [play]')
    exit()

def play_mode():
    # If the mode is play, the system will clean screen automatic
    if len(sys.argv) == 3 and sys.argv[2] == 'play':
        return os.system('cls')
    else:
        return None

filename = sys.argv[1]
game = Game(filename)

while True:
    game.is_player_move = True
    
    # draw the grid and print any message
    play_mode()
    print(game.draw())
    game.message_parse()
    
    # ask for input and check if there is any special effect
    move = input('Input a move: ').lower()
    game.game_move(move)
    
    # if player is free to move, move the player
    if game.is_player_move:
        game.player.move(move)