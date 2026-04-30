class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            if hours <= h:
                minK = min(minK,k)
                r = k - 1
            elif hours > h:
                l = k + 1
        return minK