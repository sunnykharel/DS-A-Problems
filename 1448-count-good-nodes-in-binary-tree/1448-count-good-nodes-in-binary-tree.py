# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, [])
    
    def dfs(self, root: TreeNode, path: list) -> int:
        if root is None:
            return 0
        is_good = path == [] or max(path) <= root.val
        path.append(root.val)
        child_good_nodes = self.dfs(root.left, path) + self.dfs(root.right, path)
        path.pop()

        return int(is_good) + child_good_nodes