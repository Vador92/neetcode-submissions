class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {
            "]" : "[",
            ")": "(",
            "}": "{",
        }
        if len(s) == 1:
            return False

        for curr in s:
            if curr in ref.values():
                stack.append(curr)
            else:
                if not stack:
                    return False
                if stack.pop() != ref[curr]:
                    return False
        if stack:
            return False
        return True
            