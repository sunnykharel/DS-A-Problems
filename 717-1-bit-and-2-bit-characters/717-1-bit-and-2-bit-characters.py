class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #can the last character be two bits
            #two options: 10 and 11
            #can take away 11 off the bat
        '''we must look at bits[:-2] to see if we can fit
           ANY sequence of 0, 10, 11
           recursion: 2^n almost
                try recursive back tracking
           side: if there is a one, it must be two bit
           greedy?
        '''
        if len(bits)==1:
            return True
        if len(bits)==2:
            if bits in [[0,0], [0,1]]:
                return True
            else:
                return False
        if bits[-2:] in [[0,0], [0,1]]: #it cannot end with two bits in these cases
            return True
        
        n = len(bits)-2
        def recursion(i):
            #return true if you reach the end and 
            #we start at i = 0, end at i = len(bits)-2
            '''case 1: i'''
            
            if i == n:
                return False 
            if i >n:
                return True
            if bits[i] == 0:
                return recursion(i+1)
            if bits[i:i+2] in [[1,0], [1,1]]:
                return recursion(i+2)
                    
            else:
                return True
                  
        return recursion(0)        

    
    
    
    
    
    