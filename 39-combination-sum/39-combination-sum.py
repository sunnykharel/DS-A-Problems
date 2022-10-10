class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #To do problem using backtracking:
        #basically do a bfs
        candidates.sort()
        targetSums = []
        n = len(candidates)
        def combinationSum(numbers, total, index):
            if total == target:
                targetSums.append(list(numbers))
            elif total < target:
                while index < n and candidates[index]+total <= target :
                    num = candidates[index]
                    numbers.append(num)
                    combinationSum(numbers, total+num, index)
                    numbers.pop()
                    index+=1
        combinationSum([], 0, 0)
        return targetSums
                
        