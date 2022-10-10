# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        #left child: 2n, right child: 2n+1
        #we have a map node--> number
        #for each row we find the distance between last in a row by row bfs
        
        node_number = dict()
        
        prev = [root]
        node_number[root] = 1
        max_width = 0
        while len(prev) > 0:
            
            max_width = max( max_width, node_number[prev[-1]] - node_number[prev[0]]+1 )
            curr = []
            for node in prev:
                node_num = node_number[node]
                if node.left:
                    node_number[node.left] = node_num*2
                    curr.append(node.left)
                if node.right:
                    node_number[node.right] = node_num*2+1
                    curr.append(node.right)
            prev = curr
        return max_width
            