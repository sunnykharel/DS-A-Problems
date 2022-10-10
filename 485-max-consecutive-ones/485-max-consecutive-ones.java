class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max=0;
        int num_ones=0;
        for(int i = 0; i< nums.length; i++){
            if(nums[i]==1){
                num_ones++;
            }
            else{
                if(num_ones>max){
                    max=num_ones;
                }
                num_ones=0;
            }
        }
        return Math.max(num_ones, max);
    }
}