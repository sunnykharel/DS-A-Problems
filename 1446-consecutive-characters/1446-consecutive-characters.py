class Solution:
    def maxPower(self, s: str) -> int:
        # do a loop through the string
        # keep track of the previous letter
        # max_power/max_occ
        # when we go to a new char then
        # if the new curr == prev_char, then you set the curr_power += 1: keep going
        # if new char != prev_char, then curr_power = 1, curr = new char: stop
        # 
        
        
        curr_char = ''
        curr_power = -1
        max_char = ''
        max_power = -1
        
        for char in s:
            # init
            if max_power == '' and max_occ == -1:
                max_char, max_occ = char, 1
                curr_char = char
                curr_power = 1
                continue

            # keep going
            if curr_char == char:
                curr_power += 1
                continue

            # reached a change of sequence
            if curr_power > max_power:
                max_char, max_power = curr_char, curr_power
            
            curr_char = char
            curr_power = 1
        
        # check if there was a sequence that goes till the end
        if curr_power > max_power:
            max_char, max_power = curr_char, curr_power
        
        return max_power
        
        
                
                    
                
                