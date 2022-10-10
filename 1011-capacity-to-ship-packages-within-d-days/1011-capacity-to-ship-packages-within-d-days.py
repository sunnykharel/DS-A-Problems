
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def possible(capacity):
            i = 0
            numDays = 0
            while i < len(weights) and numDays<=D:
                sums = 0
                while i<len(weights) and (sums+weights[i])<=capacity:
                    sums+=weights[i]
                    i+=1
                if sums==0:
                    return False
                numDays+=1
            return numDays<=D
        
        left = max(weights)
        right = sum(weights)
        middle = 0
        while left<=right:
            middle = (left+right)//2
            if possible(middle):
                right = middle-1
            else:
                left = middle+1

        return left
            
        
        
        #need to find D partitions
        # need to be of min weight or less
        # find the D partitions which require the least capacity
        #
        #
        # see if with this weight it's possible move within D days
        # if it is try a greater weight (have a left and right for possible weight range)
        # how to check if a certain weight is acceptable
        # go through linearly making groups of the certain weight
        # Observation: use the property that you must group ships in order
        # you will always have to fill in as much as you can for each group
        # greedy/optimal solution
        
        
    