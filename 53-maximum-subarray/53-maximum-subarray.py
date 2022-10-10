class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [nums[0]]
        # the if the prev is positive, then you include it
        # if the prev is negative, start new
        # we want to know, for each element, the max
        # sum that contains that index
        
        total_max = nums[0]
        
        for i in range(1, len(nums)):
            if memo[i-1]>0:
                memo.append(nums[i]+memo[i-1])
            else:
                memo.append(nums[i])
            total_max = max(total_max, memo[-1])
        return total_max