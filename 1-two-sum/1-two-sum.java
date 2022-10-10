class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] pair = new int[2];
        Map<Integer, Integer> hashmap = new HashMap<>();
        // System.out.println(hashmap);  
        for ( int i = 0; i < nums.length; i++){
            if (hashmap.containsKey(target-nums[i])){
                pair[0]=hashmap.get(target-nums[i]);
                pair[1]=i;
                return pair;
            }
            hashmap.put(nums[i], i);
        }
        
        
        return pair;
        
    }
}