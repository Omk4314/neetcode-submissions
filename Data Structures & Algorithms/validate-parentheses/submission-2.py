class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')': '(', '}': '{', ']': '['}

        stack = []
        for ch in s:
            if stack and mp.get(ch, '') == stack[-1]:
                stack.pop()
            else: stack.append(ch)
        return len(stack) == 0