# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        first_tree_vals = set()
        second_tree_vals = set()
        
        def dfs(root, tree_number):
            if tree_number == 1:
                first_tree_vals.add(root.val)
            elif tree_number == 2:
                second_tree_vals.add(root.val)
            if root.left:
                dfs(root.left, tree_number)
            if root.right:
                dfs(root.right, tree_number)
        
        dfs(root1, tree_number=1)
        dfs(root2, tree_number=2)
        
        for val in first_tree_vals:
            if target-val in second_tree_vals:
                return True
            
        for val in second_tree_vals:
            if target-val in first_tree_vals:
                return True
        return False
            
            
                
            
            
        