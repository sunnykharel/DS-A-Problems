class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #values of indicies are unique
        string = ['' for i in range(len(s))]
        i = 0
        for char, idx in zip(s, indices):
            string[idx]=char
        return ''.join(string)