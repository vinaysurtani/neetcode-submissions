class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxlen = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                print(seen)
                l += 1
                print('l=',l)
            seen.add(s[r])
            print(seen)
            maxlen = max(maxlen, r - l + 1)
            print('maxlen=',maxlen)
            r += 1
            print('r=',r)
        return maxlen