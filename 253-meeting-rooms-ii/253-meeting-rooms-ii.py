class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        greedy problem
        sch new room if conflict
        
        choose by start time
        let's say we put earliest start time,
        if the next earliest time conflicted,
            we would have needed two rooms anyway
            
        put the earliest time along with the slot with the earliest time
        
        input is not sorted:
        insert the whole input into a heap
        '''
        intervals.sort(key=lambda interval: interval[0])
        rooms = 0
        heap= []
        for meet in intervals:
            if len(heap)==0:
                heapq.heappush(heap, meet[1])
                rooms+=1
            elif heap[0] <= meet[0]:
                heapq.heappushpop(heap, meet[1])
            else:
                rooms+=1
                heapq.heappush(heap, meet[1])
        return rooms
            
            
                
        
        