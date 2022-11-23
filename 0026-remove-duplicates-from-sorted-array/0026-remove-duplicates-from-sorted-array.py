class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_idx = 0
        val = nums[0]
        n = len(nums)
        i, k = 0,0
        while i < n:
            j = i
            while j < n and nums[j] == val:
                j+=1
            nums[k] = val
            k += 1
            i = j
            if j < n:
                val = nums[j]
        return k
                
            