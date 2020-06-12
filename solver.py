# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)
from game import Game
import sys
if len(sys.argv) != 3:
    print('Usage: python3 solver.py <filename> mode')
    exit()

filename , mode = sys.argv[1], sys.argv[2]
game = Game(filename)

class Search:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = []

def solve(mode):
    start = [game.player.row, game.player.col]
    wait_list = []
    wait_list.append(start)
    #Find the start point
    r , c = game.find('X', -1, -1)
    search = Search(r, c)
    
    while wait_list != []:
        if mode == 'BFS':
            pop = wait_list.pop(0)
        if mode == 'DFS':
            pop = wait_list.pop()
    
        row, col = pop
        #If this is the end, found the solution
        if game.grid[row][col].display == 'Y':
            print("Found the solution")
            break
        
        path = [[ row + 1, col], [ row - 1, col ], [row, col - 1], [row, col + 1]]
        i = 0
        while i < 4:
            point = path[i]
            r , c = point
            if [r,c] not in search.visited and game.in_bound(r, c):
                if game.grid[r][c].display == ' ':
                    wait_list.append([r,c])
                    search.visited.append([r,c])
                    if i == 0:
                        game.player.moves_made.append('s')
                    if i == 1:
                        game.player.moves_made.append('w')
                    if i == 2:
                        game.player.moves_made.append('a')
                    if i == 3:
                        game.player.moves_made.append('d')
            i+=1

    print(game.player.moves_made())


if __name__ == "__main__":
    solution_found = False
    solve(mode)
    if solution_found:
        pass
        # Print your solution...
    else:
        print("There is no possible path.")
