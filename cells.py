class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        """
        If current position is not a teleport, the current position become an Air block and the player is free to move
        If it is a teleport, it stays the same
        """
        if not isinstance(game.grid[game.player.row][game.player.col], Teleport):
            game.grid[game.player.row][game.player.col]=Air()

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        """
        If current position is not a teleport, the current position become an Air block and the player is free to move
        If it is a teleport, it stays the same
        Give a game message 'win'
        """
        if not isinstance(game.grid[game.player.row][game.player.col], Teleport):
            game.grid[game.player.row][game.player.col]=Air()
        game.message='win'


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        """
        If current position is a teleport, current position is the same teleport
        Otherwise, current position become an Air block
        """
        if isinstance(game.grid[game.player.row][game.player.col], Teleport):
            game.grid[game.player.row][game.player.col]=Teleport(game.grid[game.player.row][game.player.col].display)
        else:
            game.grid[game.player.row][game.player.col]=Air()


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        """
        The player will not move
        Give a game message of step on a wall
        """
        game.is_player_move = False
        game.message = '\nYou walked into a wall. Oof!\n'


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        """
        If player have more than one water, one water is used and give a message of extinguish fire and current position become an Air block
        If player donnot have water, give a message of lose and current position become an Air block
        """
        if game.player.num_water_buckets >= 1:
            game.player.num_water_buckets -= 1
            game.message = '\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!\n'
            game.grid[game.player.row][game.player.col]=Air()
        else:
            game.message = 'lose'
            game.grid[game.player.row][game.player.col]=Air()

class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        """
        player gain one water and give a message of gaining water and current position become an Air block
        """
        game.player.num_water_buckets += 1
        game.message = "\nThank the Honourable Furious Forest, you\'ve found a bucket of water!\n"
        game.grid[game.player.row][game.player.col]=Air()


class Teleport:
    def __init__(self,cell):
        self.display = cell

    def step(self, game):
        """
        Update how the player came to current teleport
        Find the corresponding teleport and move player to there, the player are not allowed to move then
        Give a game message of teleport
        """
        game.player.moves.append(game.player.action)
        display = game.grid[game.next_row][game.next_col].display
        game.player.row, game.player.col = game.find(display, game.next_row, game.next_col)
        game.is_player_move = False
        game.message = '\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n'