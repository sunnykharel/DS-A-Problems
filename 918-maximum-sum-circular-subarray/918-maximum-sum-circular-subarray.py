class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # find the minimum and the maximum
        '''
        '''
        nonneg_count = sum(1 for i in A if i>=0)
        if nonneg_count == 0:
            return max(A)
        
        curr, total_max = 0,0
        for i in A:
            curr = max(0, i+curr)
            total_max = max(total_max, curr)
            
        curr, total_min = 0,0
        for i in A:
            curr = min(0, i+curr)
            total_min = min(total_min, curr)
            
        return max( sum(A)-total_min, total_max   )
        
        # now we need to find the min sum
        # take the negative and find the max
#         [1,-2,3,-2]
        
#         if pos prefer a 0
        
            
        
        
            
            
        
        
        
            
            