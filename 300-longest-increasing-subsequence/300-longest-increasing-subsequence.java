class Solution {
    public int lengthOfLIS(int[] nums) {
        
        //basically the knapsack problem where we 
        //can choose to select something or not
        if (nums.length==0)
            return 0;
        int n = nums.length;
        int[] memo = new int[n];
        memo[0] = 1;
        int maxi = 1;
        for (int i = 1; i < nums.length; i++) {
            int max = 0;
            for (int j = i-1; j>=0; j--){
                if (nums[j] < nums[i])
                    max = Math.max(memo[j], max);
            }
            memo[i] = max+1;
            maxi = Math.max(memo[i], maxi);
        }
        return maxi;
        
    }
}