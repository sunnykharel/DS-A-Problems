class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
#         opt = [0 for i in range(0, len(nums))]
#         opt[0] = 1
        
#         for i in range(1, len(nums)):
#             if(nums[i]>nums[i-1]):
#                 opt[i] =  opt[i-1]+1
#             else:
#                 opt[i] = 1
#         return max(opt)

        maximum=1
        streak = 1
        for i in range( 1, len(nums) ):
            if nums[i]>nums[i-1]:
                streak+=1
                maximum=max(streak, maximum)
            else:
                streak = 1
        return maximum
            

        