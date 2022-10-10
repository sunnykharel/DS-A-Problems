class Solution:
    permutation_count=0
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[] for i in range(0, math.factorial(len(nums)))]
        chosen_init = []
        len_nums = len(nums)   
        def permute_helper( numbers: List[int], chosen: List[int]):
            if(len(chosen)==len_nums):
                print(chosen)
                permutations[self.permutation_count].extend(chosen)
                self.permutation_count+=1
            for i in range(0, len(numbers)):
                #choose
                choice = numbers.pop(i)
                chosen.append(choice)
                #explore
                permute_helper(numbers, chosen)
                #unchoose
                numbers.insert(i, choice)
                del chosen[-1]                
        permute_helper(nums, chosen_init)
        return permutations