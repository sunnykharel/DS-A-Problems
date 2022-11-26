# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we need to do a dfs
        # while doing the dfs, we track the previously visited nodes
        # how do we keep track of the previously visited nodes?
        # we want O(logn) access as opposed to O(n) access
        
        # there may be a smarter way to use some math on nodes here
        # we can use sub problem property
        # if all nodes under this one are lesser value, then we are okay
        # given a certain node
        #   we can know whether all nodes below
        #       are greater?
        #       are lesser?
        # the bottom node wants to know if there
        # is anything greater that exists above it
        # the top node wants to know if there exists 
        # anything lower that exists above it
        # but it only returns the lowest
        return self.dfs(root, [])
    
    def dfs(self, root: TreeNode, path: list) -> int:
        # do a dfs
        # when we reach a node then
        # we want to check if anything before it is greater
        if root is None:
            return 0
        is_good = path == [] or max(path) <= root.val
        path.append(root.val)
        child_good_nodes = self.dfs(root.left, path) + self.dfs(root.right, path)
        path.pop()
        # print(root.val, is_good)
        return int(is_good) + child_good_nodes