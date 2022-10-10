class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        def getNumOccurencesMap(string): 
            thisCount = {}
            for char in string:
                if char not in thisCount:
                    thisCount[char]=0
                thisCount[char]+=1
            return thisCount
        
        
        count = getNumOccurencesMap(A[0])
        for string in A: 
            thisCount = getNumOccurencesMap(string)
            for char in count:
                if char not in thisCount:
                    count[char] = 0
                else:
                    count[char] = min(thisCount[char], count[char])
                    
        res = []
        sortedCount = [0 for i in range(26)]
        for i in count:
            sortedCount[ord(i)-97]=count[i]
        for i in range(26):
            total = sortedCount[i]
            while total>0:
                res.append(chr(i+97)+"")
                total-=1
        return res
            
        