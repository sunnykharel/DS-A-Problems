class Solution {
    public int climbStairs(int n) {

    
        double sqrt5 = Math.sqrt(5.0);
        double pfi = (1.0+sqrt5)/2;
        return (int)((Math.pow(pfi, n+1) - Math.pow(-pfi, -(n+1)))/sqrt5 + 0.5);
    }
    
}