class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = collections.Counter(nums)
        j = 0
        while j < counter[0]:
            nums[j] = 0
            j+=1
        while j < counter[0]+counter[1]:
            nums[j] = 1
            j+=1
        while j < counter[1]+counter[2]+counter[0]:
            nums[j]=2
            j+=1
        return nums
            
            

        """
        Do not return anything, modify nums in-place instead.
        """
        