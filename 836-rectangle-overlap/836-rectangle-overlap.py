class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # (0,0) (2,2)
        
        top_sq1, top_sq2 = max(rec1[1], rec1[3]), max(rec2[1], rec2[3])
        bot_sq1, bot_sq2 = min(rec1[1], rec1[3]), min(rec2[1], rec2[3])
        
        right_sq1, right_sq2 = max(rec1[0], rec1[2]), max(rec2[0], rec2[2])
        left_sq1, left_sq2 = min(rec1[0], rec1[2]), min(rec2[0], rec2[2])
        
        if top_sq1 <= bot_sq2:
            return False
        if bot_sq1 >= top_sq2:
            return False
        if right_sq1 <= left_sq2:
            return False
        if left_sq1 >= right_sq2:
            return False
        return True
        