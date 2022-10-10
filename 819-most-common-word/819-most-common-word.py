import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # at least 1 unbanned word
        # answer is unique
        paragraph = paragraph.replace(',', ' ')
        split = [''.join([i for i in word if i.isalpha()]) for word in paragraph.lower().split()]
        counts = collections.Counter(split)
        ban_set = set(banned)
        highest_count_word = ''
        highest_count_val = 0
        for word, count in counts.items():
            if word not in ban_set and count>highest_count_val:
                highest_count_word, highest_count_val = word, count
        return highest_count_word
                
            
            