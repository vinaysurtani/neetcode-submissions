class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float("inf")
        maxProfit = 0
        for p in prices:
            minCost = min(minCost, p)
            maxProfit = max(maxProfit, p - minCost)
        return maxProfit