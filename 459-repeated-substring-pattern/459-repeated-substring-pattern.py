class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        explored = set()
        def check_validity(substring):
            length = len(substring)
            n = len(s)
            if n%length!=0:
                return False
            for i in range(0,n,length):
                if s[i:i+length]!=substring:
                    return False
            return True
        
        for window_size in range(1, n//2+1):
            if n%window_size!=0:
                continue

            window = collections.deque()
            for i in range(window_size):
                window.append(s[i])

            for i in range(window_size, n):
                if i%window_size!=0 or window[-1]!=s[-1] or window[0]!=s[0]:
                    continue
                check = ''.join(window)
                if check_validity(check):
                    return True
                window.popleft()
                window.append(s[i])
        return False
            
            