class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        total_ones = sum(data)
        if total_ones <=1:
            return 0
        
        curr_ones = sum( data[i] for i in range(total_ones))
        l, r = 0, total_ones-1
        max_ones = curr_ones
        
        for i in range(total_ones, len(data)):
            curr_ones-=data[l]
            curr_ones+=data[i]
            l+=1
            max_ones = max(max_ones, curr_ones)
        return total_ones-max_ones
            
            
            
        
            
        '''
        swaps in general
        
        have a sliding window of size=TOTAL_NUMBER_OF_ONES
        see which start end required
        
        ##find the window with the maximum number of ones
        
        
        
        see how many more ones it needs, 
        that is output
        
        '''