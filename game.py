from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    Wall,
    Teleport
)

class Game:
    player = Player()

    def __init__(self, filename):
        """
        Arguments:
        filename -- the name of board  going to play

        Instance variable:
        grid -- returns a two dimension list of cells
        next_row, next_col -- the player's next position in the grid
        start.row, start.col -- the start position of the game
        player.row, player.col -- set the player to the start
        message : store any messages from the game
        is_player_move : controlling whether to move the player's position. If True, the player can move one step. If Flase, the player cannot move one step.
        """
        self.grid = read_lines(filename)
        self.next_row , self.next_col = 0 , 0
        self.start_row, self.start_col = self.find('X', -1, -1)
        self.player.row, self.player.col = self.start_row, self.start_col
        self.message = ''
        self.is_player_move = True

    def find(self, display, current_row, current_col):
        """
        find the position of a cell
        
        Arguments:
        display -- the display of the cell want to find
        current_row, current_col -- the current position of player

        Returns:
        a  list contains row and column of the cell
        """
        valid_display = ['X', 'Y', ' ', '*', 'F', 'W', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if display not in valid_display:
            raise ValueError('Please enter a valid display')
        
        row = 0
        result = []
        
        while row < len(self.grid):
            col = 0
            while col < len(self.grid[row]):
                if self.grid[row][col].display == display \
                        and (row != current_row or col != current_col):
                    result.append(row)
                    result.append(col)
                col += 1
            row += 1
        
        return result

    def draw(self):
        # draw the grid
        return grid_to_string(self.grid,self.player)

    def in_bound(self,row,col):
        """
        Check if the position is in the bound of grid
        
        Arguments:
        row, col -- the position going to check
        
        Returns:
        True if the position is in bound
        False if the position is out of bound, then player act as step on a wall
        """
        if type(row) != int or type(col) != int:
            raise ValueError('Please enter an integer row and col')
        
        if row <0 or row > len(self.grid)-1 or col < 0 or col > len(self.grid[0])-1:
            wall = Wall()
            wall.step(self)
            self.is_player_move = False
            return False
        else:
            return True

    def game_move(self,move):
        """
        Before move the player, check any special effect if move the player

        Arguments:
        move -- input from user (one of w, s, d, a, e, q, otherwise raise warning)
        """
        cr = self.player.row
        cl = self.player.col
        self.player.action = move
        
        if move == 'w':
            #If the next position is in the bound, step the next position to see if there is any special effect.
            if self.in_bound(cr-1,cl):
                self.next_row, self.next_col = cr-1, cl
                self.grid[cr-1][cl].step(self)
        
        elif move == 's':
            if self.in_bound(cr+1,cl):
                self.next_row, self.next_col = cr+1, cl
                self.grid[cr+1][cl].step(self)
        
        elif move == 'd':
            if self.in_bound(cr,cl+1):
                self.next_row, self.next_col = cr, cl+1
                self.grid[cr][cl+1].step(self)
        
        elif move == 'a':
            if self.in_bound(cr,cl-1):
                self.next_row, self.next_col = cr, cl-1
                self.grid[cr][cl-1].step(self)
        
        elif move == 'q':
            print('\nBye!')
            exit()
        
        elif move == 'e':
            # if player is on a teleport now and user input 'e', find the position of the other teleport and transit the player to there\
            # the player will not move one step since it is transit by the teleport
            if isinstance(self.grid[self.player.row][self.player.col], Teleport):
                display = self.grid[self.player.row][self.player.col].display
                self.player.row, self.player.col = self.find(display, self.player.row, self.player.col)
                self.is_player_move = False
                self.player.moves.append('e')
                self.message = '\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n'
        
        else:
            self.message = '\nPlease enter a valid move (w, a, s, d, e, q).\n'
            self.is_player_move = False
        
        # Set the display of start position to X
        self.grid[self.start_row][self.start_col]=Start()

    def message_parse(self):
        # parse the message from the game
        if self.message =='win':
            self.player.win()
        
        elif self.message == 'lose':
            self.player.lose()
        
        else:
            print(self.message)
        
        self.message = ''