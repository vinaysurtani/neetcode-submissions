class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                v2,v1 = stack.pop(), stack.pop()
                stack.append(v1-v2)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                v2, v1 = stack.pop(), stack.pop()
                stack.append(int(v1/v2))
            else:
                stack.append(int(token))
        return stack[0]