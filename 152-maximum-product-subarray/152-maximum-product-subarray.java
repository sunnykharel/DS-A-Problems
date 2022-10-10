class Solution {
    public int maxProduct(int[] nums) {
        //we have to get all sub arrays
        //brute force: O(n^2)
        //O(n): Opt(i) = max
        //
        int max_prod = nums[0];
        for (int i = 0; i < nums.length; i++){
            int product = 1;
            for (int j = i; j < nums.length; j++ ){
                product*=nums[j];
                max_prod = Math.max(product, max_prod);
            }
        }
        return max_prod;
        
        
        
    }
}