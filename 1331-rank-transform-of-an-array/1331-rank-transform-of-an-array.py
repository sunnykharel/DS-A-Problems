class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        import heapq
        from heapq import heapify, heappush, heappop
        heap = [(num,i) for i, num in enumerate(arr)]
        heapify(heap)
        
        rank = 0
        prev_number = -1
        while len(heap) > 0:
            element = heappop(heap)
            number, index = element[0], element[1]
            if rank == 0:
                prev_number = number
                rank = 1
            elif number != prev_number:
                rank +=1
                prev_number = number
            arr[element[1]] = rank
        return arr