class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        encountered = collections.defaultdict(int)
        count = 0
        for domino in dominoes:
            tup = (domino[0], domino[1])
            tup_rev = (domino[1], domino[0])
            if tup in encountered:
                count+=encountered[tup]
            if tup_rev in encountered and not tup[0]==tup[1]:
                count+=encountered[tup_rev]
    
            encountered[tup]+=1
        return count
                