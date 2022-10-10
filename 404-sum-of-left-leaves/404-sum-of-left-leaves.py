# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #do a dfs
        #remember which way your parent went
        
        total = 0
        def dfs(node, prev_dir):
            nonlocal total
            if not node:
                return
            if not(node.right or node.left):
                if prev_dir==True:
                    total+=node.val
                return
            else:
                dfs(node.left, True)
                dfs(node.right, False)
                return
        dfs(root, False)
        return total