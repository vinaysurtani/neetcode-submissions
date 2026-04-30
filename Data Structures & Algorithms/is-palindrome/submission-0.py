class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(sa.lower() for sa in s if sa.isalnum())
        return strs[::-1] == strs 
        