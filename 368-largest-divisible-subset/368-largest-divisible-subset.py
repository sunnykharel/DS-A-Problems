class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # find all possible subsets --> 2^n, verify them --> O(n)
        
        '''
        memoization:
            sort(nums)
            
            make an edge from j --> i if nums[j] % nums[i] == 0
                for all i in range(0, sqrt(nums[j]))
            
            memo: keep track of num edges possible in memo[j]
            
            o(n^2)
            
            q2: how to avoid double counting
            
            [1,2,4,8]
                1. find the biggest number, then traverse find the set

        for each i in nums:
            maintain a set of children
            --> o(n^2) space
        '''
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        memo = [None]*n
        for i in range(0, n):
            memo[i] = set([nums[i]])
            # find the compatible j that has largest set size
            largest = -1
            largest_idx = -1
            for j in range(0, i): #TODO: optimize to sqrt(n) search
                
                if nums[i]%nums[j] == 0:
                    # print(j,i)
                    if len(memo[j])> largest:
                        largest_idx = j
                        largest = len(memo[j])
            if largest!=-1:    
                memo[i] = memo[i].union(memo[largest_idx])
        largest = max( memo, key=len)
        return list(largest)
                
        
        
        
        
        
        
        