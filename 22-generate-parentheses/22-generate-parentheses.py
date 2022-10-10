class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # rule with stacks
        # open paren, means adding to stack
        # close paren means removing from stack
        stack = deque()
        solutions = []
        # stack.appendleft()
        # stack.popleft
        
        #now we do a recursion
        #choose to add a '(', num_open>0
        #or choose to add a ')' if room available on the stack
        
        def recursion(path, num_open, num_closed):
            nonlocal stack
            if num_open == n and num_closed==n and len(stack) == 0:
                solutions.append(path)
                return
            if num_open<n:
                stack.appendleft('(')
                recursion(path+'(', num_open+1, num_closed)
                stack.popleft()
            if len(stack)>0:
                stack.popleft()
                recursion(path+')', num_open, num_closed+1)
                stack.appendleft('(')

            return
        recursion('', 0, 0)
        return solutions
                