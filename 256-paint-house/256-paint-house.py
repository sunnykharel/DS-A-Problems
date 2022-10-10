class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red = 0
        blue = 1
        green = 2
        #idea: you try to always paint with the lowest costing
        #color
        #then the second lowest costing
        #cost of painting each house with a certain col
        # dynamic programming: each row has some options
        if costs == []:
            return 0
        if len(costs)==1:
            return min(costs[0])
        prev = costs[0]
        curr = [0,0,0]
        
        for i in range(1, len(costs)):
            curr = costs[i]
            
            curr[0] = curr[0]+min(prev[1], prev[2])
            curr[1] = curr[1]+min(prev[0], prev[2])
            curr[2] = curr[2]+min(prev[1], prev[0])
            
            prev = curr
        return min(prev)
            