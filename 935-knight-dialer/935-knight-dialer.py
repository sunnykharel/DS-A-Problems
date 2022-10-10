class Solution:
     def knightDialer(self, N):
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)
        
        # if n == 1:
        #     return 10
        # maps = {
        #     0: {4, 6},
        #     1: {6, 8},
        #     2: {7, 9},
        #     3: {4, 8},
        #     4: {3, 9, 0},
        #     5: {},
        #     6: {1, 7, 0},
        #     7: {2, 6},
        #     8: {1, 3},
        #     9: {4, 2}
        # }
        # prev = [1]*10
        # for i in range(1, n):
        #     curr = [0]*10
        #     for j in range(0, 10):
        #         curr[j] = sum(prev[k] for k in maps[j])
        #     prev = curr
        # return sum(prev)%(10**9+7)
                
        
 