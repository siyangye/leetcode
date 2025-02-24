class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        sell_price = [0] * n
        curr_price = 0
        for i in range(n-1, -1, -1):
            curr_price = max(curr_price, prices[i])
            sell_price[i] = curr_price
        for i in range(n):
            profit = max(profit, sell_price[i] - prices[i])
        return profit

        