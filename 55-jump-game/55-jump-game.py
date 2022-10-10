class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        check path exist from end of nums
        --> see all possible paths from list[i] to prev
            is there a greedy choice?
                we are at i
                choose j in range i to i+nums[i], inclusive
                    such that greedy(j)
                    
                greedy(j):
                    max j : nums[j]+j is maximized
                
                choose 
                
                you go to the child that can reach more other 
                
                breaking point: when you reach a node that cannot go forward
                when you finally reach a nums[j]+j == len(nums)-1
        '''
        i = 0
        while i < len(nums):
            if i+nums[i]>=len(nums)-1:
                return True
            elif nums[i] == 0:
                return False
            max_distance = -1
            max_j = i
            for j in range(i+1, i+nums[i]+1):
                if nums[j]+j>max_distance:
                    max_distance = nums[j]+j
                    max_j = j 
            i = max_j
        
        
        
        