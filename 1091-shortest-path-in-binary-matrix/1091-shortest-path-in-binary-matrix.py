class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        
        queue = deque([(0,0,1)])
        grid[0][0]=1
        n = len(grid)
        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while queue:
            size = len(queue)
            for i in range(size):
                curr_x,curr_y,curr_dist = queue.popleft()
                if curr_x== n-1 and curr_y == n-1:
                    return curr_dist
                for inc_x,inc_y in direction:
                    if 0<=curr_x+inc_x<=n-1 and 0<=curr_y+inc_y<=n-1 and grid[curr_x+inc_x][curr_y+inc_y]==0:
                        queue.append([curr_x+inc_x,curr_y+inc_y,curr_dist+1])
                        grid[curr_x+inc_x][curr_y+inc_y]=1
        return -1
                        


                