class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float("inf")
        maxProfit = 0
        for num in prices:
            minVal = min(minVal, num)
            maxProfit = max(maxProfit, num - minVal)
        return maxProfit