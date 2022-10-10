class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #need to have an n^2 memo
        #opt(i,j): case 1: don't include p
        if(len(s)==0):
            return 0
        if(len(s)==1):
            return 1
        longestSubstring=1
        for i in range(0, len(s)):
            encountered = set()
            encountered.add(s[i])
            j = i+1
            longest=1
            while(j< len(s) and s[j] not in encountered):
                encountered.add(s[j])
                j+=1
                longest+=1
            longestSubstring=max(longestSubstring, longest)
        return longestSubstring
            
        