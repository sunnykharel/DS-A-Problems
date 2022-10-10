class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        res = [[1]]
        
        for i in range(1, numRows):
            new = []
            new.append(1)
            for j in range(1,len(res[-1])):
                new.append(res[-1][j]+res[-1][j-1])
            new.append(1)
            res.append(new)
        return res
        