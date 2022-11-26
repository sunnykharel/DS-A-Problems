"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def print_interval(self, interval):
        if interval is None:
            print("None")
            return
        print(f'start:{interval.start}; end:{interval.end}')
    
    def print_sched(self, sched):
        print("###")
        for interval in sched:
            self.print_interval(interval)
        print("###")
    
    def get_interval_overlaps(self, interval1, interval2):
        # self.print_interval(interval1)
        # self.print_interval(interval2)
        a = interval1
        b = interval2
        start, end = 0,0
        if(a.start <= b.start):
            start = b.start
        if(a.start > b.start):
            start = a.start
        if(a.end <= b.end):
            end = a.end
        if(a.end > b.end):
            end = b.end
        if end <= start:
            res = None
        else:
            res = Interval(start=start, end=end)
        # self.print_interval(res)
        return res
    
    def common_free_time(self, sched_1, sched_2):
        common_free_time = []
        for interval_a in sched_1:
            for interval_b in sched_2:
                if interval_b.start >= interval_a.end:
                    break
                interval_overlaps = self.get_interval_overlaps(interval_a, interval_b)
                if interval_overlaps:
                    common_free_time.append(interval_overlaps)
        return common_free_time

    
    def workToFreeTime(self, schedule):
        free_sched = []
        prev_end = -(10**9)
        for interval in schedule:
            if len(free_sched) == 0:
                free_sched.append(Interval(start=prev_end, end=interval.start))
                prev_end = interval.end
            else:
                free_sched.append(Interval(start=prev_end, end=interval.start))
                prev_end = interval.end
        free_sched.append(Interval(start=prev_end, end=10**9))
        free_sched.sort(key=lambda x: x.start)
        return free_sched
            
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        schedule = [self.workToFreeTime(sched) for sched in schedule]
        while len(schedule) >= 2:
            sched_1 = schedule.pop()
            sched_2 = schedule.pop()
            common_free_time = self.common_free_time(sched_1, sched_2)
            if common_free_time:
                schedule.append(sorted(common_free_time, key=lambda x: x.start))

        res = [interval for interval in schedule[0] \
               if interval.start!= -(10**9) and interval.end!=10**9]

        return res
            
            
            