class Solution:
    def trap(self, h: List[int]) -> int:
        maxl = [0] * len(h)
        maxr = [0] * len(h)
        for i in range(len(maxl)):
            if i == 0:
                maxl[i] = h[i]
            else:
                maxl[i] = max(h[i], maxl[i - 1])
        print(maxl)
        for i in range(len(maxr) - 1, 0, -1):
            if i == len(maxr) - 1:
                maxr[i] = h[i]
            else:
                maxr[i] = max(h[i], maxr[i + 1])
        print(maxr)
        res = 0
        for i in range(len(h)):
            x = min(maxr[i], maxl[i]) - h[i]
            res += x if x > 0 else 0
            print(res)
        return res