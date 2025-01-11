class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        def dfs(r,c)->int:
            if 0<=r<len(grid) and 0<=c<len(grid[0])and grid[r][c]==1:
                grid[r][c]=0
                area = 1
                for inc_r,inc_c in directions:#loop
                    area += dfs(inc_r+r,inc_c+c)
                return area
            else:
                return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res,dfs(i,j))
        return res

        