class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        n = len(grid)
        if(n==0):
            return 0
        m=len(grid[0])
        if(m==0):
            return 0
        numIsles=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    coordinate=(i,j)
                    numIsles+=1
                    maxArea = max(maxArea, explore(coordinate, grid, n, m))
        return maxArea

        
def explore(coordinate, grid, n, m) -> int:
    x = coordinate[0]
    y = coordinate[1]
    if 0<=x<n and 0<=y<m and grid[x][y]==1:
        grid[x][y]=0
        total = 1 
        total+=explore((x,y-1), grid, n, m)
        total+=explore((x-1,y), grid, n, m)
        total+=explore((x+1, y), grid, n, m)
        total+=explore((x, y+1), grid, n, m)
        return total
    else:
        return 0