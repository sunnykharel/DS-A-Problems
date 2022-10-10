class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()
        p = path.split("/")
        for i in p:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
            
        return '/'+'/'.join(stack)
        