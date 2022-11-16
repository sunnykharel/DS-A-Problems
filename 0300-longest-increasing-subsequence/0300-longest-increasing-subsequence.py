class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        
        brute force: go from that number as far as possible 
        to the right
        
        find the longest subsequence including that number
        - doesn't work because the next number not be the most optimal
        - so basically, for each number you have to try all of the next
        numbers. 
        This is o(n^3).. not o(n^2)
        
        what number to exactly choose in this scenario
        you have n options of numbers to start from, which one do you choose
        
        -not a good way of looking at the problem...
        
        
        make subproblems: 
        you find the max subsequence for indicies 0,1,2 ...
        then you find the best one out of the previous before this one
        by finding the highest score among the non-overlapping solutions
        
        to find which one is non overlapping is a o(n^2) operation
        to search all the ones before.. now
        
        10,9,8,7,6,5
        
        
        '''

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2 if nums[1]>nums[0] else 1
        opt = [1, 2 if nums[1]>nums[0] else 1]
        lis = 1
        for i in range(2, n):
            lis_prev = 0
            for j in range(i-1,-1 , -1):
                if nums[j] < nums[i]:
                    lis_prev = max(opt[j], lis_prev)
            lis_curr = lis_prev+1
            lis = max(lis_curr, lis)
            opt.append(lis_curr)
        return lis
        
            
            
                    
        
        
        
        
        
        
#         lis = 0
#         for i in range(len(nums)):
#             prev = nums[i]
#             length = 1
#             for j in range(i, len(nums)):
#                 if nums[j]> prev:
#                     length+=1
#                     prev = nums[j]
#             lis = max(lis,length)
#         return lis
                    
                
                
        