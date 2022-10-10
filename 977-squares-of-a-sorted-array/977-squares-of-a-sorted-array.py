class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        from collections import deque
        q = deque()

        n = len(nums)
        left_ptr = 0
        right_ptr = n-1

        while left_ptr <= right_ptr:
            if left_ptr == right_ptr:
                q.append(nums[left_ptr])
                break
            if abs(nums[left_ptr]) > abs(nums[right_ptr]):
                q.append(nums[left_ptr])
                left_ptr+=1
            else:
                q.append(nums[right_ptr])
                right_ptr-=1
        
        
        for i in range(n-1, -1, -1):
            nums[i] = q.popleft()**2
        return nums
            
            
                

            
            
            