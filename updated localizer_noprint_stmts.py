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

    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(grid)
    width = len(grid[0])
    
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
 
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j]=new_beliefs[i][j]/numerator
        
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]

    for i, row in enumerate(beliefs):
        new_i = (i + dy ) % width
        for j, cell in enumerate(row):#pulls out the individual item
            
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            new_G[int(new_i)][int(new_j)] = cell
			
    normalized_grid = blur(new_G, blurring)
	
    return normalized_grid