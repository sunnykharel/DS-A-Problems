class Solution {
    public int subarraySum(int[] nums, int k) {
        int total = 0;
        for(int i = 0; i< nums.length; i++){
            int sum = nums[i];
            if(sum == k)
                total++;
            for(int j = i+1; j<nums.length; j++){
                sum+=nums[j];
                if(sum == k){
                    total++;
                }
            }
            
        }
        return total;
    }
}