class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        brute force: do a linear search
        -> o(n)
        -> faster: do log(n)
        
        nums are unique
        nums guarenteed to be rotated at some pivot
        
        keep track of left-most
        keep track of right-most
        keep track of middle
        
        4,5,6,7,0,1,2
              _
              left = 0 right = 6
              
        7,0,1,2,4, 5, 6, 7
        1. left to middle: left is bigger, range of vals
            nums[l] to 10^4
             AND
            0 to nums[m]
        
        2. left to middle: left is smaller:
          range of vals: nums[l] to nums[m]
        
        3. mid to right: right is bigger
            range: nums[m] to nums[r]
        4. mid to right: right is smaller
           range of vals: 
            nums[m] to 10^4 and 0 to nums[r]
        
        funct that takes in left right and determines if target lies in there
        
         [4  5  6  7  0  1  2]
         l, r = 0, 6
         m = 7//2 = 
         
         
         even list: _ _ _ _ 0+3/2 = 1 -> take the left
         odd list:  _ _ _ _ _ 4/2 = 2 -> choose precisely the middle
        
        '''
        def target_in_range(l_indx, r_indx, target):
            if nums[l_indx] > nums[r_indx]:
                return nums[l_indx]<=target or target<=nums[r_indx]
            else:
                return nums[l_indx]<=target and target<=nums[r_indx]
        
        l, r = 0, len(nums)-1
        while l < r:
            m = (r+l)//2
            if target_in_range(l, m, target):
                r = m
            else:
                l = m+1
        
        if nums[l] == target:
            return l
        else:
            return -1
            
        
        
        
        
        
#         for i, num in enumerate(nums):
#             if num == target:
#                 return i
#         return -1