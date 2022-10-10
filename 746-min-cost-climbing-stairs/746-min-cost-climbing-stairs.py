class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we see subproblems, thus dynamic programming
        
        '''
        base cases
            opt[1] = min(cost[0], cost[1])
            opt[0] = cost[0]
            
        what is OPT(n)
        OPT(i) = min(opt(i-1), opt(i-2))+cost[i]
        
        '''
        
        if len(cost)<=2:
            return min(cost)
        
        opt = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            opt_i = min(opt)+cost[i]
            opt = [opt[1], opt_i]
            
            
            
        return min(opt)
        
        