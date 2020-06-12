def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    strn = ''
    row = 0
    
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            if row == player.row and col == player.col:
                strn += player.display
            else:
                strn += grid[row][col].display
            col += 1
        strn+='\n'
        row += 1

    if player.num_water_buckets == 1:
        strn += '\nYou have {} water bucket.'.format(player.num_water_buckets)
    else:
        strn += '\nYou have {} water buckets.'.format(player.num_water_buckets)
    return strn