class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_str = ''
        for i in range(len(s)):
            #even palindrome
            l,r = i, i+1
            count_even = 0
            while 0<=l and r<len(s) and s[l]==s[r]:
                count_even+=1
                l-=1
                r+=1
                
            even_length = 2*count_even
            if even_length>longest:
                longest_str = s[l+1: r]
                longest=even_length
            
            # odd palindrome
            l, r = i-1, i+1
            count_odd = 0
            while 0<=l and r<len(s) and s[l]==s[r]:
                count_odd+=1
                l-=1
                r+=1
            odd_length = 2*count_odd+1
            if odd_length>longest:
                longest_str = s[l+1: r]
                longest=odd_length
                
                
                
        return longest_str
                
            
                
                
            
            #odd palindrome
            
            