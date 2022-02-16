# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    print("inital_beliefs: " + str(beliefs))
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(grid)
    width = len(grid[0])
    #numerator = p_hit + ((height * width) - 1)*p_miss
    
    for row in range(height):
        new_row=[]
        for col in range(width):
                new_value = 0
                current_value = grid[row][col]
            if color == grid[row][col]:
                new_value = p_hit*current_value
                new_row.append(new_value)
            else:
                new_value = p_miss*current_value
                new_row.append(new_value)
        
        new_beliefs.append(new_row)
    numerator = sum(new_beliefs)
    print("numerator: " + str(numerator))
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j]=new_beliefs[i][j]/numerator
        
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    print("\nheight: " + str(height))
    width = len(beliefs[0])
    print("\nwidth: " + str(width))
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    #print("\nnew_G: " + str(new_G)), #produces a grid of zeros
    
    for i, row in enumerate(beliefs):#rows change only a little but the same multiples of 0.675
        
        #print("\ncurrent row of probabilities: " + str(row))
        print("\nCurrent i: " + str(i))
        print("row shift dy: " + str(dy))
        new_i = (i + dy ) % width
        #print("\n(i + dy) % width: " + "(" + str(i) + " + " + str(dy) + ")" + " % " + str(width))
        print("new_i: " + str(new_i) + "\n")
        print("column shift dx: " + str(dx))
                
        for j, cell in enumerate(row):#why enumerate??pulls out the individual item
            
            new_i = (i + dy ) % width
            
            #print("\n(i + dy) % width: " + "(" + str(i) + " + " + str(dy) + ")" + " % " + str(width))
            #print("new_i: " + str(new_i))
            
            new_j = (j + dx ) % height
            #print("\n(j + dx) % width: " + "(" + str(j) + " + " + str(dx) + ")" + " % " + str(height))
            print("old_j: " + str(j) + ", new_j: " + str(new_j))
            
            # pdb.set_trace()
            #print("\ncell: " + str(cell))
            new_G[int(new_i)][int(new_j)] = cell
        print("\ncurrent row of probabilities: " + str(row))
        print("\nnew row values after shift: " + str(new_G[new_i]))    
    print("\nOld_G: " + str(beliefs))        
    print("\n\nnew_G: " + str(new_G))
    #print("\nblurring: " + str(blurring))
    #print("\nnormalized_grid: " + str(normalized_grid))
    normalized_grid = blur(new_G, blurring)
    #print("\nnormalized_grid: " + str(normalized_grid))
    return normalized_grid













