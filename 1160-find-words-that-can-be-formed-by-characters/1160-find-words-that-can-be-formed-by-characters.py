class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # we can create all possible combos of words
        # we create a counter for each str
        
        # we have to see that the counts of every thing in str1 < counts of all in chars
        
        chars_counter = collections.Counter(chars)
        
        def check_validity(word):
            nonlocal chars_counter
            word_counter = collections.Counter(word)
            for char, count in word_counter.items():
                if char not in chars_counter:
                    return False
                if count > chars_counter[char]:
                    return False
            return True
        
        total_length = 0
        for word in words:
            if check_validity(word):
                total_length+=len(word)
        return total_length