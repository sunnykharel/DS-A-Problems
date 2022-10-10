class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # elements of arr2 are distinct
        # all elements in arr2 are in arr1
        
        #sort arr1 such that relative ordering in arr1 same as in arr2
            #loop thru arr2, add elems w/ counts to arr2
        #elems not in arr2 should be placed in end of arr1
        
        arr1_counts = collections.Counter(arr1)
        
        arr2_set = set(arr2)
        heap = []
        new_arr1 = []
        
        for i in arr2:
            new_arr1.extend([i]*arr1_counts[i])
            arr1_counts[i] = 0
        
        
        for num, counts in arr1_counts.items():
            if counts>0:
                heapq.heappush(heap, num)
        while heap:
            item = heapq.heappop(heap)
            new_arr1.extend([item]*arr1_counts[item])
        return new_arr1
        
            
        