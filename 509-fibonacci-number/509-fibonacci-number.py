class Solution:
    def fib(self, N: int) -> int:
        opt = [0,1]
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        for i in range(2, N+1):
            opt_i = sum(opt)
            opt = [opt[1], opt_i]
            
        return opt[1]