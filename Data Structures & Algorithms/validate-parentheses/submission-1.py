class Solution:
    def isValid(self, s: str) -> bool:
        brkts_mtch = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for brkt in s:
            if brkt in brkts_mtch:
                stack.append(brkt)
            else:
                if not stack:
                    return False
                if brkts_mtch[stack[-1]] == brkt:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0