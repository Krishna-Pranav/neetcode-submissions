class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = float("inf")
        for price in prices:
            if price < buy:
                buy = price
                continue
            maxProfit = max(maxProfit, price-buy)
        return maxProfit