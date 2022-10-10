class Solution {
    private int[] original;
    private int[] shuffled;
    public Solution(int[] nums) {
        original = nums;
        shuffled = new int[nums.length];
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int[] placekeeper = new int[this.original.length];
        int unique = 0;
        for (int i = 0; i < this.original.length; i++){
            int random = (int) (Math.random()*this.original.length);
            while (placekeeper[random]!=0) {
                random = (int) (Math.random()*this.original.length);
            }
            this.shuffled[i] = original[random];
            placekeeper[random] = 1;
        }
        
        return this.shuffled;
        //index 1 can choose from any of the three
        //index 2 can choose from any of the two
        //1 can go to any other place
        //so can 2
        //on a collision
        //have to recalculate the shuffled value
        //we choose from any index rather
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */