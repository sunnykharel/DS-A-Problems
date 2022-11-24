class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # we have the formula
        # row * column -> sum -> sum goes into res[row][column]
        # we can iterate on rows of the first matrix
        #   then iterate on each of the cols of the second
        
        # brute force:
        # for loop on rows for mat1 nested loop for cols on mat2
        
        rows = len(mat1)
        cols = len(mat2[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                row = mat1[r]
                col = [mat2[k][c] for k in range(len(mat2))]
                value = sum(rc_vals[0]*rc_vals[1] for rc_vals in zip(row, col))
                result[r][c] = value
        return result
                