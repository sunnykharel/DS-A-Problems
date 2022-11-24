class Solution:
    def __init__(self):
        self.strobo_nums = ['0', '1', '6', '8', '9']
        self.strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }
        self.non_strobo = {'2', '3', '4', '5', '7'}
        self.low, self.high = 0, 0

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
    
    def findStroboBfsSizeRange(self, n: int) -> List[str]:
        result = []
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

    def findStroboNumsInSizeRange(self, n):
        # We want to find both even length strobos as well as odd length strobos
        # so we must keep track of even strobo nums as well as odd
        # we stop at the size len(high)
        # if number even:
        #   even stops at len(high), odd stops at len(high) -1
        # if number odd:
        #   even stops at len(high) -1 and odd stops at len(high)
        res = []
        even_prev, even_curr = [f'{kv[0]}{kv[1]}' for kv in self.strobo_pairs.items()], []
        odd_prev, odd_curr = [kv[0] for kv in self.strobo_pairs.items() if kv[0]==kv[1]], []
        
        prev, curr = even_prev+odd_prev, []
        start = 0
        if n%2 == 0:
            start = 4
        else:
            start = 3
        res.extend(prev)
        for size in range(start, n+1, 2):
            for node in prev:
                for l, r in self.strobo_pairs.items():
                    curr.append(l+node+r)
            res.extend(curr)
            prev = curr
            curr = []
        print(res)
        return sorted(filter(self.is_valid_number, res))
        
        
    def falls_in_range(self, number: str):
        # print(self.low, self.high, number)
        return self.low <= int(number) <= self.high


    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # step 1: get the size range of strobogrammatic numbers we want to generate
        #   - range(len(low), len(high) + 1)
        self.low, self.high = int(low), int(high)
        n = len(high)
        strobo_nums = self.findStroboNumsInSizeRange(n)
        if 0 <= int(low) <= 9 and 0 <= int(high) <= 9:
            # print('here')
            return len(list(filter(self.falls_in_range,['0', '1', '8'])))
        if (low,high) in [('0', '0'), ('1', '1'), ('8', '8')]:
            return 1
        return len(list(filter(self.falls_in_range,strobo_nums)))
        
        # step 2: given the range of sizes, we want to find all strobo numbers with sizes within the given range
        #   - create a function called findStroboNumsInSizeRange
        # step 3: Filter the result of step 2 for numbers with values in range(int(low), int(high))
        # step 4: return the result
        