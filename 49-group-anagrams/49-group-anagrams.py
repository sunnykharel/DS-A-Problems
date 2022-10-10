class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         need 26 bits to store info: keep a string of size 26 for each string
#         hash to a dictionary, insert it into there
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        # maps = {}
        # for s in strs:
        #     counts = [0 for i in range(26)]
        #     for char in s:
        #         counts[ord(char)-ord('a')]+=1
        #     hash_key = ''.join(str(counts))
        #     if hash_key not in maps:
        #         maps[hash_key] = []
        #     maps[hash_key].append(s)
        # solution = [map_item[1] for map_item in maps.items()]
        # return solution