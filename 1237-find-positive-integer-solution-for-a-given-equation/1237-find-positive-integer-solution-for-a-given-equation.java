/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */

class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        //integer pairs where f(x,y) == z
        //solution 1: start x and y with value == 1
        //x,y is less than 1000, so we keep on increasing until we hit either 1000 or 
        //go above z
        /*
            f(x,y) > z case 1:
                decrease x
                decrease y
                have a memo to point to decrease x and decrease y
            f(x,y) < z case 2
        
        */
        List<List<Integer>> sol = new ArrayList<>();
        Set<Integer> squared = new HashSet<Integer>();
        int total = 0;
        for (int i = 1; i < 1000; i++){
            for (int j = 1; j < 1000; j++){
                if (i == j && squared.contains(i))
                    continue;
                if (customfunction.f(i,j)==z){
                    List<Integer> news = new ArrayList<Integer>();
                    news.add(i);news.add(j);
                    sol.add(news);
                    if (i==j)
                        squared.add(i);
                }
            }
        }
        return sol;
        
        
        
    }
}