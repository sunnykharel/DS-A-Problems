class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = [i for i in s]     
        
        def rev(start, stop):
            nonlocal string
            while start < stop:
                string[start], string[stop] = string[stop], string[start]
                start+=1
                stop-=1
            
        
        i = 0
        n = len(s)
        while i < n:
            if n-i <= k:
                rev(i, n-1)
                return ''.join(string)
            elif n-i > k and n-i < 2*k:
                rev(i, i+k-1)
                return ''.join(string)
            else:
                rev(i, i+k-1)
                i+=2*k
        return ''.join(string)
        
        '''
        we just start at 0 and increment by 2k
        
        'a b c d e f g'
         1 2 3 4 5 6 7
         
        
        look at substrings to simplify
        case 1:
            len(s)-i <= k
                rev(i,len(s))
            
        case 2:
            len(s)-i > k and len(s)-i<2k
                rev(i,i+k)
    
        case 2:
        len(s)-i>2k
            rev(i, i+k)
            
            i+=2*k
                
        
        '''
        