class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #chars = Counter(s)
        dic = {}
        #print(chars)
        #sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        l = 0
        r = 0
        maxf = 0
        res = 0
        while r < len(s):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            maxf = max(maxf, dic[s[r]])
            if (r - l + 1) - maxf > k:
                dic[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res