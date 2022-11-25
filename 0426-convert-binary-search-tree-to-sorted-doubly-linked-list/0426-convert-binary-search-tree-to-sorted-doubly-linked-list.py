"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def make_ll_doubly_linked(self, start):
        prev = start
        if not prev:
            return start
        while prev.right:
            curr = prev.right
            curr.left = prev
            prev = curr
        prev.right = start
        start.left = prev
        return start
        
    def in_order_traversal(self, root):
        # as we do inorder, we create bi-link between prev and curr
        stack = collections.deque()
        curr = root
        prev = None
        start = None
        while curr or len(stack) > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue
            curr = stack.pop()
            if prev is None:
                start = curr
                prev = curr
            else:
                prev.right = curr
                prev = curr
            curr = curr.right
        
        return self.make_ll_doubly_linked(start)
    def in_order_traversal_recursive(self, root):
        if root:
            self.in_order_traversal_recursive(root.left)
            print(root.val)
            self.in_order_traversal_recursive(root.right)

        
        
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.in_order_traversal(root)
        # 1. in-order traversal to get the correct order of nodes
        # as you do in order, you create the LL, as you iterate
        #   BC Q calls for in-place, we must do iteratively
        '''
                4
              /.  \
             2     5
            / \.  
           1   3
        '''
        
        # How to do an in-order traversal recursively
            # choose(node.left)
            # choose(node)
            # choose(node.right)
        # iteratively, it calls for using a stack
            # if the node has a left
                # pop node onto stack
                # iterate left
            # if the node doesn't have a left
                #then you print
            # 
            # pop node onto stack
            # go left
        # whenever you pop a node for which you've gone left already
        # how do you know that you haven't gone left already?