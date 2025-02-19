class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            if n== 0:
                return 1
            if n < 0:
                return 0
            l = dfs(n -2)
            r = dfs(n -1)
            return l + r
        return dfs(n)