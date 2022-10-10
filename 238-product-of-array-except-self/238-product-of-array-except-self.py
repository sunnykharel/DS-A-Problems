class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        lefts = [1 for _ in range(n)]
        lefts[0] = 1
        for i in range(1, n):
            lefts[i] = lefts[i-1]*nums[i-1]

        right_product = 1
        for i in range(n-1, -1, -1):
            lefts[i] *= right_product
            right_product *= nums[i]
        return lefts

            
        
            
        