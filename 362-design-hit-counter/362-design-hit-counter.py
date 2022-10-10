class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = collections.OrderedDict()
        self.hits = []
        
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.counts:
            self.counts[timestamp] = 0
            self.hits.append(timestamp)
        self.counts[timestamp]+=1
        
        # print(self.counts)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start, end = self.getHitsRange(timestamp)
        if start==None or end==None:
            return 0
        # print(start, end, timestamp)
        
        # k = self.counts.keys()
        return sum( self.counts[self.hits[i]] for i in range(start, end+1))
        
        
    def getHitsRange(self, timestamp):
        start, end = None, None
        
        # start is first value from left that is w/in timestamp-300
        # end is first val from right less than or eq timestamp
        
        for idx,i in enumerate(self.hits):
            if i > timestamp - 300:
                start = idx
                break
        for idx, i in enumerate(reversed(self.hits)):
            if timestamp-300 < i <= timestamp:
                end = len(self.hits)-idx-1
                break
        return start, end

        
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

'''
process hits with hit(timeStamp)

getHits()--> counts number of hits recieved in past 5 minutes

time is in units of seconds

ex: counter.getHits(301)--> 2, 3, 4

[1, 2, 3, 300]

[ c0, c1, c2, c3, c4, c5, c100 ...  ] -> our hits map idx by timestamp
    - hits may be sparse, so consider using hashmap
    - ordered dict, so that we can maintain order
    
    space(O(unique hits))
    
getHits:
    we look for valid start index, and valid end index
    then sum each count in range (start, end)
    
     - a simple two pointer solution will do 
     
    time (O(|unique hits|)) --> O(300 hits) prefix sum
        - actually a binary search will take from O(uh)--> o(log(uh))
    
'''



















