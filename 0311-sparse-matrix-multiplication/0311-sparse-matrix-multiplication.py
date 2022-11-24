class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows = len(mat1)
        cols = len(mat2[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                result[r][c] += sum(mat1[r][k]*mat2[k][c] for k in range(len(mat2)))

        return result
                