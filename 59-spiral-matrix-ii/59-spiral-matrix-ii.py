class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        size = n
        level = 0
        number = 1
        solution = [[0 for j in range(n)] for i in range(n)]

        while size > 0:
            if size == 1:
                solution[level][level] = number
                break
            else:
                for j in range(level, n-level):
                    solution[level][j] = number
                    number +=1
                for i in range(level+1, n-level-1):
                    solution[i][n-1-level] = number
                    number+=1
                for j in range(n-level-1, level-1, -1):
                    solution[n-1-level][j] = number
                    number+=1
                for i in range(n-level-1-1, level, -1):
                    solution[i][level] = number
                    number+=1
            size -=2
            level+=1
        return solution