# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        seq1=[]
        seq2=[]
        def in_order(node, seq):
            if not node:
                return
            if not(node.left or node.right):
                seq.append(node.val)
                return
            in_order(node.left, seq)
            in_order(node.right, seq)
            return 
        
        in_order(root1, seq1)
        in_order(root2, seq2)
        return seq1==seq2
            