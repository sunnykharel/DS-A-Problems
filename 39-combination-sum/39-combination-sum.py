class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidate numbers --> set
        # target 
        # find all unique combos in target that sum to target
        # Recursive solution
        # at every step, we can either choose or not choose
        '''
        at idx i: we can stay here, move forward, that is for every step
        want to be able to stay here as long as curr_val+i*cand[i] < target 
        '''
        sol = []
        def recursion(i, remaining, path):
            if remaining < 0:
                return
            if remaining == 0:
                if path not in sol:
                    sol.append(path)
            if i >=len(candidates):
                return
            else:
                j = 1
                while remaining-candidates[i]*j >= 0:
                    recursion(i+1, remaining - candidates[i]*j, path+[candidates[i]]*j)
                    j+=1
                recursion(i+1, remaining, path)
            return
        recursion(0, target, [])
        return sol