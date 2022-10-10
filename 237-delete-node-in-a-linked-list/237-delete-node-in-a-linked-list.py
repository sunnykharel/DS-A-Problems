# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        
        node.val = node.next.val
        node.next = node.next.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        shift everything to the left
        
        
        
        4 5 1 9 null
        
        
        4 1 9 null
        
        
        
        
        """
        # def recursion(node):
        #     if not node:
        #         return -1001
        #     temp = node.val
        #     node.val = recursion(node.next)
        #     if node.next and node.next.val==-1001:
        #         node.next=None
        #     return temp
        # recursion(node)
                
            