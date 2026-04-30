class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closedN):
            #base case, open and closed brackets are n
            if openN == closedN == n:
                res.append("".join(stack))
                return
            #only add open bracket if its less than n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            # only add closed bracket if its less than no. of open brackets
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res