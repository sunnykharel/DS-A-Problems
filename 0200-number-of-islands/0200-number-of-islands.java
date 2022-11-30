class Solution {
    private int numLands (char[][] grid){
        int numLands = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == '1'){
                    numLands++;
                }
            }
        }
        return numLands;
    }
    private int surveyIsland(char[][] grid, int i, int j){
        Queue<Integer[]> q = new LinkedList<Integer[]>();
        Integer[] start = new Integer[] {i, j};
        q.add(start);
        int directions[][] = { {-1, 0} , { 1, 0}, {0, 1}, {0, -1} };
        int landsEncountered = 1;
        grid[i][j] = 0;
        while (q.size() > 0){
            Integer[] node = q.poll();
            int x = node[0];
            int y = node[1];
            for (int[] dir: directions){
                int deltaX = dir[0];
                int deltaY = dir[1];
                boolean xInBounds = !(x+deltaX < 0 || x+deltaX > grid.length-1);
                boolean yInBounds = !(y+deltaY < 0 || y+deltaY > grid[0].length-1);
                if (xInBounds && yInBounds && grid[x+deltaX][y+deltaY] == '1'){
                    grid[x+deltaX][y+deltaY] = 0;
                    landsEncountered++;
                    q.add( new Integer[] {x+deltaX, y+deltaY});
                }
            }
        }
        return landsEncountered;
    }
    public int numIslands(char[][] grid) {
        int numLands = numLands(grid);
        int numIslands = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++ ){
                if (grid[i][j] == '1'){
                    numLands += surveyIsland(grid, i, j);
                    numIslands++;
                }
            }
        }
        return numIslands;
    }
}