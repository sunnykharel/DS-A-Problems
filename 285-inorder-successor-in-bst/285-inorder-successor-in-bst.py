# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # to do an in order, you go left, do current then do right
        
        variable = TreeNode(-1)
        
        def in_order(root):
            nonlocal variable
            if variable.val!=-1:
                return
            if not root:
                return
            in_order(root.left)
            if root.val>p.val and variable.val==-1:
                variable.val = root.val
            in_order(root.right)
        in_order(root)
        if variable.val==-1:
            return None
        return variable
            
            