class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
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
                