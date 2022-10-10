class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        '''
        flip row, easy as reverse
        flip row, and immediatly invert the value
        do for each row
        '''
        i=0
        while i < len(A):
            row = A[i]
            l, r = 0, len(row)-1
            while l <= r:
                left = row[l]
                right = row[r]
                row[l] = 0 if right == 1 else 1
                row[r] = 0 if left == 1 else 1
                l+=1
                r-=1
            i+=1
        return A