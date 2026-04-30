class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_b = {"}" : "{","]" : "[",")" : "("}
        for c in s:
            if c in close_b:
                if stack and stack[-1] == close_b[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack