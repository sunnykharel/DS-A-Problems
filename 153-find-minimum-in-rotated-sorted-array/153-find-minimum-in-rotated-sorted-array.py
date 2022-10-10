class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        
        binary search point is to cut the array in half
        
        5670124
        6701245
        
        01234
        
        another case
        
        1,2,3,4,0
        
        4, 0, 1, 2, 3
        
        originally 
        4, 5, 6, 7, 0, 1, 2

        0, 1, 2, 4, 5, 6, 7
        
        '''
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        
        while left < right:
            #if odd then _ _ _ _ _     _ _ _ _ 
            mid = (left+right)//2
            if nums[mid]>=nums[0]:
                #num at mid occcurs before the shift point
                left = mid+1
            else:
                right = mid-1
        return min(nums[left], nums[(left+1)%len(nums)])
            
            
        
        
        