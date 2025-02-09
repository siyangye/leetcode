class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(i,j):
            if 0>i or i>=row or 0>j or j>= col or grid[i][j]!="1":
                return
            #if grid[i][j] == 1 
            grid[i][j]='2'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
                    
        print(grid)
        return count

