class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        
#         all letter combinations the number could represent
#         complexity : length(number)*3
        
#         first number: 3 possibilities 3 n(3n(3n-1)*...)
#         second number: 3 possibilities
            
#         create a trie node
        if digits == "":
            return []
        solution = []
        def recursion(path, depth):
            if depth == len(digits):
                solution.append(path)
                return
            else:
                for letter in maps[digits[depth]]:
                    recursion(path+letter, depth+1)
                return
        recursion('', 0)
        return solution
            
        
            
                