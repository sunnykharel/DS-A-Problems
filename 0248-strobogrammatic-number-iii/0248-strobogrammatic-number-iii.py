class Solution:
    def __init__(self):
        self.strobo_nums = ['0', '1', '6', '8', '9']
        self.strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }
        self.non_strobo = {'2', '3', '4', '5', '7'}
        self.low, self.high = 0, 0

    def is_valid_number_in_range(self, number: str):
        return len(str(int(number))) == len(number) \
            and self.low <= int(number) <= self.high

    def findStroboNumsInSizeRange(self, n):
        res = []
        even_prev = [f'{kv[0]}{kv[1]}' for kv in self.strobo_pairs.items()]
        odd_prev = [kv[0] for kv in self.strobo_pairs.items() if kv[0]==kv[1]]
        prev, curr = even_prev+odd_prev, []
        start = 4 if n%2 == 0 else 3
        res.extend(prev)
        for size in range(start, n+1, 2):
            for node in prev:
                for l, r in self.strobo_pairs.items():
                    curr.append(l+node+r)
            res.extend(curr)
            prev = curr
            curr = []
        return list(filter(self.is_valid_number_in_range, res))

    



    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.low, self.high = int(low), int(high)
        n = len(high)
        strobo_nums_in_range = self.findStroboNumsInSizeRange(n)
        return len(strobo_nums_in_range)

        