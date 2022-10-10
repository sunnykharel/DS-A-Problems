class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.dq = collections.deque()
        self.max_size = size
        self.curr_size = 0
        self.curr_sum = 0

    def next(self, val: int) -> float:
        if len(self.dq) < self.max_size:
            self.dq.append(val)
            self.curr_size += 1
            self.curr_sum += val
        else:
            rem = self.dq.popleft()
            self.dq.append(val)
            self.curr_sum+=val
            self.curr_sum-=rem
        return self.curr_sum/self.curr_size
            
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)