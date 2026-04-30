class Solution:
    def isValid(self, s: str) -> bool:
        bracs = {')':'(', '}':'{',']':'['}
        res  = []
        for c in s:
            if c in bracs:
                if res and res[-1] == bracs[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return len(res) == 0