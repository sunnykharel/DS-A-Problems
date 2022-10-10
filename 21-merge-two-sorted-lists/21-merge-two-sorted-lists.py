# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        big, small = None, None
        
        if l1.val>=l2.val:
            big=l1
            small=l2
        else:
            big,small=l2,l1
        
        node = ListNode()
        head = node
        while small and big:
            #when adding a value from other node, we skip two nodes
            if small.val<=big.val:
                head.next=small
                head = head.next
                small = small.next
                # temp = small.next
                # small.next = big
                # big.next = temp
                # small = temp
                
            else:
                head.next = big
                head = head.next
                big = big.next
        
        
        if not small and not big:
            return node.next
        
        remainder = small if small else big
        
        head.next = remainder
        return node.next
        
            