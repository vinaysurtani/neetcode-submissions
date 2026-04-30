class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1
        if s_count == t_count:
            return True
        return False