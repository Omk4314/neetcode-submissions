class Solution:
    def isValid(self, s: str) -> bool:
        mp = {']': '[', ')': '(', '}': '{'}
        stack = []
        if len(s)%2 != 0:
            return False
        for c in s:
            if stack and c in mp and mp[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0