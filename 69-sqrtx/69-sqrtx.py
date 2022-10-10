class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x//2
        
        while l <= r:
            m = (l + r) // 2
            if m*m <= x < (m+1)*(m+1):
                return m
            if m*m > x:
                r = m - 1
            elif m*m < x:
                l = m + 1
        return l
                
            