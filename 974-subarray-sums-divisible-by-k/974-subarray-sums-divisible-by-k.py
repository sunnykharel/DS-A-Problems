class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = [0]
        for idx, i in enumerate(A):
            prefix_sum.append(i+prefix_sum[idx])
        num_enc = dict()
        total = 0
        for i in prefix_sum:
            i_mod_k = i%K
            if (i_mod_k ) in num_enc:
                total+=num_enc[i_mod_k ]
            if (i_mod_k  - K) in num_enc:
                total+=num_enc[i_mod_k  - K]
            if i%K not in num_enc:
                num_enc[i_mod_k ] = 0
            num_enc[i_mod_k ]+=1
        return total