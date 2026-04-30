class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversion = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c not in conversion:
                stack.append(c)
            else:
                if not stack or stack.pop() != conversion[c]:
                    return False
        if stack:
            return False
        return True