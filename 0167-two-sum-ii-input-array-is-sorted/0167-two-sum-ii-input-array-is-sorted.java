class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /**
            The key
            How do we verify that the two pointer solution works?
            
            Doesn't the two pointer solution miss out on potential opportunities?
            
            Let's make sure that it does not
            
            let's say that we are at the left, and we want to go from right to left
            we move the left cursor if we need more
            we move the right cursor if we need less
            if we move the right cursor, and we have less than we need,
            then we move the left cursor to the right
            we are basically honing in on the value that we want
            when we go from right to left, then what do we do?
                that is essentially saying that there exists no
                possible pairs for all values to the right of the right pointer
                because we've exhausted all of them
            when we go from left to right
                that is essentially saying that there exists no 
                right ptr possible pairs for this left.ptr value,
                because we've tried all of them, and it led to too small of a result
                
            the algorithm will stop when the two pointers clash,
            meaning that we've examined all candidates for left pointers 
            and right pointers. It's essentially intelligently honing
            in on a solution
        */
        int l = 0; int r = numbers.length - 1;
        while (l < r){
            int currSum = numbers[l] + numbers[r];
            if (currSum == target) {
                return new int[] {l+1, r+1}; // 0-index to 1-index
            } else if(currSum < target) {
                l ++;
            } else {
                r --;
            }
        }
        return null;
    }
}