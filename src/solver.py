#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    alive_count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr==0 and dc==0:
                continue
            
            nr=row+dr
            nc=col+dc
            
            if 0<=nr<rows and 0<=nc<cols:
                if grid[nr][nc]==1:
                    alive_count+=1

    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            cell = grid[r][c]
            
            if cell==1:
                if neighbors in (2, 3):
                    next_grid[r][c]=1
            else:
                if neighbors==3:
                    next_grid[r][c]=1

    return next_grid