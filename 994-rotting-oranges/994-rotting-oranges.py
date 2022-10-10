class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        n = len(grid)
        m = len(grid[0])

        fresh_oranges = 0
        rotten_oranges_queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges+=1
                elif grid[i][j] == 2:
                    rotten_oranges_queue.append((i,j))

        minutes = 0
        while len(rotten_oranges_queue) > 0 and fresh_oranges!=0:
            new_rotten_oranges_queue = []
            for rotten_orange in rotten_oranges_queue:
                i,j = rotten_orange
                neighbors = []
                if i > 0:
                    neighbors.append((i-1,j))
                if i < n-1:
                    neighbors.append((i+1,j))
                if j > 0:
                    neighbors.append((i, j-1))
                if j < m-1:
                    neighbors.append((i, j+1))
                for neighbor in neighbors:
                    if grid[neighbor[0]][neighbor[1]] == 1:
                        new_rotten_oranges_queue.append(neighbor)
                        grid[neighbor[0]][neighbor[1]] = 2
                        fresh_oranges-=1
            rotten_oranges_queue = new_rotten_oranges_queue
            minutes+=1
        return minutes if fresh_oranges == 0 else -1
        
         
        
        