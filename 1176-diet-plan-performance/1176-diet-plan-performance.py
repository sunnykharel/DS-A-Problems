class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # get sum of each sliding window of size k
        # check that the sum of the sliding window, then update total count
        # if sum_ < lower: total-=1
        # if sum > upper: total+=1
        n = len(calories)
        
        sum_k = sum(calories[j] for j in range(k))
        total = 0
        for i in range(0, n-k+1):
            if i != 0:
                sum_k -= calories[i-1]
                sum_k += calories[i+k-1]
            if sum_k < lower: 
                total-=1
            if sum_k > upper: 
                total+=1
        return total