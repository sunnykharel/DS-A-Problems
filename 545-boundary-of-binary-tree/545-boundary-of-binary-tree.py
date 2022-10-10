# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        '''
        steps:
            1. find left bound: 
                go all way left
            2. find right bound:
                go all way right
            
            
            3. get all the leaves: do an in order
                it hits all leaves, add leaves to list
            
        '''
        if not root: return []
        if not (root.right or root.left):
            return [root.val]
        
        start = [root.val]
        left_bound = []
        # get left
        node = root.left
        while(node):
            if not (node.left or node.right):
                break
            left_bound.append(node.val)
            if not node.left:
                node=node.right
            else:
                node = node.left
                
        print(left_bound)  
        
        # get right
        right_bound = []
        node = root.right
        while(node):
            if not (node.left or node.right):
                break
            right_bound.append(node.val)
            if not node.right:
                node = node.left
            else:
                node = node.right
            
        print(right_bound)
        #get leaves       
        leaves = []
        def in_order(root):
            nonlocal leaves
            if not root:
                return
            if not (root.left or root.right):
                leaves.append(root.val)
            else:
                in_order(root.left)
                in_order(root.right)
                     
        in_order(root)
        right_bound.reverse()
        return start+left_bound+leaves+right_bound
            
        