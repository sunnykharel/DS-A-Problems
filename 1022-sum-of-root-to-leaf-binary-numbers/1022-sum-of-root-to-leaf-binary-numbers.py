# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        '''
            we can have a tree algorithm
            
            Each tree sub problem returns the sum of its roots
            but we cannot just make it a sub problem
            because the solution doesn't build
            Example:
            1 calls left and right:
                left 0:
                    0 calls left and right
                        left 0:
                            returns 0
                        right 1:
                            returns
                             2
                right 1:
                    1 calls left and right:
                        left 0:
                            returns 0
                        right 1:
                            returns 1
        
        The next way to solve the problem is by doing the following
            we keep track of the path
            and then when we reach the leaf, then we add it to global
        '''
        global_sum = [0]
        
        def binary_to_dec(binary_str):
            decimal = 0
            length = len(binary_str)
            for power_of_2 in range(len(binary_str)):
                binary_bit = binary_str[length - 1 - power_of_2]
                binary_bit= int(binary_bit)
                decimal += binary_bit * (2**power_of_2)
            return decimal
        
        def dfs(node, path):
            # print(node.val, path)
            if node.left is None and node.right is None:
                # print(path)
                global_sum[0] += binary_to_dec(path)
                return
            if node.left:
                dfs(node.left, path+str(node.left.val))
            if node.right:
                dfs(node.right, path+str(node.right.val))
        
        dfs(root, f'{root.val}')
        return global_sum[0]
            
            
                
                
            
        
        