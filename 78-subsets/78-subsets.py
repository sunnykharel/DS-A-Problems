class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsetList = []
        def subsets(depth, numbers):
            if depth == n:
                print(numbers)
                subsetList.append(list(numbers))
            elif depth<n:
                numbers.append(nums[depth])
                subsets(depth+1, numbers)
                numbers.pop()
                subsets(depth+1, numbers)
        subsets(0, [])
        return subsetList
            
        