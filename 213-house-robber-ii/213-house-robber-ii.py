class Solution:
    def rob(self, nums: List[int]) -> int:
        #brute force is to get every possible arrangement of houses
        #the 1-d way of doing this is 
        #opt(i) = max{  opt(i-1), opt(i-2)+value[i]  }
        #issue with this solution if you choose the first house, you can choose
        #the second house.
        #think about having a 'flag' firstHouse true
        #dynamic programming works since each problem is a subproblem
        #however at the last index...
        #choosing the first and last house are mutually exclusive
        #   2,3,2
        # try 2,3
        # try 3,2
        # 1,2,3,1
        # try 1,2,3 --> 4
        # try 2,3,1 --> 3
        #do basically 2 robs, first with last house removed, second with first removed
        def robStartFinish( start, finish):
            opt_minus_1 = 0
            opt_minus_2 = 0
            for i in range(start, finish):
                opt_minus_1, opt_minus_2 = max( nums[i]+opt_minus_2, opt_minus_1 ), opt_minus_1 
            return opt_minus_1
        if len(nums)==1: return nums[0]
        return max( robStartFinish(1, len(nums)), robStartFinish(0, len(nums)-1) )
            
        
            