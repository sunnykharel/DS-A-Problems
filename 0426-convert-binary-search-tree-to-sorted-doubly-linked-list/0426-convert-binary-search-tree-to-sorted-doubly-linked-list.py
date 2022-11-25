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

    def in_order_traversal_to_ll(self, root):
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
        return start

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        in_order_ll = self.in_order_traversal_to_ll(root)
        in_order_doubly_ll = self.make_ll_doubly_linked(in_order_ll)
        return in_order_doubly_ll