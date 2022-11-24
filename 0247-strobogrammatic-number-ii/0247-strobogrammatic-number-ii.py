class Solution:
    def __init__(self):
        self.strobo_nums = ['0', '1', '6', '8', '9']
        self.strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }

    def is_strobogrammatic(self, num: list) -> bool:
        non_strobo = {'2', '3', '4', '5', '7'}
        strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }
        n = len(num)
        for i in range(n//2 + 1):
            l, r = num[i], num[-(i+1)]
            if l in non_strobo or r in non_strobo:
                return False
            if strobo_pairs[l] != r or strobo_pairs[r] != l:
                return False
        return True
    
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        digits = [0 for _ in range(n)]
        permutations = []
        self.recursion(0, digits, n, permutations)
        return permutations
        
    def recursion(self, idx, digits, n, permutations):
        reach_end = (
            ((n%2==0) and idx == n//2) or ((n%2==1) and idx == n//2+1)   
        )
        if reach_end:
            if self.is_strobogrammatic(digits):
                number = ''.join(digits)
                if len(str(int(number))) == len(number):
                    permutations.append(number)
            return

        for num in self.strobo_nums:
            digits[idx], digits[-(idx+1)] = num, self.strobo_pairs[num]
            self.recursion(idx+1, digits, n, permutations)

        digits[idx], digits[-(idx+1)] = 0, 0
        return
    
    
    '''
    4//2 = 2: 0,1
    5//2 = 2: 0, 1, 2, 3, 4
    2, -(2+1) = -3
    if (n%2 == 1) and n == n//2:
        only go once
        
        we can do some type of dynamic programming to memoize
    
    '''
            
            
        