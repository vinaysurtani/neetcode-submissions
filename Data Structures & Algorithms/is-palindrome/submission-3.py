class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_word = "".join([c.lower() for c in s if c.isalnum() == True])
        l = 0
        r = len(clean_word) - 1
        while l < r:
            if clean_word[l] == clean_word[r]:
                l += 1
                r -= 1
            else:
                return False
        return True