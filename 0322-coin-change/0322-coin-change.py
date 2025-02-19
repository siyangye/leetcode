class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        res = []
        def dfs(i, path,curr_sum):
            #base case:
            if curr_sum == amount:
                res.append(path)
                return
            if curr_sum > amount:
                return
            if i < len(coins):
                return
            #if not:
            path.append(coins[i])
            dfs(i,path,curr_sum + coins[i])
            path.pop()
            dfs(i+1,path,curr_sum)
        dfs(0,[],0)
        if not res:
            return -1
        min_amount = len(res[0])
        for sums in res:
            min_amount = min(min_amount, len(sums))
        return min_amount

