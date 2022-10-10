class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # first word alphanumeric identifier
        # after first,
            #each word only consist lowercase (letter logs)
            #or only digits (digit logs)
        #guarenteed each log has identifier + word
        #want letter logs before digit logs
        #sort letter logs lexigraphically
        
            
        
        letters = []
        numbers = []
        mapz = dict()
        
        for i in logs:
            first_space = i.index(' ')
            identifier, string = i[:first_space], i[first_space+1:]
            if ord('a')<=ord(string[0])<=ord('z'):
                letters.append(i)
                mapz[i] = string
            else:
                numbers.append(i)
        def comparator(s1, s2):
            nonlocal mapz
            if mapz[s1] == mapz[s2]:
                if s1<s2:
                    return -1
                else:
                    return 1
            else:
                if mapz[s1]<=mapz[s2]:
                    return -1
                return 1
                
        letters.sort(key=cmp_to_key(comparator))
        return letters+numbers
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
        