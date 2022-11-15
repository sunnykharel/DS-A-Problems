class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        up, right, down, left = 0, 1, 2, 3
        memo = [[[0,0,0,0] for _ in range(cols)] for _ in range(rows)]
        for row in memo:
            print(row)
        def set_up_value(row, col):
            if grid[row][col] == 'W':
                memo[row][col][up] = 0
            elif row == 0:
                memo[row][col][up] = \
                    1 if grid[row][col] == 'E' else 0
            else:
                memo[row][col][up] = \
                    int(grid[row][col] == 'E') + memo[row-1][col][up]

        def set_down_value(row, col):
            print(row,col)
            if grid[row][col] == 'W':
                memo[row][col][down] = 0
            elif row == rows-1:
                memo[row][col][down] = \
                    1 if grid[row][col] == 'E' else 0
            else:
                memo[row][col][down] = \
                    int(grid[row][col] == 'E') + memo[row+1][col][down]

        def set_right_value(row, col):
            if grid[row][col] == 'W':
                memo[row][col][right] = 0
            elif col == cols-1:
                memo[row][col][right] = \
                    1 if grid[row][col] == 'E' else 0
            else:
                memo[row][col][right] = \
                    int(grid[row][col] == 'E') + memo[row][col+1][right]
        
        def set_left_value(row, col):
            if grid[row][col] == 'W':
                memo[row][col][left] = 0
            elif col == 0:
                memo[row][col][left] = \
                    1 if grid[row][col] == 'E' else 0
            else:
                memo[row][col][left] = \
                    int(grid[row][col] == 'E') + memo[row][col-1][left] 
        
        for row in range(0,rows):
            for col in range(0,cols):
                #get ups and lefts
                # up
                set_up_value(row, col)
                set_left_value(row,col)
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                set_down_value(row,col)
                set_right_value(row,col)
        
        opts = [[-1 for _ in range(cols)] for _ in range(rows)]
        max_hits = 0
                
        for row in range(rows):
            for col in range(cols):
                can_up, can_down = row > 0, row < rows-1
                can_left, can_right = col > 0, col < cols - 1
                coord_max_hits = 0
                is_not_empty_coord = grid[row][col] != '0'
                if is_not_empty_coord:
                    continue
                coord_max_hits = 0
                if can_up:
                    coord_max_hits += memo[row][col][up]
                if can_down:
                    coord_max_hits += memo[row][col][down]
                if can_right:
                    coord_max_hits += memo[row][col][right]
                if can_left:
                    coord_max_hits += memo[row][col][left]
                opts[row][col] = coord_max_hits
                max_hits = max(coord_max_hits, max_hits)
        # you can only place the bomb in the empty cell
        for row in grid:
            print(row)
        for row in memo:
            print(row)    
        print()
        for row in opts:
            print(row)
            
        expected = [
            [0,1,1,0], [1,1,2,1], [0,0,0,1], [0, 0, 1, 1]
            
        ]
        return max_hits
    
    
                
                
            
        '''
        brute force:
            you go to every index and then go left, right,
            up, down until you hit a wall in each direction
            this is a simple iteration in each direction.
            
            there is a property for each direction
            opt needs to take direction as another source of info
            
            how do you populate the memoization?
            if you are going down right, then you will 
            get the up memos and the left memos
            
            if you are going up left then you will get
            the right memos and the down memos
            
            memo = [[0 for _ in range()]]
            
            
            opt(i,j, up) = (
                0 if grid[i,j] == W,
                1 if grid[i,j] == E else 0, i == 0,
                1 if grid[i,j] == E else 0
                    + opt(i,j-1, up)
            )
            opt(i,j, down) = (
                0 if grid[i,j] == W,
                1 if grid[i,j] == E else 0, i == n-1,
                1 if grid[i,j] == E else 0
                    + opt(i,j-1, down)
            )
            opt(i,j, down)
            opt(i,j, left)
            opt(i,j, right)
            
            opt(i,j) = (
                1 if grid[i,j] == E else 0 + 
                opt(i-1)
            )
            
            opt(i,j,up) = 
            
        
        '''
