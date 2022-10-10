class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        def is_peak(i):
            if i == 0:
                return nums[i]> nums[i+1]
            if i == len(nums)-1:
                return nums[i]>nums[i-1]
            else:
                return nums[i-1]<nums[i]>nums[i+1]
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            if r-l==1:
                if nums[l] > nums[r]:
                    return l
                else:
                    return r
            
            mid = (l+r)//2
            if is_peak(mid):
                return mid
            else:
                # go to the increasing side
                if mid == 0:
                    return 0
                if mid == len(nums)-1:
                    return 0
                if nums[mid-1]> nums[mid]:
                    r = mid
                else:
                    l = mid+1
        if nums[r]>nums[l]:
            return r
        else:
            return l
        
            