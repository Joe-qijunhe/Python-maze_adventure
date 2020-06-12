class Player:
    def __init__(self):
        """
        display -- the display of the player
        num_water_buckets -- the number of water the player have
        row, col -- the position of the player
        moves -- store the move made by the player
        action -- store the user's input (record how the player move to the teleport)
        """
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0
        self.moves = []
        self.action = ''

    def move(self, move):
        # Move the player
        if move =='w':
            self.row -= 1
            self.moves.append('w')
        
        if move =='s':
            self.row += 1
            self.moves.append('s')
        
        if move =='d':
            self.col += 1
            self.moves.append('d')
        
        if move =='a':
            self.col -= 1
            self.moves.append('a')
        
        if move == 'e':
            self.moves.append('e')
    
    def moves_made(self):
        """
        Returns:
        A string contains how many moves the player made and their moves
        """
        message = ''
        num_of_move = len(self.moves)
        moves = ', '.join(self.moves)

        if len(self.moves) == 1:
            message += 'You made {} move.\n'.format(num_of_move)
            message += 'Your move: {}\n'.format(moves)
        else:
            message += 'You made {} moves.\n'.format(num_of_move)
            message += 'Your moves: {}\n'.format(moves)
        
        return message
    
    def win(self):
        # Print the winning message and the moves
        print()
        print('\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable \
Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n')
        print(self.moves_made())
        print('''=====================\n====== YOU WIN! =====\n=====================''')
        exit()

    def lose(self):
        # Print the winning message and the moves
        print()
        print('\nYou step into the fires and watch your dreams disappear :(.')
        print('\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of \
ash and is scattered to the winds by the next storm... You have been roasted.\n')
        print(self.moves_made())
        print('''=====================\n===== GAME OVER =====\n=====================''')
        exit()