class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]*(amount +1)
        for i in range(1,amount+1):
            min_amount = float('inf')
            for coin in coins:
                
                diff = i - coin
                if diff < 0:
                    break
                #else
                min_amount = min(min_amount, 1 + dp[diff])
            dp[i] = min_amount
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
                