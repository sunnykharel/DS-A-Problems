class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        1. brute force
            for every string go as far as you can in both directions,
            note the farthest, i.e. longest palindrome
            O(n^2)
            
            boundary i-j>0 and i+j<=len(s)
            
            you can also do an even palindrome as well
        '''
        longest=1
        beg, end = 0,0
        
        for i in range(len(s)):
            l = i-1
            r = i+1
            while( l>=0 and r<len(s)  and s[l]==s[r]):
                l-=1
                r+=1
            l+=1
            r-=1
            if r - l +1 > longest:
                longest = r-l+1
                beg,end = l, r

            l = i
            r = i+1
            while(l>=0 and r<len(s)  and s[l]==s[r]):
                l-=1
                r+=1
            l+=1
            r-=1
            if r - l +1 > longest:
                longest = r-l+1
                beg,end = l, r
            
        return s[beg:end+1]

    
                
            
        