class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0] # initialize lowest to use in array
        for price in prices:
            if price<lowest: #to find the lowest value in the array
                lowest=price 
            res=max(res,price-lowest) #take the value with the max difference, aka max profit
        return res