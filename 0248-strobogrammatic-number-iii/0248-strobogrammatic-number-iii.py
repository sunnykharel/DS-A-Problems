class Solution:
    def __init__(self):
        self.strobo_nums = ['0', '1', '6', '8', '9']
        self.strobo_pairs = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
        }
        self.non_strobo = {'2', '3', '4', '5', '7'}
        self.low, self.high = 0, 0

    def is_valid_number_in_range(self, number: str):
        int_number = int(number)
        return len(str(int_number)) == len(number) \
            and self.low <= int_number <= self.high

    def findStroboNumsInSizeRange(self, n):
        count = 0
        res = []
        even_prev = [f'{kv[0]}{kv[1]}' for kv in self.strobo_pairs.items()]
        odd_prev = [kv[0] for kv in self.strobo_pairs.items() if kv[0]==kv[1]]
        prev, curr = even_prev+odd_prev, []
        start = 4 if n%2 == 0 else 3
        for number in prev:
            if self.is_valid_number_in_range(number):
                count+=1

        for size in range(start, n+1, 2):
            for node in prev:
                for l, r in self.strobo_pairs.items():
                    number = l+node+r
                    curr.append(number)
                    if self.is_valid_number_in_range(number):
                        count+=1
            prev = curr
            curr = []
        return count

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.low, self.high = int(low), int(high)
        n = len(high)
        strobo_nums_in_range = self.findStroboNumsInSizeRange(n)
        return strobo_nums_in_range

        