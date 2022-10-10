class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #each group contains exactly k characters
        #except for the first group
        '''
        "5F3Z-2e-9-w"
        
        i = start
        
        while i < len(str):
            letter_count
            
            while letter_count!=4
            
        edge cases:
            first is greater than k
            at the end, the letter may not be equal to k
            
        '''
        
        
        res = []
        
        letters = [S[j].upper() for j in range(0, len(S)) if S[j]!='-']
        print(letters)
        
        for j in range(len(letters), -1, -K):
            res.append(''.join( letters[max(0,j-K):j]))
        print(res)
        if res[-1] == '':
            res.pop(-1)
        return '-'.join(reversed(res))
            
        
        