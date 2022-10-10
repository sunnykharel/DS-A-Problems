class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = dict()
        extra_letters = []
        result = ['' for _ in range(len(s))]
        for char in order:
            counts[char] = 0
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                extra_letters.append(char)
        
        i = 0
        for char, count in counts.items():
            for _ in range(count):  
                result[i] = char
                i+=1
        for char in extra_letters:
            result[i] = char
            i+=1
        
        return ''.join(result)
            
        