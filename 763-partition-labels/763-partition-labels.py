class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #partition string into many parts as possible so each letter appears in at most one part
        
        '''
        requirement: any two parts cannot have the same letter
        
        brute force: we try every split, and check if it is valid or not:
        greedy approach: find the smallest split you can make from the left on
        
        linear approach: find last index of current letter in s, that is your new cutoff
        if you approach your cutoff, then you are good
        
        '''
        
        last_occ = dict()
        for i in range(len(S)-1, -1, -1):
            if S[i] not in last_occ:
                last_occ[S[i]] = i
        
        
        
        curr_letters = set()
        cutoff = -1
        res = []
        length = 0
        for i in range(0, len(S)):
            length+=1
            if i == cutoff:
                curr_letters = set()
                if len(res)==0:
                    res.append(length)
                else:
                    res.append(length)
                cutoff=-1
                length=0
                continue
                
            let = S[i]
            if cutoff == -1:
                cutoff = i
            last_occ_let = last_occ[let]
            if last_occ_let == i and i == cutoff:
                res.append(1)
                cutoff=-1
                curr_letters = set()
                length=0
            else:
                cutoff = max(cutoff, last_occ_let)
                curr_letters.add(let)
        return res