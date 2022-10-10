class Solution {
    public int numOfWays(int n) {
        //dynamic programming
        //top right grid can take 3 colors
        //every grid next to it can take 2 colors
        int r = 0;
        int y = 1;
        int g = 2;
        // if (n==1)
        //     return 12;
        
        int[][] combos = {
            {r,y,r},{y,r,y},{g,r,y},{r,y,g},{y,r,g},{g,r,g},{r,g,r},{y,g,r},{g,y,r},{r,g,y},{y,g,y},{g,y,g}
        };
        int[] prev =  {1,1,1,1,1,1,1,1,1,1,1,1};
        
        //see the vertical capability count for each
        for (int k = 2; k <=n; k++){
            int[] numWays = new int[12];
            for (int i = 0; i < 12; i++){
                for(int j = 0; j < 12; j++){
                    if(combos[i][0]!=combos[j][0] && combos[i][1]!=combos[j][1] && combos[i][2]!=combos[j][2]){
                        numWays[i]=(numWays[i]+prev[j])%(1000000007);
                    }
                }
            }
            prev = numWays;

        }
        int sum = 0;
        for (int i: prev)
            sum = (sum+i)%1000000007;
        
        
        
        return sum;        
    }
}