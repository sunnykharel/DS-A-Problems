class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        # n cnadies
        # i'th candy is of type candies[i]
        # want to distribute candies evenly
        # n is even
        # so there are n/2 spots
        # fill the variety first, then 
        
        n = len(candies)
        seen = set()
        for i in candies:
            if i not in seen:
                seen.add(i)
        return min(len(seen), n//2)