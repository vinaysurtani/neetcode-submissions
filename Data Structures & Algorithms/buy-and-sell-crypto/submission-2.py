class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float("inf")
        maxProfit = 0
        for p in prices:
            if p < minCost:
                minCost = p
            diff = p - minCost
            maxProfit = max(maxProfit, diff)
        return maxProfit