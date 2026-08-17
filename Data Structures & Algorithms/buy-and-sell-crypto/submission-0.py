class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        profit = 0
        for index, price in enumerate(prices):
            if price <= lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)
        if not profit:
            return 0 
        else:
            return profit

        