class Solution {
    public int pivotIndex(int[] nums) {
        
        //Keep growing sum from left -> right
        //Keep growing sum from right -> left
        // Org:[1, 7,  3,   6,  5,  6]
        // LtR [1,  8,  11, 17, 22, 28]
        // RtL [28 ,27 ,20 ,17 ,11 ,6]
        
        int n = nums.length;
        int[] leftToRight = new int[n];
        int[] rightToLeft = new int[n];
        rightToLeft[n-1] = nums[n-1];
        leftToRight[0] = nums[0];
        
        
        for(int i=1; i < n; i++){
            leftToRight[i] += nums[i] + leftToRight[i-1];
            rightToLeft[(n-i)-1] += nums[(n-i)-1] + rightToLeft[n-i];
        }
        for (int i = 0; i < n; i++){
            if (leftToRight[i] == rightToLeft[i]){
                return i;
            }
        }
        return -1;
    }
}