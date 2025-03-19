class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for sell in range(len(prices)):
            if prices[sell]<prices[buy]:
                buy = sell
            else:
                max_profit = max(prices[sell]-prices[buy], max_profit)
        return max_profit