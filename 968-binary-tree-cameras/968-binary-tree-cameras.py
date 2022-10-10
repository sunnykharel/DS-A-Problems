# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        #if any node seen return true
        #if both children seen, no need for camera
        has_camera = dict()
        def recursion(node):
            if not node:
                return True
            if not (node.left or node.right): # is a root node
                return False
            
            left_seen, right_seen = recursion(node.left), recursion(node.right)
            if not(left_seen and right_seen):
                has_camera[node] = True
                return True
            else:
                #both children have been seen
                #we don't need a camera at this node
                if node.left and node.left in has_camera or node.right and node.right in has_camera:
                        return True
                else:
                    return False
                
        if not recursion(root):
            return len(has_camera)+1
        else:
            return len(has_camera)
            
            
            
            
            