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
        even_inits = [f'{kv[0]}{kv[1]}' for kv in self.strobo_pairs.items()]
        odd_inits = [kv[0] for kv in self.strobo_pairs.items() if kv[0]==kv[1]]
        q = collections.deque(even_inits+odd_inits)
        while len(q) > 0:
            node = q.popleft()
            if self.is_valid_number_in_range(node):
                count += 1
            if len(node) > n-2:
                continue
            for l,r in self.strobo_pairs.items():
                number = l+node+r
                if len(number) <= n:
                    q.append(number)
        return count

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.low, self.high = int(low), int(high)
        n = len(high)
        strobo_nums_in_range = self.findStroboNumsInSizeRange(n)
        return strobo_nums_in_range

    # def strobogrammaticInRange(self, low, high):
    #     q, cnt, low, high, ln = ["", "0", "1", "8"], 0, int(low), int(high), len(high)
    #     while q:
    #         s = q.pop()
    #         if s and s[0] != "0" and low <= int(s) <= high: cnt += 1
    #         q += [l + s + r for l, r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0")) if len(s) <= ln - 2] 
    #     return cnt if low != 0 else cnt + 1

        