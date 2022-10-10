class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        values = []
        def permutations(depth, path, nums_left):
            if depth == 4:
                values.append(path)
            else:
                for i in range(len(nums_left)):
                    permutations(depth+1, path+str(nums_left[i]), nums_left[:i]+nums_left[i+1:])
        permutations(0, '', [i for i in arr])

        def is_valid_time(time):
            hour, minutes = time[:2], time[2:]
            if int(hour) > 23:
                return False
            if int(minutes) > 59:
                return False
            return True

        def time_to_total_minutes(time_):
            hour, minutes = time_[:2], time_[2:]
            return int(hour)*60 + int(minutes)

        values = [value for value in values if is_valid_time(value)]
        
        values.sort(key=lambda time: time_to_total_minutes(time))
        if len(values) == 0:
            return ""
        return values[-1][:2] +':'+ values[-1][2:]

                
        