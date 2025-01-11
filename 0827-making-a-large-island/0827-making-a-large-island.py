class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_id = -1 #it cannot be 0 or 1
        island_areas={}
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(m,n)->int:
            #change grid to id value. 
            if (0<=m<len(grid))and (0<=n<len(grid))and grid[m][n]==1:
                curr_area = 1
                grid[m][n]=island_id
                for m_inc,n_inc in directions:
                    new_m = m+m_inc
                    new_n = n+n_inc
                    curr_area +=dfs(new_m,new_n)
                return curr_area
            else:
                return 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n]==1:#island we didn't go thru yet. 
                    island_areas[island_id]= dfs(m,n)
                    island_id -=1 

        max_area = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n]==0:#we only flip 0
                    area = 1
                    surrounding = set()
                    for m_inc,n_inc in directions:
                        new_m = m+m_inc
                        new_n = n+n_inc
                        if 0<=new_m<len(grid) and 0<=new_n<len(grid) and grid[new_m][new_n]!=0:
                            surrounding.add(grid[new_m][new_n])
                    for ids in surrounding:
                        area +=island_areas[ids]
                    max_area = max(max_area,area)
        if max_area!=0:
            return max_area
        else:
            return (len(grid))**2


                    



