class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(1, len(points)):
            prev = points[i-1]
            curr = points[i]
            
            # reduce diag first
            # only if the min_difference in coords is 1 or greate
            diff_x = abs(prev[0]-curr[0])
            diff_y = abs(prev[1]-curr[1])
            
            min_diff = min(diff_x, diff_y)
            total += min_diff
            diff_x-=min_diff
            diff_y-=min_diff
            total+=diff_y+diff_x
        return total
            
            
            # finish off horizontal movements