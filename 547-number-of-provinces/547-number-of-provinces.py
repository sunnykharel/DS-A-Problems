class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        
        def dfs(i, visited):
            if i in visited:
                return
            visited.add(i)
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    dfs(j, visited)
                
        total = 0
        for i in range(0, len(M)):
            if i in visited:
                continue
            else:
                total+=1
                dfs(i, visited)
        return total
                
        
        