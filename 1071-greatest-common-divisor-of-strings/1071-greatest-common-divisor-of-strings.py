class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
            We want to find a repeating pattern
            that's the same in both strings
            It has to be repeating
            
            ABCABC
            
            ABC
            
            trees? Ah, we can use a trie here
            
            What is brute force?
            
            We get one sequence in string 1 and see if it divides both
            we get one sequence in string 2 and see if it divides both
            2 pass   
            
            Is there a 2 pointer solution
        '''
        def is_string_divisible_by_substring(string, substring):
            if len(string)%len(substring) != 0:
                return False
            
            repititions = len(string) // len(substring)
            return substring*repititions == string
        
        
        def valid_substrings(a, b):
            smaller_string = a if len(a) < len(b) else b
            valid_substrings = set()
            for i in range(len(smaller_string)):

                substring = smaller_string[:i+1]

                if substring in valid_substrings:
                    continue
                if (is_string_divisible_by_substring(a, substring) and 
                    is_string_divisible_by_substring(b, substring)):

                        valid_substrings.add(substring)

            return valid_substrings
        
        
        valid_substrings = valid_substrings(str1, str2)
        if len(valid_substrings) == 0:
            return ''

        gcd = max(valid_substrings, key=lambda substr: len(substr))
        return gcd
        
                        


                
                