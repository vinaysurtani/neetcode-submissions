class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        stack = []
        res = 0
        for t in tokens:
            if t not in ops:
                #print('enter if')
                stack.append(int(t))
                print(stack)
            else:
                #print('enter else')
                val2 = stack.pop()
                val1 = stack.pop()
                if t == '+':
                    res = (val1 + val2)
                elif t == '-':
                    res = (val1 - val2)
                elif t == '*':
                    res = (val1 * val2)
                else:
                    neg = False
                    if val2 < 0 or val1 <0:
                        neg = True
                    res = (abs(val1) // abs(val2))
                    if neg:
                        res *= -1
                stack.append(res)
                print(stack)
        return stack[-1]
            