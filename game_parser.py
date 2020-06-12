from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """
    Read in a file, process them using parse(),
    and return the contents as a list of list of cells.
    """
    try:
        f = open(filename)
    except:
        print('{} does not exist!'.format(filename))
        exit()
    
    lines = f.readlines()
    f.close()
    return parse(lines)

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    count_x = 0
    count_y = 0
    count_tele = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    grid = []
    
    for line in lines:
        str_cells = list(line.rstrip())
        obj_cells = []
        
        for cell in str_cells:
            if cell == 'X':
                obj_cells.append(Start())
                count_x+=1
            
            elif cell == 'Y':
                obj_cells.append(End())
                count_y+=1
            
            elif cell == ' ':
                obj_cells.append(Air())
            
            elif cell == '*':
                obj_cells.append(Wall())
            
            elif cell == 'F':
                obj_cells.append(Fire())
            
            elif cell == 'W':
                obj_cells.append(Water())
            
            elif cell.isdigit():
                if int(cell) in [i for i in range(1,10)]:
                    obj_cells.append(Teleport(cell))
                    count_tele[cell] += 1
                else:
                    raise ValueError('Bad letter in configuration file: {}.'.format(cell))
            
            else:
                raise ValueError('Bad letter in configuration file: {}.'.format(cell))
        
        grid.append(obj_cells)
    
    # Check there is one start, end, teleport in pairs
    if count_x != 1:
        raise ValueError('Expected 1 starting position, got {}.'.format(count_x))
    if count_y != 1:
        raise ValueError('Expected 1 ending position, got {}.'.format(count_y))
    for [key,value] in count_tele.items():
        if value == 1 or value > 2:
            raise ValueError('Teleport pad {} does not have an exclusively matching pad.'.format(key))
    
    return grid