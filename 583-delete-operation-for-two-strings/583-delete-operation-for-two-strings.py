class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1=='' or word2=='':
            return max(len(word1), len(word2))
        
        n, m = len(word1), len(word2)
        opt = [[0 for _ in range(m+1)] for _ in range(n+1)]
        def valid(tup):
            nonlocal n,m
            return 0<=tup[0]<n and 0<=tup[1]<m
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                # we look at left, and up
                left = opt[i-1][j]
                up = opt[i][j-1]
                diag = opt[i-1][j-1]
                if word1[i-1]==word2[j-1]:
                    opt[i][j] = diag+1
                else:
                    opt[i][j] = max(left, up)
        
        return n+m-2*opt[n][m] 
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                        # this is basically a word ladder 
        # we remove the letters that are not in eaiter
        # we can delete either character in the string
        # we cannot add letters, only remove letters
        # brute force: remove first letter
        # delete first from first, delete first from second,
                                # , delete second from second
                                # , so forth
        # or we look for the longest chain similarity
        # longest = optimal
        # we start at string 1
        # for i in range(0, len(s1))
        # look for a chain starting from i
        # look for first occurence of s1[i] in s2, idx j
        # from j onwards look for first occ of s1[i+1]
        # while j < len(s2)
        # we can choose 1 letter to go next or any other
        # have to generate all possible substrings first
        # have to validate that this combo can be found in word2
                
                
                
                    
                    
                    
        
        
        
            
            