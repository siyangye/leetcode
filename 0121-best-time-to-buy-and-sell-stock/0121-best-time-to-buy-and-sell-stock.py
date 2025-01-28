class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        res = 0
        buy_price = float('inf')
        for i in range(len(prices)):
            buy_price = min(buy_price,prices[i])
            if buy_price < prices[i]:
                res = max(res,prices[i]-buy_price)
        return res 
                
                
        