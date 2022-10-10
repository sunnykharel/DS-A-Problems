class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # non decreasing, means increasing
        #min number of movements
        # ie the min number of swaps
        # one way: find the min number of swaps
        # o(n^2)
        # we have a pointer on the left and a pointer on the right
        # if the value on the right is smaller, swap with left
        # if the value on the left is bigger, swap
        counter = collections.Counter(heights)
        mini = min(heights)
        maxi = max(heights)
        arr = []
        for i in range(mini, maxi+1):
            if i in counter:
                arr.extend([i]*counter[i])
        count = 0
        for i, j in zip(arr, heights):
            if i != j:
                count+=1
        return count
            