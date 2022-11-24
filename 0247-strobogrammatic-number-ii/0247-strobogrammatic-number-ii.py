class Solution:
    def __init__(self):
        self.strobo_nums = ['0', '1', '6', '8', '9']
        self.strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }
        self.non_strobo = {'2', '3', '4', '5', '7'}

    def is_strobogrammatic(self, num: list) -> bool:
        n = len(num)
        for i in range(n//2 + 1):
            l, r = num[i], num[-(i+1)]
            if l in self.non_strobo or r in self.non_strobo:
                return False
            if self.strobo_pairs[l] != r or self.strobo_pairs[r] != l:
                return False
        return True

    def is_valid_number(self, number: str):
        return len(str(int(number))) == len(number)
    
    
    def findStroboBfs(self, n: int) -> List[str]:
        prev = []
        curr = []
        start = 0
        if n%2 == 0:
            start = 4 
            for key, val in self.strobo_pairs.items():
                prev.append(f'{key}{val}')
        else:
            start = 3
            for key, val in self.strobo_pairs.items():
                if key==val:
                    prev.append(key)
        
        for size in range(start, n+1, 2):
            for node in prev:
                for l, r in self.strobo_pairs.items():
                    curr.append(l+node+r)
            prev = curr
            curr = []
        return sorted(filter(self.is_valid_number, prev))


    def findStrobogrammatic(self, n: int) -> List[str]:
        # digits = [0 for _ in range(n)]
        # permutations = []
        # self.recursion(0, digits, n, permutations)
        return self.findStroboBfs(n)

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
            
            
        