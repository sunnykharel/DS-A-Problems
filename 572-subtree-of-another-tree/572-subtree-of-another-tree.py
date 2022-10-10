# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # assuming that s is larger than t
        def check_same(t1, t2):
            if not(t1) and not(t2):
                return True
            if not(t1) or not(t2):
                return False
            if t1.val != t2.val:
                return False
            return check_same(t1.left, t2.left) and check_same(t1.right, t2.right)
        
        bfs = collections.deque()
        bfs.appendleft(s)
        while len(bfs)>0:
            node = bfs.popleft()
            if check_same(node, t):
                return True
            else:
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return False
        