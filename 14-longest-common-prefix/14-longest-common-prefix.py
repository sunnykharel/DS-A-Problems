class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length_word = min(strs, key=len)
        min_length = len(min_length_word)
        for longest in range(0,min_length):
            char = strs[0][longest]
            for s in strs:
                if s[longest]!=char:
                    return min_length_word[:longest]
        return min_length_word
                