class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = [c.lower() for c in s if c.isalnum()]
        pali = "".join(newstr)
        print(pali)
        l = 0
        r = len(pali)-1
        while l < r:
            if pali[l] == pali[r]:
                l += 1
                r -= 1
            else:
                return False
        return True